from django.db import models
from django.utils import timezone
import math
#untuk system agen resmi

#class-class abstract:
class Identitas(models.Model):
	nama=models.CharField(max_length=30)
	no_hp=models.CharField(max_length=15)
	akun=models.OneToOneField('Akun', on_delete=models.CASCADE, default=None)

	class Meta:
		abstract=True

#class-class non-abstract:
class Role(models.Model):
	nama=models.CharField(max_length=20)
	kemampuan=models.CharField(max_length=200, default=nama)

	def __str__(self):
		return self.nama

class Konsumen(Identitas):
	alamat=models.CharField(max_length=150)

	def __str__(self):
		return self.nama

class Personil(Identitas):
	bus=models.OneToOneField('Bus', on_delete=models.CASCADE)
	def __str__(self):
		return self.nama

class Admin(Identitas):
	agen=models.ForeignKey('Agen', on_delete=models.CASCADE, default=None)
	paraf=models.TextField()

	def __str__(self):
		return self.nama

class Agen(models.Model):
	nama=models.CharField(max_length=20)
	alamat=models.CharField(max_length=150)

	def __str__(self):
		return self.nama

class Akun(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	role=models.ForeignKey('Role', on_delete=models.CASCADE)
	status=models.IntegerField(default=0)
	
	def __str__(self):
		return self.username

class Bus(models.Model):
	no_body=models.CharField(max_length=7, primary_key=True)
	jurusan=models.OneToOneField('Jurusan', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.no_body

class Jurusan(models.Model):
	nama=models.CharField(max_length=40)

	def __str__(self):
		return self.nama

class Kategori_Barang(models.Model):
	#kategori dengan pk=1 adalah bisa ditimbang
	#kategori dengan pk=2 adalah tidak bisa ditimbang
	nama=models.CharField(max_length=20)

	def __str__(self):
		return self.nama

#untuk buat format report, invoice, dll dan juga menyimpan
	
class Invoice(models.Model):
	#no_invoice adalah pk dari class ini
	register=models.OneToOneField('Register', on_delete=models.CASCADE, null=True, blank=True)
	admin=models.OneToOneField('Admin', on_delete=models.CASCADE, null=True, blank=True)
	harga=models.DecimalField(max_digits=10, decimal_places=3)	
	
	#sepertinya rekam manual tidak dibutuhkan, karena rekam ke system perlu akun
	#@staticmethod
	#def rekam():
	#	pass

class Register(models.Model):
	#no_register adalah pk dari class ini
	tanggal=models.DateField(default=timezone.now)
	konsumen_pengirim=models.OneToOneField('Konsumen', on_delete=models.CASCADE, related_name="pengirim", null=True, blank=True)
	konsumen_penerima=models.OneToOneField('Konsumen', on_delete=models.CASCADE, related_name="penerima", null=True, blank=True)
	dari_agen=models.OneToOneField('Agen', on_delete=models.CASCADE, related_name='dari', null=True, blank=True)
	tujuan_agen=models.OneToOneField('Agen', on_delete=models.CASCADE, related_name='tujuan', null=True, blank=True)
	barang=models.CharField(max_length=20)
	berat_barang=models.DecimalField(max_digits=7, decimal_places=4)
	kategori_barang=models.OneToOneField('Kategori_Barang', on_delete=models.CASCADE, null=True, blank=True)
	jenis_packing=models.CharField(max_length=20, default="dus/box")
	keterangan=models.CharField(max_length=255, default="")

	@staticmethod
	def rekam(nama_pengirim, no_hp_pengirim, nama_penerima, no_hp_penerima):
		pengirim=Konsumen.objects.create(nama=nama_pengirim, no_hp=no_hp_pengirim)
		penerima=Konsumen.objects.create(nama=nama_penerima, no_hp=no_hp_penerima)
		Register.objects.create(konsumen_pengirim=pengirim, konsumen_penerima=penerima)

#report harian paling penting, system harus bisa nge-rekam transaksi baik yang dilakukan
#di dalam system dengan akun atau tanpa akun, selalu pakai method untuk mengisi
#tiap tabel pada tabel ini (kecuali no. invoice)
#report harian lebih baik tidak berelasi dengan apa pun, perlu diketahui juga jika invoice dan register 
#ada di database

class Report(models.Model):
	invoice=models.OneToOneField('Invoice', on_delete=models.CASCADE, null=True, blank=True)
	personil=models.OneToOneField('Personil', on_delete=models.CASCADE, null=True, blank=True)

	#method-method untuk rekam transaksi tanpa system oleh pengguna
	#@staticmethod
	#def rekam(no_invoice, id_personil):
	#	invoice=Invoice.objects.get(pk=no_invoice)
	#	personil=Personil.objects.get(pk=id_personil)
	#	Report.objects.create(invoice=invoice, personil=personil)
		



from django.db import models
from django.utils import timezone
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

	def __str__(self):
		return self.no_body

class Barang(models.Model):
	nama=models.CharField(max_length=20)
	berat=models.DecimalField(max_digits=7, decimal_places=4)
	harga=models.DecimalField(max_digits=10, decimal_places=3)
	jenis_packing=models.CharField(max_length=20, default="dus/box")
	dari=models.CharField(max_length=20)
	tujuan=models.CharField(max_length=20)

	def __str__(self):
		return self.nama


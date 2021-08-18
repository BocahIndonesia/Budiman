# Generated by Django 3.2.dev20201203083208 on 2021-08-17 12:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_auto_20210816_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harga', models.DecimalField(decimal_places=3, max_digits=10)),
                ('admin', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Kategori_Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(default=django.utils.timezone.now)),
                ('pengirim', models.CharField(max_length=30)),
                ('no_hp_pengirim', models.CharField(max_length=15)),
                ('penerima', models.CharField(max_length=30)),
                ('no_hp_penerima', models.CharField(max_length=15)),
                ('dari', models.CharField(max_length=20)),
                ('tujuan', models.CharField(max_length=20)),
                ('barang', models.CharField(max_length=20)),
                ('berat_barang', models.DecimalField(decimal_places=4, max_digits=7)),
                ('jenis_packing', models.CharField(default='dus/box', max_length=20)),
                ('keterangan', models.CharField(default='', max_length=255)),
                ('kategori_barang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cargo.kategori_barang')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.invoice')),
                ('personil', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.personil')),
            ],
        ),
        migrations.DeleteModel(
            name='Barang',
        ),
        migrations.AddField(
            model_name='invoice',
            name='register',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.register'),
        ),
    ]
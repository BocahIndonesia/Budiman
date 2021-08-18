# Generated by Django 3.2.dev20201203083208 on 2021-08-18 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0003_auto_20210817_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='dari',
        ),
        migrations.RemoveField(
            model_name='register',
            name='no_hp_penerima',
        ),
        migrations.RemoveField(
            model_name='register',
            name='no_hp_pengirim',
        ),
        migrations.RemoveField(
            model_name='register',
            name='penerima',
        ),
        migrations.RemoveField(
            model_name='register',
            name='pengirim',
        ),
        migrations.RemoveField(
            model_name='register',
            name='tujuan',
        ),
        migrations.AddField(
            model_name='register',
            name='dari_agen',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dari', to='cargo.agen'),
        ),
        migrations.AddField(
            model_name='register',
            name='konsumen_penerima',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penerima', to='cargo.konsumen'),
        ),
        migrations.AddField(
            model_name='register',
            name='konsumen_pengirim',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengirim', to='cargo.konsumen'),
        ),
        migrations.AddField(
            model_name='register',
            name='tujuan_agen',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tujuan', to='cargo.agen'),
        ),
        migrations.AlterField(
            model_name='register',
            name='kategori_barang',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.kategori_barang'),
        ),
    ]

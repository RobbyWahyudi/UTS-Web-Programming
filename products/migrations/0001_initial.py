# Generated by Django 4.2.6 on 2023-11-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(max_length=100)),
                ('harga', models.IntegerField()),
                ('jenis', models.CharField(max_length=50)),
            ],
        ),
    ]

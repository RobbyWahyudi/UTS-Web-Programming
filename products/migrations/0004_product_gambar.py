# Generated by Django 4.2.6 on 2023-11-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_kategori_remove_product_jenis_product_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gambar',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]

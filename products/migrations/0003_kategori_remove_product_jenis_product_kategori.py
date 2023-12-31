# Generated by Django 4.2.6 on 2023-11-09 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='jenis',
        ),
        migrations.AddField(
            model_name='product',
            name='kategori',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.kategori'),
            preserve_default=False,
        ),
    ]

from django.db import models


# Create your models here.
class Kategori(models.Model):
    kategori = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.kategori}"


class Product(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    nama_produk = models.CharField(max_length=100)
    harga = models.IntegerField()
    gambar = models.CharField(max_length=100)

from django.contrib import admin
from .models import Product, Kategori


class ProductKategori(admin.ModelAdmin):
    list_display = (
        "nama_produk",
        "harga",
        "kategori",
        "gambar",
    )


admin.site.register(Product, ProductKategori)
admin.site.register(Kategori)

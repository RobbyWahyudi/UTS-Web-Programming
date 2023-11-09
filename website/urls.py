from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("", include("about.urls")),
    path("", include("contact.urls")),
    path("", include("products.urls")),
]

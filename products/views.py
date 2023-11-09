from django.http import HttpResponse
from django.template import loader
from .models import Product


# Create your views here.
def products(request):
    products = Product.objects.all().values()
    context = {
        "title": "Products",
        "products": products,
    }
    template = loader.get_template("product.html")

    return HttpResponse(template.render(context, request))

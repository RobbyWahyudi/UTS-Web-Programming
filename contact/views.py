from django.http import HttpResponse
from django.template import loader


# Create your views here.
def contact(request):
    context = {
        "title": "Contact",
    }
    template = loader.get_template("contact.html")

    return HttpResponse(template.render(context))

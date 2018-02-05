from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import asifURL

# Create your views here.

def asif_redirect_view(request, shortcode=None, *args, **kwargs):
    try:
        obj = asifURL.objects.get(shortcode=shortcode)
    except:
        obj = asifURL.objects.all().first()
    return HttpResponse("hello {sc}".format(sc=obj.url))

class asifCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("hello again {sc}".format(sc=shortcode))

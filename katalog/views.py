from django.shortcuts import render
from .models import *
# TODO: Create your views here.
def show_catalog(request):
    data_catalogue = CatalogItem().objects.all()
    context = {
        'list_katalog' : data_catalogue
    }
    return render(request, 'katalog.html', context)

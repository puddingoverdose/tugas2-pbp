from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render
from .models import *
# Create your views here

def show_watchlist(request):
    data = MyWatchList.objects.all()
    context = {
                'list_barang': data,
               }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



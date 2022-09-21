from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request) :
    data = WatchList.objects.all()
    context = {
        'movie_list' : data,
        'nama' : 'Aulia Najwa Salsabila',
        'npm' : '2106751524',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request) :
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request) : 
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

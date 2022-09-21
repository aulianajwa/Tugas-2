from ast import If
from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request) :
    data = WatchList.objects.all()
    
    watched_true = 0
    watched_false = 0
    output = ""

    for i in data :
        if(i.watched) : 
            watched_true += 1
        else : 
            watched_false += 1

    if watched_true > watched_false : 
        output = "Selamat, kamu sudah banyak menonton!"
    elif watched_true == watched_false or watched_true < watched_false :
        output = "Wah, kamu masih sedikit menonton!"

    context = {
        'movie_list' : data,
        'nama' : 'Aulia Najwa Salsabila',
        'npm' : '2106751524',
        'watched_true' : watched_true,
        'watched_false' : watched_false,
        'output' : output
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request) :
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request) : 
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

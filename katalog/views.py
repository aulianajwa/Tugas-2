from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request) :
    data_item = CatalogItem.objects.all()
    context = {
        'list_item' :data_item,
        'nama' : 'Aulia Najwa Salsabila',
        'npm' : '2106751524'
    }
    return render(request, "katalog.html", context)
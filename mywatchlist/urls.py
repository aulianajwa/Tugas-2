from django.urls import path
from mywatchlist.views import show_watchlist, show_xml, show_json

app_name = 'wishlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_watchlist,name='show_watchlist')
]
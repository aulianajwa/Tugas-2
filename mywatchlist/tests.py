from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.views import show_watchlist, show_json, show_xml
# Create your tests here.

class Test(TestCase) :
    def test_html(self) :
        client = Client()
        response = client.get(reverse("mywatchlist:show_watchlist"))
        self.assertEquals(response.status_code,200)
    
    def test_json(self) :
        client = Client()
        response =client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code,200)
    
    def test_xml(self) :
        client = Client()
        response = client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code,200)
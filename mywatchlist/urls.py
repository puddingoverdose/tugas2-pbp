from django.urls import path
from .views import *
app_name = 'mywatchlist'

urlpatterns = [
        path('', show_watchlist, name='show_wishlist'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json')
        ]

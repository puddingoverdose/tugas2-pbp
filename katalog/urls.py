from django.urls import path
from .views import *
# TODO: Implement Routings Here
app_name = 'katalog'

urlpatterns = [
    path('', show_catalog),
]
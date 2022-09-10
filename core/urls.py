from .views import *
from django.urls import path

urlpatterns = [
    path('newObject/', newObject, name='newObject'),
    path('listObject/', listObject, name='listObject'),
    path('getObject/', getObject, name='getObject'),
]

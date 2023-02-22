from django.urls import path
from . import views

#maps each url with its view function
urlpatterns = [
    #/products
    path('', views.index),
    #/products/new
    path('new', views.new),
]
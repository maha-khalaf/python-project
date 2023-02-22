from django.http import HttpResponse
from django.shortcuts import render
from .models  import Product

# index is used as the default page
def index(request):
    #declare a variable that includes all objects in product model
    products = Product.objects.all()

    #use "products"in index.html
    return render(request, 
        'index.html', 
        #dictionary containing data to be passed to index.html template
        {'products': products})


def new(request):
    return HttpResponse('<h1>New Products</h1>')
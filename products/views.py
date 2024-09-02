from django.http import HttpResponse
from django.shortcuts import render
from .models import product
def show_products(request):
   all_products = product.objects.all
   return render(request,"products/show_product.html",{'my_products':all_products})
 
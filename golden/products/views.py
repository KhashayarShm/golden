from django.http import JsonResponse
import requests

# def gold_prices(request):
#     iran_price = requests.get("https://api.example.com/iran-gold").json()
#     world_price = requests.get("https://api.example.com/world-gold").json()
#     return JsonResponse({
#         "iran": iran_price,
#         "world": world_price
#     })
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})
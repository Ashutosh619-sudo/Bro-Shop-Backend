from django.db.models import manager
from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .product import products
from .models import Product
from .serializer import ProductSerializer


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

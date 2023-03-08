from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Firm,Brand,Product,Purchases,Sales
from .serializers import CategorySerializer

# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

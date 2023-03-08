from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Category,Firm,Brand,Product,Purchases,Sales
from .serializers import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name']

from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Category,Firm,Brand,Product,Purchases,Sales
from .serializers import CategorySerializer,CategoryProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions

# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['name']
    permission_classes=[DjangoModelPermissions]
    
    def get_serializer_class(self):
        if self.request.query_params.get("name"):
            return CategoryProductSerializer
        
        return super().get_serializer_class()

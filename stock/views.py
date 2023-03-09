from django.shortcuts import render
from rest_framework import viewsets,filters,status
from rest_framework.response import Response
from .models import Category,Firm,Brand,Product,Purchases,Sales
from .serializers import CategorySerializer,CategoryProductSerializer,BrandSerializer,FirmSerializer,ProductSerializer,PurchasesSerializer
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

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    
class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]    
    
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "brand"]
    search_fields = ["name"]  
    
class PurchasesView(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["firm", "product"]
    search_fields = ["firm"]  
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) #raise_exception ın amacı serializer validasyondan geçemezse hata versin.
        #! #### ADD PRODUCT STOCK #### 
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
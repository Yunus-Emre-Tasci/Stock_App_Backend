from rest_framework import serializers
from .models import Category,Firm,Brand,Product,Purchases,Sales

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields = ("id", "name")
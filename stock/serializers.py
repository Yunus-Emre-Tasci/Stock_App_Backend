from rest_framework import serializers
from .models import Category,Firm,Brand,Product,Purchases,Sales
import datetime

class CategorySerializer(serializers.ModelSerializer):
    product_count=serializers.SerializerMethodField() #bu method readonly, sadece get ile görüntülenir.
    class Meta:
        model=Category
        fields = ("id", "name","product_count")
        
    def get_product_count(self,obj):
        return Product.objects.filter(category_id=obj.id).count()
    
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField() #bu metod otomatik readonly
    brand=serializers.StringRelatedField() #bu metodun amacı, Foreign key ile bağlı olduğu için sadece id si geliyordu, sadece id si gelmesin, ilgili brandin ismi de gelsin demek.
    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    class Meta:
        model=Product
        fields=("id","name","category","category_id","brand","brand_id","stock",)    
        
        read_only_fields=("stock",) #readonly yapmamızın amacı buradaki stock miktarının purchase ve sales lara göre değişiecek olması.
        
class CategoryProductSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    product_count=serializers.SerializerMethodField() #bu method readonly, sadece get ile görüntülenir.
    class Meta:
        model=Category
        fields = ("id", "name","product_count","products")
        
    def get_product_count(self,obj):
        return Product.objects.filter(category_id=obj.id).count()
    
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "image"
        )
        
class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            "id",
            "name",
            "phone",
            "image",
            "address"
        )                
        
class PurchasesSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    firm=serializers.StringRelatedField()
    brand=serializers.StringRelatedField()
    product=serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    category=serializers.SerializerMethodField()
    time_hour=serializers.SerializerMethodField()
    createds=serializers.SerializerMethodField()
    class Meta:
        model=Purchases
        fields=("id","user","user_id","firm","firm_id","brand","brand_id","product","product_id","quantity","price","price_total","updated","category","time_hour","createds",)   
        
    # def get_category(self,obj):
        # product=Product.objects.get(id=obj.product_id)
        # return Category.objects.get(id=product.category_id).name  
    # yukarıdaki fonksiyonun kısa yazımı
    def get_category(self, obj):
        return obj.product.category.name       
        
    def get_time_hour(self,obj):
        return datetime.datetime.strftime(obj.createds,"%H:%M")    
    
    def get_createds(self,obj):
        return datetime.datetime.strftime(obj.createds, "%d,%m,%Y")
    
class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            "id",
            "name",
            "phone",
            "image",
            "address"
        )                
        
class SalesSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    brand=serializers.StringRelatedField()
    product=serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    time_hour=serializers.SerializerMethodField()
    createds=serializers.SerializerMethodField()
    class Meta:
        model=Sales
        fields=("id","user","user_id","brand","brand_id","product","product_id","quantity","price","price_total","time_hour","createds",)   
        
   
        
    def get_time_hour(self,obj):
        return datetime.datetime.strftime(obj.createds,"%H:%M")    
    
    def get_createds(self,obj):
        return datetime.datetime.strftime(obj.createds, "%d,%m,%Y")    
    
    
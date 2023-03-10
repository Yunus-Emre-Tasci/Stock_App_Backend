from rest_framework import serializers
from .models import Category,Firm,Brand,Product,Purchases,Sales

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
        
        read_only_fields=("stock",) #readonly yapmamızın amacı buradaki stock miktarının purchase ve sales lara göre değişiecek.
        
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
    class Meta:
        model=Purchases
        fields=("id","user","user_id","firm","firm_id","brand","brand_id","product","product_id","quantity","price","price_total","createds","updated",)        
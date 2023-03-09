from django.urls import path 
from rest_framework import routers
from .views import CategoryView,BrandView,FirmView,ProductView,PurchasesView

router=routers.DefaultRouter()
router.register("categories",CategoryView)
router.register("brands", BrandView)
router.register("firms", FirmView)
router.register("products", ProductView)
router.register("purchases", PurchasesView)

urlpatterns = [
    
] + router.urls

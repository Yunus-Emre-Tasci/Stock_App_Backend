from django.urls import path 
from rest_framework import routers
from .views import CategoryView,BrandView,FirmView,ProductView

router=routers.DefaultRouter()
router.register("categories",CategoryView)
router.register("brands", BrandView)
router.register("firms", FirmView)
router.register("products", ProductView)

urlpatterns = [
    
] + router.urls

from django.db.models.signals import pre_save #pre kullanılmasının amacı, database e kayıt yapılmadan önce price total ı da hesaplayıp purchases objesine ekleyip öyle göndereceğiz
from django.dispatch import receiver
from .models import Purchases,Sales

@receiver(pre_save,sender=Purchases)
def calculate_total_price(sender,instance,**kwargs):
    instance.price_total=instance.quantity*instance.price  # signal kullandığımızı apps.py içerisinde belirtiyorduk.
    
@receiver(pre_save,sender=Sales)
def calculate_total_price(sender,instance,**kwargs):
    instance.price_total=instance.quantity*instance.price    
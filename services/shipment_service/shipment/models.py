from django.db import models
from services.order_service.order.models import Order 
# Create your models here.
class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=255)
    shipment_status = models.CharField(max_length=50, choices=[("In Transit", "In Transit"), ("Delivered", "Delivered"), ("Pending", "Pending")])
    
    def __str__(self):
        return f"Shipment {self.tracking_number} - {self.shipment_status}"

from django.db import models
from services.order_service.order.models import Order
# Create your models here.
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=[("Credit Card", "Credit Card"), ("PayPal", "PayPal"), ("Cash on Delivery", "Cash on Delivery")])
    payment_status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Completed", "Completed"), ("Failed", "Failed")])
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.payment_status}"

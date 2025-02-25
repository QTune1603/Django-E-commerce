from django.db import models
from customer.models import Customer

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Shipped", "Shipped"), ("Delivered", "Delivered")])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
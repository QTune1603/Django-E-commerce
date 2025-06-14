from django.db import models

class Cart(models.Model):
    customer = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book_id = models.IntegerField()  # 👉 Thay vì ForeignKey
    quantity = models.PositiveIntegerField(default=1)

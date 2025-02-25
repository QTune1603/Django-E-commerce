from django.urls import path
from .views import add_to_cart, cart_view

urlpatterns = [
    path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),  # Add to Cart URL
    path('', cart_view, name='cart_view'),  # Cart View URL
]

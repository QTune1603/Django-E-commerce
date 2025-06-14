from django.urls import path
from .views import cart_view
from .views import cart_view, add_to_cart
from . import views

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', views.update_quantity, name='update_quantity'),
]
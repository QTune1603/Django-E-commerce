# cart/views.py
from django.shortcuts import render, redirect
from .models import Cart, CartItem
from .models import Book

def cart_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(customer=request.user.customer).first()
        if not cart:
            cart = Cart.objects.create(customer=request.user.customer)
        items = CartItem.objects.filter(cart=cart)
        total = sum(item.book.price * item.quantity for item in items)
        return render(request, 'cart/cart_view.html', {'items': items, 'total': total})
    else:
        return redirect('login')

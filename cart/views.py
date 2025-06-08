from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Cart,CartItem
from book.models import Book
from django.shortcuts import render, redirect
from customer.models import Customer


@require_POST
def add_to_cart(request, book_id):
    user = request.user
    customer = Customer.objects.get(user=user)

    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(customer=user) 

    item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_view')

@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__customer=request.user)
    item.delete()
    return redirect('cart_view')

def cart_view(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    cart, created = Cart.objects.get_or_create(customer=user)
    cart_items = CartItem.objects.filter(cart=cart)

    total = sum(item.book.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart_view.html', {
        'cart_items': cart_items,
        'total': sum(item.book.price * item.quantity for item in cart_items)
    })

@require_POST
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__customer=request.user)
    action = request.POST.get('action')

    if action == 'increment':
        item.quantity += 1
        item.save()
    elif action == 'decrement':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
    # Luôn trả về HttpResponse
    return redirect('cart_view')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from customer.models import Customer

@login_required
def payment_home(request):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total = sum(item.book.price * item.quantity for item in cart_items)

    # Nếu bạn muốn xử lý form POST ở đây sau này, thêm xử lý ở dưới

    return render(request, 'payment/home.html', {
        'cart_items': cart_items,
        'total': total
    })

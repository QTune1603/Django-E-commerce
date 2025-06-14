from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from services.customer_service.customer.models import Customer
from .models import Order

@login_required
def order_history(request):
    customer = Customer.objects.using('default').get(user=request.user)
    orders = Order.objects.using('order').filter(customer=customer).order_by('-created_at')
    return render(request, 'order/order_history.html', {'orders': orders})

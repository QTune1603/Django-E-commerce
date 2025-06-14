from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Customer

@login_required
def customer_profile(request):
    return render(request, "customer/profile.html")

@login_required
def edit_profile(request):
    customer = Customer.objects.get(user=request.user)

    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.phone = request.POST.get('phone')
        customer.save()
        return redirect('customer_profile')
    return render(request, 'customer/edit_profile.html', {'customer': customer})


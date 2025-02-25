from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def customer_profile(request):
    return render(request, "customer/profile.html")

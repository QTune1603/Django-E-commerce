from django.shortcuts import render

def payment_home(request):
    return render(request, "payment/home.html")

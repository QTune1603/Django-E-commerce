from django.urls import path
from .views import customer_profile

urlpatterns = [
    path("profile/", customer_profile, name="customer_profile"),
]

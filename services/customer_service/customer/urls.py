from django.urls import path
from .views import customer_profile
from . import views

urlpatterns = [
    path("profile/", customer_profile, name="customer_profile"),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

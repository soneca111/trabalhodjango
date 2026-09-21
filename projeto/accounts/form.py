from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ("username", "email")
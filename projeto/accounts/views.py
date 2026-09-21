from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.form import CustomerUserCreationForm

class AccountCreateView(CreateView):
    form_class = CustomerUserCreationForm
    template_name = 'registro/signup_form.html'
    success_url = reverse_lazy('remedio')
    success_message = "Usuário Criado com sucesso!"

class Inicial(CreateView):
    form_class = CustomerUserCreationForm
    template_name = 'registro/login.html'
    success_url = reverse_lazy('remedio')
    success_message = "Usuário Criado com sucesso!"
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.form import CustomerUserCreationForm
from .models import CustomerUser


class AccountCreateView(CreateView):
    form_class = CustomerUserCreationForm
    template_name = 'registro/signup_form.html'
    success_url = reverse_lazy('remedio')
    success_message = "Usuário Criado com sucesso!"


@login_required
def desativar_conta(request, pk):
    # Busca o usuário pelo ID ou retorna 404 se não existir
    usuario = get_object_or_404(CustomerUser, pk=pk)

    if request.method == 'POST':
        # Faz a exclusão lógica
        usuario.ativo = False
        usuario.is_active = False
        usuario.save()

        # Encerra a sessão do usuário
        logout(request)

        messages.success(
            request, f'O usuário "{usuario.username}" foi desativado com sucesso.'
        )
        return redirect('login')

    return render(request, 'registro/excluirusuario.html', {'usuario': usuario})
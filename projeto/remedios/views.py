
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from remedios.models import Remedio
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from remedios.form import RemedioForm
# View que renderiza a página inicial com o layout e a sidebar


@login_required
def index(request):
    
    remedios = Remedio.objects.filter(usuario=request.user)
    context = {"todos_remedios": remedios}
    return render(request, 'index.html', context)

@login_required
def remedio_create(request):
    context = {}
    form = RemedioForm(request.POST or None, request.FILES or None)
    context['form'] = form
    context['titulo'] = "Adicionar remedio"
    context['botao'] = "Adicionar"

    if request.method == 'POST':
        if form.is_valid():
            remedio = form.save(commit=False)
            remedio.usuario = request.user  # type: ignore (Garantir 12 espaços / 3 tabs de recuo)
            remedio.save()

            messages.success(request, "Remedio criado com sucesso")
            return redirect('remedio')

    return render(request, 'remedio/formRemedio.html', context)



def remedio_update(request,id):
    context={}
    remedios = get_object_or_404(Remedio, id=id, usuario=request.user)
    form = RemedioForm(request.POST or None, instance=remedios)
    context['form'] = form
    context['titulo'] = "Alterar remedio"
    context['botao'] = "Alterar"

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Remedio atualizado com sucesso")
            return redirect('remedio')

    return render(request,'remedio/formRemedio.html', context)




def remedio_deletar(request,id):
    context={}
    remedios = get_object_or_404(Remedio, id=id, usuario=request.user)
    context['object'] = remedios
    context['titulo'] = 'Excluindo remedio'
    context['botao'] = 'Excluir'

    if request.method == 'POST':
        remedios.delete()
        messages.success(request,"Remedio deletado com sucesso")
        return redirect('remedio')

    return render(request,"remedio/confirmarExclusao.html",context)


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from .form import (
    ConsultaMedicaForm,
    EstoqueRemedioForm,
    RegistroSintomaForm,
    RemedioForm,
    SinalVitalForm,
)
from .models import (
    ConsultaMedica,
    EstoqueRemedio,
    RegistroSintoma,
    Remedio,
    SinalVital,
)



# REMÉDIOS (CRUD PRINCIPAL)
@login_required
def index(request):
    todos_remedios = Remedio.objects.filter(usuario=request.user)
    return render(request, 'index.html', {'todos_remedios': todos_remedios})


@login_required
def remedio_create(request):
    form = RemedioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        remedio = form.save(commit=False)
        remedio.usuario = request.user
        remedio.save()
        messages.success(request, 'Remédio cadastrado com sucesso!')
        return redirect('remedio')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Adicionar Remédio', 'botao': 'Salvar'},
    )


@login_required
def remedio_update(request, id):
    remedio = get_object_or_404(Remedio, id=id, usuario=request.user)
    form = RemedioForm(request.POST or None, instance=remedio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Remédio atualizado com sucesso!')
        return redirect('remedio')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Alterar Remédio', 'botao': 'Atualizar'},
    )


@login_required
def remedio_deletar(request, id):
    remedio = get_object_or_404(Remedio, id=id, usuario=request.user)
    remedio.delete()
    messages.success(request, 'Remédio removido com sucesso!')
    return redirect('remedio')



# ESTOQUE DE REMÉDIOS

@login_required
def estoque_list(request):
    estoques = EstoqueRemedio.objects.filter(usuario=request.user)
    return render(
        request, 'remedio/estoque_list.html', {'estoques': estoques}
    )


@login_required
def estoque_create(request):
    form = EstoqueRemedioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        estoque = form.save(commit=False)
        estoque.usuario = request.user
        estoque.save()
        messages.success(request, 'Estoque cadastrado com sucesso!')
        return redirect('estoque_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Adicionar Estoque', 'botao': 'Salvar'},
    )


@login_required
def estoque_update(request, id):
    estoque = get_object_or_404(EstoqueRemedio, id=id, usuario=request.user)
    form = EstoqueRemedioForm(request.POST or None, instance=estoque)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Estoque atualizado com sucesso!')
        return redirect('estoque_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Alterar Estoque', 'botao': 'Atualizar'},
    )


@login_required
def estoque_delete(request, id):
    estoque = get_object_or_404(EstoqueRemedio, id=id, usuario=request.user)
    estoque.delete()
    messages.success(request, 'Estoque removido com sucesso!')
    return redirect('estoque_list')



# REGISTRO DE SINTOMAS
@login_required
def sintoma_list(request):
    sintomas = RegistroSintoma.objects.filter(usuario=request.user).order_by(
        '-data_ocorrencia'
    )
    return render(
        request, 
        'remedio/sintomas_list.html', 
        {'sintomas': sintomas}
    )


@login_required
def sintoma_create(request):
    form = RegistroSintomaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        sintoma = form.save(commit=False)
        sintoma.usuario = request.user
        sintoma.save()
        messages.success(request, 'Sintoma registrado com sucesso!')
        return redirect('sintoma_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Registrar Sintoma', 'botao': 'Salvar'},
    )


@login_required
def sintoma_update(request, id):
    sintoma = get_object_or_404(RegistroSintoma, id=id, usuario=request.user)
    form = RegistroSintomaForm(request.POST or None, instance=sintoma)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Sintoma atualizado com sucesso!')
        return redirect('sintoma_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Alterar Sintoma', 'botao': 'Atualizar'},
    )


@login_required
def sintoma_delete(request, id):
    sintoma = get_object_or_404(RegistroSintoma, id=id, usuario=request.user)
    sintoma.delete()
    messages.success(request, 'Sintoma removido com sucesso!')
    return redirect('sintoma_list')



# CONSULTAS MÉDICAS
@login_required
def consulta_list(request):
    consultas = ConsultaMedica.objects.filter(usuario=request.user).order_by(
        'data_hora'
    )
    return render(
        request, 'remedio/consultas_list.html', {'consultas': consultas}
    )


@login_required
def consulta_create(request):
    form = ConsultaMedicaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        consulta = form.save(commit=False)
        consulta.usuario = request.user
        consulta.save()
        messages.success(request, 'Consulta agendada com sucesso!')
        return redirect('consulta_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Agendar Consulta', 'botao': 'Salvar'},
    )


@login_required
def consulta_update(request, id):
    consulta = get_object_or_404(ConsultaMedica, id=id, usuario=request.user)
    form = ConsultaMedicaForm(request.POST or None, instance=consulta)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Consulta atualizada com sucesso!')
        return redirect('consulta_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {'form': form, 'titulo': 'Alterar Consulta', 'botao': 'Atualizar'},
    )


@login_required
def consulta_delete(request, id):
    consulta = get_object_or_404(ConsultaMedica, id=id, usuario=request.user)
    consulta.delete()
    messages.success(request, 'Consulta removida com sucesso!')
    return redirect('consulta_list')



# SINAIS VITAIS
@login_required
def sinal_vital_list(request):
    sinais = SinalVital.objects.filter(usuario=request.user).order_by(
        '-data_afericao'
    )
    return render(request, 'remedio/sinais_vitais_list.html', {'sinais': sinais})


@login_required
def sinal_vital_create(request):
    form = SinalVitalForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        sinal = form.save(commit=False)
        sinal.usuario = request.user
        sinal.save()
        messages.success(request, 'Sinal vital registrado com sucesso!')
        return redirect('sinal_vital_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {
            'form': form,
            'titulo': 'Registrar Sinal Vital',
            'botao': 'Salvar',
        },
    )


@login_required
def sinal_vital_update(request, id):
    sinal = get_object_or_404(SinalVital, id=id, usuario=request.user)
    form = SinalVitalForm(request.POST or None, instance=sinal)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Sinal vital atualizado com sucesso!')
        return redirect('sinal_vital_list')
    return render(
        request,
        'remedio/formRemedio.html',
        {
            'form': form,
            'titulo': 'Alterar Sinal Vital',
            'botao': 'Atualizar',
        },
    )


@login_required
def sinal_vital_delete(request, id):
    sinal = get_object_or_404(SinalVital, id=id, usuario=request.user)
    sinal.delete()
    messages.success(request, 'Sinal vital removido com sucesso!')
    return redirect('sinal_vital_list')
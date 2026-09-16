
from django.shortcuts import render
from remedios.models import Remedio
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from remedios.form import RemedioForm
# View que renderiza a página inicial com o layout e a sidebar
def index(request):
    remedios = Remedio.objects.all()
    context = {"todos_remedios":remedios}
    return render(request, 'remedio.html',context)


class RemedioCreateView(CreateView):
    model = Remedio
    form_class = RemedioForm
    template_name = 'criarRemedio.html' 
    success_url = reverse_lazy('remedio')
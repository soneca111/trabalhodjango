from django import forms
from .models import Remedio, EstoqueRemedio, RegistroSintoma, ConsultaMedica, SinalVital

class RemedioForm(forms.ModelForm):
    class Meta:
        model = Remedio
        fields = ("nome", "dosagem", "quantidade", "horario", "observacoes")
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'dosagem': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'horario': forms.TimeInput(
                format='%H:%M',
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EstoqueRemedioForm(forms.ModelForm):
    class Meta:
        model = EstoqueRemedio
        fields = ("nome_remedio", "quantidade_atual", "data_validade")
        widgets = {
            'nome_remedio': forms.TextInput( attrs={'class': 'form-control'}),
            'quantidade_atual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Quantidade de caixas '}),
            'data_validade': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }

class RegistroSintomaForm(forms.ModelForm):
    class Meta:
        model = RegistroSintoma
        fields = ("sintoma", "intensidade", "data_ocorrencia", "observacao")
        widgets = {
            'sintoma': forms.TextInput(attrs={'class': 'form-control'}),
            'intensidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Leve, Moderada, Muita dor'}),            
            'data_ocorrencia': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ConsultaMedicaForm(forms.ModelForm):
    class Meta:
        model = ConsultaMedica
        fields = ("titulo_exame_consulta", "data_hora", "local", "observacoes")
        widgets = {
            'titulo_exame_consulta': forms.TextInput(attrs={'class': 'form-control'}),
            'data_hora': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SinalVitalForm(forms.ModelForm):
    class Meta:
        model = SinalVital
        fields = ("tipo", "valor", "data_afericao")
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Pressão Arterial, Glicemia'}),
            'valor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 12x8, 98 mg/dL'}),
            'data_afericao': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
        }
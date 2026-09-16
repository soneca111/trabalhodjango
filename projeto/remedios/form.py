from django import forms
from remedios.models import Remedio

class RemedioForm(forms.ModelForm):
    class Meta:
        model = Remedio
        fields = ("nome","dosagem","quantidade","horario","observacoes")

        widgets = {
          'horario': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'type': 'time',
                }
            )
        }
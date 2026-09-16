from django.contrib import admin
from remedios.models import Remedio

# Register your models here.

class RemedioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dosagem', 'quantidade')  # Colunas exibidas na tabela
    search_fields = ('nome',)                        # Barra de pesquisa pelo nome
    list_filter = ('quantidade',)                    # Filtro lateral

admin.site.register(Remedio, RemedioAdmin)
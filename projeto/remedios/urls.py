from django.urls import path
from remedios.views import index, remedio_create, remedio_deletar,remedio_update
urlpatterns = [
    path('', index, name='remedio'),
    path('criar/', remedio_create, name='criar_remedio'),
    path('delete/<int:id>',remedio_deletar,name="remedio_delete"),
    path('alterar/<int:id>',remedio_update,name="remedio_alterar"),
    
]
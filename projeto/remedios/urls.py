from django.urls import path
from . import views

urlpatterns = [
    # 1. REMÉDIOS (Página Inicial / CRUD principal)
    path('', views.index, name='remedio'),
    path('criar/', views.remedio_create, name='criar_remedio'),
    path('delete/<int:id>', views.remedio_deletar, name='remedio_delete'),
    path('alterar/<int:id>', views.remedio_update, name='remedio_alterar'),

    # 2. ESTOQUE DE REMÉDIOS
    path('estoque/', views.estoque_list, name='estoque_list'),
    path('estoque/criar/', views.estoque_create, name='estoque_create'),
    path('estoque/alterar/<int:id>/', views.estoque_update, name='estoque_update'),
    path('estoque/deletar/<int:id>/', views.estoque_delete, name='estoque_delete'),

  
    # 3. REGISTRO DE SINTOMAS
    path('sintomas/', views.sintoma_list, name='sintoma_list'),
    path('sintomas/criar/', views.sintoma_create, name='sintoma_create'),
    path('sintomas/alterar/<int:id>/', views.sintoma_update, name='sintoma_update'),
    path('sintomas/deletar/<int:id>/', views.sintoma_delete, name='sintoma_delete'),

    # 4. CONSULTAS MÉDICAS
    path('consultas/', views.consulta_list, name='consulta_list'),
    path('consultas/criar/', views.consulta_create, name='consulta_create'),
    path('consultas/alterar/<int:id>/', views.consulta_update, name='consulta_update'),
    path('consultas/deletar/<int:id>/', views.consulta_delete, name='consulta_delete'),

  
    # 5. SINAIS VITAIS
    path('sinais-vitais/', views.sinal_vital_list, name='sinal_vital_list'),
    path('sinais-vitais/criar/', views.sinal_vital_create, name='sinal_vital_create'),
    path('sinais-vitais/alterar/<int:id>/', views.sinal_vital_update, name='sinal_vital_update'),
    path('sinais-vitais/deletar/<int:id>/', views.sinal_vital_delete, name='sinal_vital_delete'),
]
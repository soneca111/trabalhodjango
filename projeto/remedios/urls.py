from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='remedio'),
    path('criar/', views.RemedioCreateView.as_view(), name='criar_remedio'),
]
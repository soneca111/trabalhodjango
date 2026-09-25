from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', views.AccountCreateView.as_view(), name='signup'),

    path(
        'login/',
        LoginView.as_view(template_name='registro/login.html'),
        name='login',
    ),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('usuario/<int:pk>/desativar/', views.desativar_conta, name='desativar_conta'),

]
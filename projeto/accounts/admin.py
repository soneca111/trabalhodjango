
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser


class CustomerUserAdmin(UserAdmin):
    # Permite VER na tabela principal
    list_display = (
        'username',
        'email',
        'is_active'
    )


admin.site.register(CustomerUser, CustomerUserAdmin)
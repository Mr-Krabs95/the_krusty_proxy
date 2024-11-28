from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'id','is_staff', 'is_active', 'is_subscribed', 'is_superuser')
    list_filter = ('email', 'id', 'is_staff', 'is_active', 'is_subscribed', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': (
            'is_staff', 'is_active', 'is_subscribed', 
            'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff',
                'is_active', 'is_subscribed', 'is_superuser', 'groups', 
                'user_permissions'
            )}
        ),
    )
    search_fields = ('email', 'id',)
    ordering = ('id', 'email',)


admin.site.register(CustomUser, CustomUserAdmin)
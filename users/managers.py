from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """Свой менеджер пользователей."""
    def create_user(self, email, password, **extra_fields):
        """Создание обычного пользователя"""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создание суперпользователя"""
        extra_fields.setdefault('is_superuser', True) # Устанавливаем, чтобы пользователь был суперпользователем
        extra_fields.setdefault('is_staff', True) # Доступ к админке
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)
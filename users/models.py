from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Своя модель пользователя."""
    
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name= 'on/off профиль', 
        default=True,
        )
    is_staff = models.BooleanField(
        verbose_name=_("Доступ к админке"), 
        default=False # Доступ к админке
        ) 
    is_superuser = models.BooleanField(
        verbose_name=_('Статус суперполльзователя'), 
        default=False)
    is_subscribed = models.BooleanField(
        verbose_name=_('Статус подписки'),
        default=False # Активность подписки
        )

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    # Указываем менеджер, который будет работать с нашей моделью
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Дополнительные обязательные поля для создания суперпользователя

    def __str__(self):
        return self.email

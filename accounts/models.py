from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), max_length=128, unique=True, db_index=True)
    email = models.EmailField(_('Email Address'), unique=True, db_index=True)
    first_name = models.CharField(_('First Name'), max_length=128)
    last_name = models.CharField(_('Last Name'), max_length=128)
    is_verified = models.BooleanField(
        _('Verified Account'), default=False,
        help_text='Designates whether the user has verified the account.'
    )
    is_active = models.BooleanField(
        _('Account is Active'), default=True,
        help_text='Designates that the user account is not banned/suspended.'
    )
    is_admin = models.BooleanField(
        _('Admin Status'), default=False,
        help_text='Designates whether the user can log into sub-admin.'
    )
    is_staff = models.BooleanField(
        _('Staff Status'), default=False,
        help_text='Designates whether the user can log into admin area.'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        db_table = "accounts_users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'

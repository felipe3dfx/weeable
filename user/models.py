from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField

from app.storages import random_upload_path
from user.data import GENDER_CHOICES


class UserManager(BaseUserManager):
    """ Custom manager to create users and superusers
    """
    def create_user(self, email, password=None, is_active=True, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=UserManager.normalize_email(email),
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name=_('email'),
    )

    first_name = models.CharField(
        max_length=128,
        verbose_name=_('first names'),
    )

    last_name = models.CharField(
        max_length=128,
        verbose_name=_('last names'),
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('birth date'),
    )

    gender = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        choices=GENDER_CHOICES,
        verbose_name=_('gender'),
    )

    city = models.CharField(
        blank=True,
        max_length=128,
        verbose_name=_('city'),
    )

    country = CountryField()

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=random_upload_path,
        help_text=_('300x300 pixels as light as possible.'),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is active')
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Staff'),
        help_text=_('Indicates id can enter the site of administration.'),
    )

    date_joined = models.DateTimeField(
        default=now,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('last updated data'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = _('user')
        verbose_name_plural = _('users')

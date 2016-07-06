from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.timezone import now

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
            raise ValueError('Users must have an email address')

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
        verbose_name='Correo electrónico',
        help_text='''Ten en cuenta que al cambiar el correo electrónico tambien
        cambia la forma de ingresar a la plataforma.''',
    )

    first_name = models.CharField(
        max_length=128,
        verbose_name='Nombres',
    )

    last_name = models.CharField(
        max_length=128,
        verbose_name='Apellidos',
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento',
    )

    gender = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        choices=GENDER_CHOICES,
        verbose_name='Género',
    )

    city = models.CharField(
        blank=True,
        max_length=128,
        verbose_name='Ciudad',
    )

    country = CountryField()

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=random_upload_path,
        help_text='300x300 pixels as light as possible.',
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Es activo'
    )

    is_editor = models.BooleanField(
        default=False,
        verbose_name='Es editor'
    )

    is_admin = models.BooleanField(
        default=False,
        verbose_name='Es administrador'
    )

    date_joined = models.DateTimeField(
        default=now(),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de última actualización de datos',
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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

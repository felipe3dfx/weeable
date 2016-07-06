from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from registration.backends.hmac.views import RegistrationView

from user.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    actions = ['resend_activation_email']

    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
    )

    add_fieldsets = (
        (_('Información básica'), {
            'fields': (
                'first_name',
                'last_name',
            ),
        }),
        (_('Información de acceso'), {
            'fields': (
                'email',
                'password1',
                'password2',
            ),
        }),
    )

    fieldsets = (
        (_('Información de acceso'), {
            'fields': (
                'email',
                'password',
            ),
        }),
        (_('Información básica'), {
            'fields': (
                'first_name',
                'last_name',
            ),
        }),
        (_('Información personal'), {
            'fields': (
                'avatar',
                'gender',
                'birth_date',
                'city',
                'country',
            ),
        }),
        (_('Permisos'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
            ),
        }),
        (_('Fechas importantes'), {
            'fields': (
                'last_login',
                'date_joined',
                'updated_at',
            ),
        }),
    )

    ordering = ('first_name', 'last_name')

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super(CustomUserAdmin, self).get_readonly_fields(
            request, obj
        )
        return read_only_fields + ('last_login', 'date_joined', 'updated_at')

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return False

    def resend_activation_email(self, request, queryset):
        view = RegistrationView(request=request)
        for user in queryset:
            view.send_activation_email(user)

    resend_activation_email.short_description = 'Reenviar correo de activación'

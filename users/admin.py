from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
from users import models as um


# @admin.register(settings.AUTH_USER_MODEL)
@admin.register(um.User)
class UserExtendedAdmin(BaseUserAdmin):
    """Define admin model for custom User model with no email field."""
    # print(BaseUserAdmin.fieldsets)
    # fieldsets = BaseUserAdmin.fieldsets
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name')}),
        # ('Assing Roles', {'fields': ('roles',)}),  # adding roles
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'profile']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']


@admin.register(um.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in um.Profile._meta.get_fields()]



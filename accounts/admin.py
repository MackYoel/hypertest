from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import ugettext_lazy as _


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'fb_avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('pk', 'username', 'date_joined', 'is_staff', 'is_superuser')

    list_editable = ('username',)
    list_filter = ('username', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('pk', 'username')


admin.site.register(User, UserAdmin)

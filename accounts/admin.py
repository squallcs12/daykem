'''
Created on Apr 13, 2014

@author: antipro
'''
from awesome_avatar.fields import AvatarField
from awesome_avatar.widgets import AvatarWidget
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from accounts import models


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'display_name', 'email', 'avatar', 'homepage',
                       'gender', 'birthday')
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    formfield_overrides = {
        AvatarField: {'widget': AvatarWidget},
    }

admin.site.register(models.User, UserAdmin)
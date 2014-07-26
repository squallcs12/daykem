'''
Created on Sep 16, 2013

@author: antipro
'''
from django import forms

from accounts.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('username', 'user_permissions', 'groups', 'is_superuser', 'password', 'last_login',
                   'date_joined', 'is_active', 'is_staff', 'first_name', 'last_name', )


class UserSetupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('account_type', )
        widgets = {
            'account_type': forms.HiddenInput()
        }
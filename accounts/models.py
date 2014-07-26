from awesome_avatar.fields import AvatarField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _


class User(AbstractUser):
    GENDER_CHOICES = (
        (True, _('Male')),
        (False, _('Female')),
    )
    ACCOUNT_TYPE_CHOICES = {
        'TEACHER': _('Teacher'),
        'PARENT': _('Parent'),
    }

    display_name = models.CharField(max_length=255, blank=True, default='')
    avatar = AvatarField(upload_to='avatars', width=200, height=200)
    homepage = models.URLField(default='', blank=True)
    gender = models.BooleanField(default=True, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True, null=True, default=None)
    account_type = models.CharField(choices=ACCOUNT_TYPE_CHOICES.items(), max_length=20, null=True)

    def is_teacher(self):
        return self.account_type == 'TEACHER'

    def is_parent(self):
        return self.account_type == 'PARENT'
import re

from awesome_avatar.fields import AvatarField
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

GENDER_CHOICES = (
    (True, 'Male'),
    (False, 'Female'),
)


class User(AbstractUser):
    display_name = models.CharField(max_length=255, blank=True, default='')
    avatar = AvatarField(upload_to='avatars', width=200, height=200)
    homepage = models.URLField(default='', blank=True)
    gender = models.BooleanField(default=True, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True, null=True, default=None)

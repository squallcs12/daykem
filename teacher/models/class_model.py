"""
Created on 27/07/2014

@author: antipro
"""
__author__ = 'antipro'

from django.db import models
from django.utils.translation import ugettext as _


class Class(models.Model):

    CLASS_NUMBER_CHOICES = [(i, i) for i in range(1, 13)]
    DAYS_PER_WEEK_CHOICES = [(i, i) for i in range(1, 8)]
    HOURS_PER_DAY_CHOICES = [(i / 2.0, i / 2.0) for i in range(1, 9)]

    user = models.ForeignKey('accounts.User')
    class_number = models.IntegerField(_("Class"), choices=CLASS_NUMBER_CHOICES)
    hour_salary_minimum = models.FloatField()
    hour_salary_maximum = models.FloatField()
    days_per_week = models.IntegerField(choices=DAYS_PER_WEEK_CHOICES)
    hours_per_day = models.DecimalField(max_digits=2, decimal_places=1, choices=HOURS_PER_DAY_CHOICES)
    four_months_salary_minimum = models.FloatField()
    four_months_salary_maximum = models.FloatField()
    available = models.BooleanField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.four_months_salary_maximum = self.hour_salary_maximum * 4 * self.days_per_week * float(self.hours_per_day)
        self.four_months_salary_minimum = self.hour_salary_minimum * 4 * self.days_per_week * float(self.hours_per_day)
        super(Class, self).save(force_insert=force_insert,
                                force_update=force_update,
                                using=using,
                                update_fields=update_fields)

    class Meta:
        app_label = 'teacher'

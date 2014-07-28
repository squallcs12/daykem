"""
Created on 26/07/2014

@author: antipro
"""
__author__ = 'antipro'
from django import forms

from teacher import models


class ClassForm(forms.ModelForm):

    class Meta:
        model = models.Class
        exclude = ('user', 'four_months_salary_minimum', 'four_months_salary_maximum', )

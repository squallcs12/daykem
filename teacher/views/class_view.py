"""
Created on 27/07/2014

@author: antipro
"""
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from teacher import forms, models

__author__ = 'antipro'


class ClassView(View):

    template = 'teacher/class.html'
    extra_context = {}

    @method_decorator(login_required)
    def get(self, request):
        context = {
            'form': forms.ClassForm(),
        }
        context.update(self.extra_context)

        return TemplateResponse(request, self.template, context)

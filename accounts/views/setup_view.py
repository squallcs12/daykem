'''
Created on 26/07/2014

@author: antipro
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from accounts.forms import UserSetupForm

__author__ = 'antipro'


class SetupView(View):

    template = 'accounts/setup.html'
    extra_context = {}
    form = UserSetupForm

    def render(self):
        context = {
            'form': self.form()
        }
        context.update(self.extra_context)

        return TemplateResponse(self.request, self.template, context)

    @method_decorator(login_required)
    def get(self, request):
        return self.render()

    @method_decorator(login_required)
    def post(self, request):
        form = self.form(request.POST, instance=request.user)

        if not form.is_valid():
            return self.render()

        form.save()
        return redirect('accounts_profile')
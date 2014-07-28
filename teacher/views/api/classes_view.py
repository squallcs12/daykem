"""
Created on 27/07/2014

@author: antipro
"""
from common.rest_response import Response
from teacher.forms import ClassForm
from teacher.models.class_model import Class

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView


class ClassesView(APIView):

    extra_context = {}

    @method_decorator(login_required)
    def get(self, request):
        context = {
            'classes': request.user.class_set.all()
        }
        context.update(self.extra_context)

        return Response(context)

    @method_decorator(login_required)
    def post(self, request):
        instance = Class(user=request.user)
        form = ClassForm(request.DATA, instance=instance)
        if not form.is_valid():
            pass
        the_class = form.save()

        context = {
            'class': the_class,
        }
        return Response(context)

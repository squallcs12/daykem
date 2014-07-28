"""
Created on 26/07/2014

@author: antipro
"""
from teacher.views.class_view import ClassView

__author__ = 'antipro'
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^class/$', ClassView.as_view(), name='class'),
)

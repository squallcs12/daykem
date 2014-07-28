'''
Created on Sep 21, 2013

@author: antipro
'''
from django import template

register = template.Library()


@register.filter
def angular(form):
    for bound_field in form:
        if not 'ng-model' in bound_field.field.widget.attrs:
            bound_field.field.widget.attrs['ng-model'] = bound_field.name
    return form

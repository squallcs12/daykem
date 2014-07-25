'''
Created on Jul 29, 2013

@author: antipro
'''
from django import template
from django.contrib.auth import REDIRECT_FIELD_NAME

from common.django_custom import get_go_back_url

register = template.Library()


@register.tag
def back_url(_, token):
    try:
        args = token.split_contents()  # @UnusedVariable
        return BackUrlNode(*args)
    except ValueError:
        return BackUrlNode()


class BackUrlNode(template.Node):
    def __init__(self, default=None, prepend=None, redirect_field_name=REDIRECT_FIELD_NAME):
        self._prepend = prepend
        self._default = default
        self._redirect_field_name = redirect_field_name

    def render(self, context):
        request = context['request']
        back_href = get_go_back_url(request, self._redirect_field_name, self._default)

        if self._prepend == '0':
            return back_href
        return '' if not back_href else '?next=%s' % back_href


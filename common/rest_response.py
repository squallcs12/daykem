"""
Created on 28/07/2014

@author: antipro
"""
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import model_to_dict
from rest_framework.response import Response as OriginResponse


class Response(OriginResponse):

    def __init__(self, *args, **kwargs):
        data = kwargs['data'] if 'data' in kwargs else args[0]

        self.model_to_dict(data)
        # add success keyword
        success = kwargs.pop('success', 'errors' not in data)
        data['success'] = bool(success)

        super(Response, self).__init__(*args, **kwargs)

    def model_to_dict(self, data):
        if isinstance(data, dict):
            for key, value in data.iteritems():
                if isinstance(value, models.Model):
                    data[key] = model_to_dict(value)
                elif isinstance(value, QuerySet):
                    data[key] = [model_to_dict(o) for o in value]
                elif isinstance(value, (list, dict)):
                    self.model_to_dict(value)
        elif isinstance(data, list) and isinstance(data[0], models.Model):
            data = [model_to_dict(o) for o in data]
        return data

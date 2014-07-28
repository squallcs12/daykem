from django.conf.urls import patterns, url

from teacher.views.api.classes_view import ClassesView


urlpatterns = patterns(
    '',
    url(r'^classes/', ClassesView.as_view(), name='class'),
)

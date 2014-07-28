from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import api_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'common.views.home_view.main', name='homepage'),
    url(r'^/', include('common.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^api/', include(api_urls)),
    url(r'^parent/', include('parent.urls')),
    url(r'^teacher/', include('teacher.urls', namespace='teacher')),
)

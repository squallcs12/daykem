from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^teacher/', include('teacher.api_urls', namespace='teacher-api')),
)

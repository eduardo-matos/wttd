from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('eventex.core.views',
    url(r'^speaker/(?P<slug>[\w\-\_]+)', 'speaker_detail', name='speaker_detail'),
    url(r'^talk/(\d+)', 'talk_detail', name='talk_detail'),
    url(r'^talk-list/', 'talk_list', name='talk_list'),
    url(r'^$', 'homepage', name='homepage'),
)

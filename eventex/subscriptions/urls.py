from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('eventex.subscriptions.views',
    url(r'^$', 'inscricao', name='inscricao'),
    url(r'^(\d+)$', 'detail', name='detail'),
)

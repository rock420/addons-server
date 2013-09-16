from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url('^server.html$', views.commonplace, {'repo': 'fireplace'},
        name='commonplace.fireplace'),
    url('^comm/.*$', views.commonplace, {'repo': 'commbadge'},
        name='commonplace.commbadge'),
    url('^curation/.*$', views.commonplace, {'repo': 'rocketfuel'},
        name='commonplace.rocketfuel'),
    url('^stats/.*$', views.commonplace, {'repo': 'marketplace-stats'},
        name='commonplace.stats'),
)

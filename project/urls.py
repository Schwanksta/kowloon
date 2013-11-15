from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.static import serve as static_serve
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
admin.autodiscover()

from kowloon.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^getLayer/(?P<table>[-\w]+)/$', get_layer, name='get-layer'),
    url(r'^pointsInPolygon/(?P<poly_table>[-\w]+)/(?P<point_table>[-\w]+)/$', points_in_polygon, name='points-in-polygon'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True,
        }),
        url(r'^media/(?P<path>.*)$', 'serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )


if settings.PRODUCTION:
    urlpatterns += patterns('',
        url(r'^munin/(?P<path>.*)$', staff_member_required(static_serve), {
            'document_root': settings.MUNIN_ROOT,
        })
   )

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'', 'education.contrib.page.views.home'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    (r''),
    # (r'^app/(?P<slug>[^\.^/]+)/$', view=,  name='product.view.view'),
)

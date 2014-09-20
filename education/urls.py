from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^products/(?P<id>.*)$', 'education.contrib.product.views.view'),
    (r'^game/(?P<slug>.*)$', 'education.contrib.review.views.view'),
    (r'^website/(?P<slug>.*)$', 'education.contrib.review.views.view'),
    (r'^app/(?P<slug>.*)$', 'education.contrib.review.views.view'),
    (r'^users/(?P<slug>.*)$', 'education.contrib.user.views.view'),
    (r'', 'education.contrib.page.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    (r''),
    # (r'^app/(?P<slug>[^\.^/]+)/$', view=,  name='product.view.view'),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
import egg

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pou.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^egg/', include('egg.urls')),
)

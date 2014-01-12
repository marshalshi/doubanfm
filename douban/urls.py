from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from fm.views import test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'douban.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', test, name="test"),
)

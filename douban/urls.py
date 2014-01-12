from django.conf.urls import patterns, include, url

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from fm.views import test, get_play_list

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'douban.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', test, name="test"),
    url(r'^test/json/$', get_play_list, name="list"),
)

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS}),
                        )

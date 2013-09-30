from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'pages.views.home', name='home'),
    #url(r'^about/$', 'pages.views.about', name='About'),
    # url(r'^challenge/$', 'pages.views.tbd', name='Challenge'),
    # url(r'^downloads/$', 'pages.views.tbd', name='Downloads'),
    # url(r'^keynote/$', 'pages.views.tbd', name='Keynotes'),
    # url(r'^program/$', 'pages.views.tbd', name='Program'),
    # url(r'^tutorial/$', 'pages.views.tbd', name='Tutorial'),
    url(r'^cfp/$', 'pages.views.cfp', name='Proposals'),
    url(r'^committee/$', 'pages.views.committee', name='committee'),
    # url(r'^about/$', 'pages.views.about'),
    url(r'^(?P<page>.+)/$', 'pages.views.tbd'),
    # url(r'^sbp2014/', include('sbp2014.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),



)

urlpatterns += staticfiles_urlpatterns()

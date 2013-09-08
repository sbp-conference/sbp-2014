from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^about/$', 'pages.views.home', name='home'),
    url(r'^challenge/$', 'pages.views.home', name='home'),
    url(r'^downloads/$', 'pages.views.home', name='home'),
    url(r'^keynote/$', 'pages.views.home', name='home'),
    url(r'^program/$', 'pages.views.home', name='home'),
    url(r'^tutorial/$', 'pages.views.home', name='home'),
    # url(r'^sbp2014/', include('sbp2014.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()

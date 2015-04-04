from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Expence.views.home', name='home'),
     url(r'^expence/', include('Expanceapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

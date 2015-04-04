from django.conf.urls import patterns, include, url
from django.utils import timezone
import datetime
from models import Expence
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Expanceapp.views.index', name='home'),
    #url(r'(?P<pk>\d+)/^$', 'Expence.views.month', name='month'),
     #url(r'/one^$', 'Expence.views.home', name='home'),

)

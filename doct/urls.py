from django.conf.urls import patterns, include, url
from django.contrib import admin
from doct.app import views

urlpatterns = patterns('',
    url(r'^$', 'doct.app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^task/$', views.new_task, name='new_task'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.update_task, name='update_task'),
    url(r'^list/$', views.list_task, name='list_task'),
    url(r'^contribute/(?P<pk>[0-9]+)/$', views.contribute_task, name='contribute_task'),
)

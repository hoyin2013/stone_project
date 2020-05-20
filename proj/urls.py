#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','sannet.views.login',name='login'),
    url(r'^login/$','sannet.views.login',name='login'),
    url(r'^index/$','sannet.views.index',name='index'),
    url(r'^logout/$','sannet.views.logout',name='logout'),
    url(r'^proj_detail/(\d+)$','sannet.views.proj_detail',name='proj_detail'),
    url(r'^project_device/(\d+)$','sannet.views.project_device',name='project_device'),
    url(r'^device_list/$','sannet.views.device_list',name='device_list'),
    url(r'^device_detail/(\d+)$','sannet.views.device_detail',name='device_detail'),

   
)

#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()




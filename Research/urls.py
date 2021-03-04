from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Article, name="Article"),
    url(r'^admin/$', views.admin),
    url(r'^manage/$', views.manage, name="manage"),
    url(r'project/(?P<id>\d)/$', views.projectContent, name="content"),
    url(r'(?P<id>\d)/$', views.articleContent, name="content"),
]

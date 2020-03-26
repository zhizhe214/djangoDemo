
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^hello_url/$', views.hello_views),
    url(r'msg_url/(?P<name>\w+)/(?P<age>\d+)/(?P<height9>\d+)/$', views.msg_views),
    url(r'add_url/(?P<name>\w+)/(?P<address>\w+)/$', views.show_views),
]
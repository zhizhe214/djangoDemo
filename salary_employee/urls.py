from django.conf.urls import url
from . import views
urlpatterns = [
    # app 工资统计
    url(r'wage_url/(?P<name>\w+)/(?P<wage>\d+)/$', views.wage_statistics_views),
]


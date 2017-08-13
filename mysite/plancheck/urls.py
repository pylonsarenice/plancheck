from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view_plans/$', views.view_plans, name='view_plans')
]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clear/$', views.clear),
    url(r'^submit/(?P<survey_id>[0-9]+)/$', views.submit),
]

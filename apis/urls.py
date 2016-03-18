from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^models$', views.getAll, name='getAll'),
    url(r'^models/(?P<pk>(.)+)$', views.getOne, name='getOne'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


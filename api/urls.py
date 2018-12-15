from django.contrib import admin
from api.views import *
from django.conf.urls import include, url

urlpatterns=[
    url('test',test),
    url('mnist',mnist)
]
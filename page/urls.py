from django.contrib import admin
from page.views import *
from django.conf.urls import include, url

urlpatterns=[
    url('test',test,name='test'),
    url('login',login,name='login'),
    url('question',question,name='question'),
    url('rank',rank,name='rank'),
    url('mnist',mnist,name='mnist'),
    url('model',model,name='model'),
    url('elements',model,name='elements')
]
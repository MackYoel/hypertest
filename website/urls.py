from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^(?P<duel_token>[\w\.-]+)$', views.duel, name='duel'),
    url(r'^(?P<duel_token>[\w\.-]+)/$', views.duel, name='duel'),
]

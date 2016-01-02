from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^signin', views.signin, name='signin'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^game', views.game, name='game'),
]
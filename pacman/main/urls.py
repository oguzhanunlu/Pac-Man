from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^signin', views.signin, name='signin'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^game/$', views.game, name='game'),
    url(r'^game/?dir=r/$', views.game, name='game'),
    url(r'^game/?dir=l/$', views.game, name='game'),
    url(r'^game/?dir=u/$', views.game, name='game'),
    url(r'^game/?dir=d/$', views.game, name='game'),
    url(r'^quit', views.qquit, name='quit'),
]
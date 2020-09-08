from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views


urlpatterns = [

    url(r'^$', views.representatives, name='representatives'),
    url(r'^accepted', views.accepted, name='accepted'),
    url(r'^Already', views.representatives, name='already'),

        ]
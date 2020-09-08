from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'crypto'
urlpatterns = [

    url(r'$^', views.cryptohome.as_view(), name="wat"),
    url(r'sell', views.CryptoSell.as_view(), name="sell")

]
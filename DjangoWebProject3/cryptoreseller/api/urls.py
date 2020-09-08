from django.conf.urls import url
from .views import Crypthome

urlpatterns = [
    url(r'^$', Crypthome.as_view(), name='homesjuitcreate'),
    # url(r'^(?P<pk>\d+)/$', AttendancePostView.as_view(), name='homesjuit'),

]
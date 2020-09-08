"""
Definition of urls for DjangoWebProject3.
"""
from django.contrib.auth.views import ( 
    password_reset, 
    password_reset_done, 
    password_reset_confirm,
    password_reset_complete
    )


from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^representatives/', include('representatives.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^market/', include('market.urls')),
    url(r'^cryptoreseller/', include('cryptoreseller.urls')),
    url(r'^api/cryptoreseller/', include('cryptoreseller.api.urls', namespace='api-crypto')),
    url(r'^payments/', include('django_pesapal.urls')),
    #url(r'^register/$', register),
    url(r'^password-reset/$', password_reset),
    url(r'^password-reset/done/$',password_reset_done),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$',password_reset_complete),
    # url(r'^$', include('app.urls')),
    # url(r'^DjangoWebProject3/', include('DjangoWebProject3.DjangoWebProject3.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header ="XumpesA"
admin.site.index_title = "XumpesA"
#if settings.DEBUG:
   # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
PESAPAL_DEMO = True
PESAPAL_OAUTH_CALLBACK_URL = 'transaction_completed'
PESAPAL_OAUTH_SIGNATURE_METHOD = 'SignatureMethod_HMAC_SHA1'
PESAPAL_TRANSACTION_DEFAULT_REDIRECT_URL = 'payment'
PESAPAL_DEMO = True
PESAPAL_OAUTH_CALLBACK_URL = 'transaction_completed'
PESAPAL_OAUTH_SIGNATURE_METHOD = 'SignatureMethod_HMAC_SHA1'
PESAPAL_TRANSACTION_FAILED_REDIRECT_URL = ''
PESAPAL_ITEM_DESCRIPTION = False
PESAPAL_TRANSACTION_MODEL = 'django_pesapal.Transaction'

PESAPAL_TRANSACTION_DEFAULT_REDIRECT_URL = 'app:deposit'  # this needs to be a reversible



# Override pesapal keys

try:
    from local_config import *
except ImportError:
    pass
from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'market'
urlpatterns = [

    url(r'^$', login_required(views.registerproduct), name ='register'),
    url(r'^Confirmation', login_required(views.ConfirmationView.as_view()), name='Confirmation'),
    url(r'^Conditions', login_required(views.MarketConditionsView.as_view()), name='Conditions'),
    url(r'^Processors', login_required(views.ProcessorsView.as_view()), name='Processors'),
    url(r'^Processor', login_required(views.Processors_listView.as_view()), name='processors_list'),





    url(r'^Myproducts', login_required(views.MyProducts.as_view()), name='myproducts'),
    # url(r'^(?P<pk>[0-9]+)/ProductsDetails$', views.MyProductDetails.as_view(), name='ProductsDetails'),



    url(r'^api/', views.MarketView.as_view(), name = 'ApiMarket'),
    url(r'^Mpesa/', login_required(views.MpesaView.as_view()), name = 'mpesa'),

    url(r'^Paymethod', login_required(views.PayMethodView.as_view()), name='Paymethod'),


    url(r'^Crediting', login_required(views.creditcardview), name='Crediting'),



    url(r'^Newdeals', login_required(views.NewDealsView.as_view()), name='Newdeals'),



    url(r'^product/add/$', login_required(views.productcreate), name='upload-add'),
    url(r'^Orders/(?P<pk>[0-9]+)/$', login_required(views.Orderdetails.as_view()), name='orderdetails'),

    url(r'^category', login_required(views.albumcreate), name='category'),
    url(r'^customer-Orders', login_required(views.CustomerOrders.as_view()), name='customers'),
    url(r'^customer-Orders-Details', login_required(views.CustomerOrdersDetails.as_view()), name='customerorderdetails'),

    url(r'^product/(?P<pk>[0-9]+)/$', login_required(views.ProductUpdate.as_view()), name='upload-update'),
    url(r'^product/PaidProductedit/(?P<pk>[0-9]+)/$', login_required(views.PaidProductedit.as_view()), name='PaidProducteditdetail'),
    url(r'^product/paidproductedit/(?P<pk>[0-9]+)/$', login_required(views.MyProductPaiddetails.as_view()), name='Myproductspaidedit'),

    # url(r'^product/(?P<pk>[0-9]+)/delete/$', login_required(views.ProductDelete.as_view()), name='upload-delete'),
    url(r'^product/(?P<pk>[0-9]+)$', login_required(views.ProductDelete.as_view()), name='upload-delete'),

    url(r'^Orders/new/(?P<pk>[0-9]+)$', login_required(views.OrderReturn.as_view()), name='orderreturn'),
    url(r'^Orders/Paidproductdelete/(?P<pk>[0-9]+)$', login_required(views.PaidProductdelete.as_view()), name='paiddelete'),
    url(r'^Orders/new/remove/(?P<pk>[0-9]+)$', login_required(views.Ordercomplete.as_view()), name='complete'),


    # url(r'^Productslist/$', views.MarketingkwListView.as_view(), name='marketing'),
    url(r'^Main-market/$', views.MarketingListView.as_view(), name='main-market'),
    url(r'^Productslist/(?P<pk>[0-9]+)$', views.MarketingDetailsView.as_view(), name='marketingdetails'),
    url(r'^(?P<pk>[0-9]+)/Prods$', login_required(views.ProdsDetails.as_view()), name='Prods'),
    # url(r'^Completes/(?P<pk>[0-9]+)/$', login_required(views.ReceiveForme.as_view()), name='ReceivForm'),




    url(r'^Completes/(?P<pk>[0-9]+)$', login_required(views.Finnished.as_view()), name='Finnish'),
    url(r'^Customerdismiss/(?P<pk>[0-9]+)$', login_required(views.CustomertDismiss.as_view()), name='Change'),
    url(r'^SentbysellerDismiss/(?P<pk>[0-9]+)$', login_required(views.SentbysellerDismiss.as_view()), name='Away'),



    url(r'^Cart/(?P<pk>[0-9]+)$', login_required(views.Caret.as_view()), name='cart'),
    url(r'^Cart/delete/(?P<pk>[0-9]+)$', login_required(views.Cartdelete.as_view()), name='caritdelete'),
    url(r'^Cart/$', login_required(views.Cartlist.as_view()), name='cartlist'),
    # url(r'^test/$', login_required(views.Cart.as_view()), name='test'),
    url(r'^Form/$', login_required(views.ProdsForm.as_view()), name='ProdsForm'),


    url(r'^promo_products', login_required(views.Promo.as_view()), name='promo'),
    url(r'^Priced', login_required(views.PriceProducts.as_view()), name='PaidProducts'),


    # url(r'^(?P<pk>[0-9]+)/$', views.PromoDetails.as_view(), name='details'),
    # url(r'^purchase', views.purchase, name='purchase')
    # market/upload/2/delete/

     url(r'^product/(?P<pk>[0-9]+)/Edit/$', login_required(views.Productedit.as_view()), name='product-edit'),
     url(r'^premium/(?P<pk>[0-9]+)/$', login_required(views.PriceProductdetails.as_view()), name='pricedetails'),
     url(r'^wish/(?P<pk>[0-9]+)/confirm/$', login_required(views.Receiveupdate.as_view()), name='receiveconfirm'),

    # url(r'^(?P<pk>[0-9]+)/Secured', views.BuyingView.as_view(), name='secured'),

    url(r'^Search', login_required(views.SearchView.as_view()), name='Search'),
    url(r'^Orders/', login_required(views.OrdersList.as_view()), name='orders'),

        ]


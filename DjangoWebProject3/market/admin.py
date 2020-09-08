from django.contrib import admin

from market.models import Products, Album, Purchases, CreditCard, Mpesa, Cart, FinishedTransactions, Prepurchase, PaidProducts, ReturnedPurchases


def received (Modeladmin, request, queryset):
    queryset.update(status='Received')


def canceled(modeladmin, request, queryset):
    queryset.update(status='Canceled')

def not_received(modeladmin, request, queryset):
    queryset.update(status='Not received')
not_received.short_description = "Was not received"




class AlbumAdmin(admin.ModelAdmin):
    list_display = ["user", "Full_name", "country", "currently_location"]


class CreditCardAdmin(admin.ModelAdmin):
    list_display = ["username", "products", "Card_holder_name", "Card_number", "Passport_id",
                    "Expirity_month", "Expirity_year", "Security_code_CVV"]


class PurchasesAdmin(admin.ModelAdmin):
    list_display = ["userid", "user", "product_id", "shortcode", "product_title", "product_owner", "name_of_receiver", "quantity", "currency_used",
                    "country", "Region", "Price_sold", "Price", "Street", "processor", "phone_no", "Receive_acc", "buyers_acc", "orderdate", "lastdate", "complete", "status", "customers_status", "sellers_status"]
    actions = [received, canceled, not_received]


class ReturnedPurchasesAdmin(admin.ModelAdmin):
    list_display = ["userid", "sellers_name", "product_id", "shortcode", "product_title", "product_owner", "buyers_name", "quantity",
                    "country", "Region", "Price_sold", "Price", "Street", "processor", "phone_no", "Receive_acc", "orderdate", "status", "customers_status", "sellers_status"]


class PrePurchaseAdmin(admin.ModelAdmin):
    list_display = ["userid", "user", "product_id", "product_title", "product_owner", "purchase_id", "name_of_receiver", "quantity",
                    "country", "Region", "shortcode", "Price_sold", "Price", "Street","processor", "phone_no", "Receive_acc", "orderdate", "lastdate", "status"]


class FinishedTransAdmin(admin.ModelAdmin):
    list_display = ["userid", "user", "purchase_id",  "name_of_receiver", "currency", "country", "Receive_acc",
                    "product_id", "product_title", "Region", "Price_sold" ,"processor", "Street" , "phone_no", "quantity", "product_owner",
                    "Price_sold", "Price" , "status"]
#
# class FinishedTransAdmin(admin.ModelAdmin):
#     list_display = ["userid", "user", "product_id", "product_title", "product_owner", "name_of_receiver", "quantity", "date_of_delivery",
#                     "country", "Region", "Price_sold", "Price", "Street","processor", "phone_no", "Receive_acc", "orderdate", "lastdate", "status"]


class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "stock_products", "image", "image1", "category", "timestamp", "title", "Price",
                    "Price_sold", "Receive_acc", "condition", "currency_used"]


class PaidProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "stock_products", "Youremail", "Phone_numbers", "image", "image1", "category", "timestamp", "title", "Price",
                    "Price_sold", "Receive_acc", "AdsPackage", "condition"]


class CartAdmin(admin.ModelAdmin):
    list_display = ["username", "image", "image1", "category", "title", "Price",
                    "Price_sold", "Receive_acc", "condition"]


class MpesaAdmin(admin.ModelAdmin):
    list_display = ["username", "Account_balance", "mpesa_Name", "phone_no", "amount_sent",
                    "order_date", "kumbukumbu_no", "Admin_kumbukumbu_no", "order_no"]


admin.site.register(Products, ProductsAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Purchases, PurchasesAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(Mpesa, MpesaAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(FinishedTransactions, FinishedTransAdmin)
admin.site.register(Prepurchase, PrePurchaseAdmin)
admin.site.register(PaidProducts, PaidProductsAdmin)
admin.site.register(ReturnedPurchases, ReturnedPurchasesAdmin)










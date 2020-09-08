from .forms import *
from PIL import Image, ImageFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from .models import *
from .mixins import *
from rest_framework.views import APIView
import schedule
from rest_framework import status
from django.core.paginator import Paginator
from braces.views import FormMessagesMixin
from django.utils.translation import ugettext_lazy as _
import datetime
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden
import operator
from django.http import HttpResponse
from functools import reduce
from rest_framework.response import Response
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib import messages
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, FormMixin, UpdateView, ModelFormMixin
from django.views.generic import DetailView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import MarketSerializers
from .models import *

class Promo(generic.ListView):
    template_name = 'promo_products.html'

    def get_queryset(self):
        return Products.objects.filter(user=self.request.user)

#
# class MarketingkwListView(generic.ListView):
#     model = Products
#     template_name = 'home_main.html'
#
#     def get_queryset(self):
#         return Products.objects.all()



class MarketingListView(generic.ListView):
    model = Products
    template_name = 'home_list.html'

    def get_queryset(self):
        return Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MarketingListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['Priced'] = PaidProducts.objects.all()
        context['object_list'] = Products.objects.all()
        return context
    # def get_context_data(self, **kwargs):
    #     context = super(MarketingkwListView, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     context['all'] = Products.objects.all()
    #     return context


class MarketingDetailsView(generic.DetailView):
    model = Products
    template_name = 'home_maindetails.html'

    # def get_queryset(self):
    #     return Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MarketingDetailsView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        # cout = UserInfo.objects.get(user=self.request.user.pk)
        # watre = cout.full_name
        context['Mvuno'] = Products.objects.all()[:4]
        # coutm = UserInfo.objects.get(user=self.request.user.pk)
        # watrem = coutm.user
        # context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        return context


class MyProducts(generic.ListView):
    model = Products
    template_name = 'My_products.html'

    def get_queryset(self):
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        return Products.objects.filter(username=watre)

    def get_context_data(self, **kwargs):
        context = super(MyProducts, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre).exclude(order_actions=Cancelled).exclude(complete='completed')
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['Priced'] = PaidProducts.objects.filter(username=watrem)
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled).exclude(complete='completed')
        return context


# class MyProductDetails(generic.DetailView):
#     template_name = 'My_products.html'


class PromoDetails(generic.DetailView):
    model = Products
    template_name = 'PromoDetails.html'







    def get_context_data(self, **kwargs):
        context = super(PromoDetails, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(PromoDetails, self).get_context_data(**kwargs)
    #     context['form'] = BuyingForm
    #     return  context


# class RegisterProduct(generic.ListView):
#     template_name = 'register_products.html'
#
#     def get_queryset(self):
#         return Products.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super(RegisterProduct, self).get_context_data(**kwargs)
#         context['user'] = self.request.user
#         return context
@login_required(login_url='/login/')
def registerproduct(request):
    Furnitures = Products.objects.filter(category__icontains="Furniture's")[:1]
    Furnitures = Products.objects.filter(category__icontains="Furniture's")[:1]
    clothing = Products.objects.filter(category__icontains="Clothing")[:1]
    improvements = Products.objects.filter(category__icontains="Home improvement")[:1]
    others = Products.objects.filter(category__icontains="others")[:1]
    sports = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
    jewelry = Products.objects.filter(category__icontains="jewelry & watches")[:1]
    hair = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
    office = Products.objects.filter(category__icontains="office & school supplys")[:1]
    computers = Products.objects.filter(category__icontains="Computers & office")[:1]
    health = Products.objects.filter(category__icontains="Health & Beauty")[:1]
    phones = Products.objects.filter(category__icontains="Phones & accessories")[:1]
    homegarden = Products.objects.filter(category__icontains="Home & garden")[:1]
    clotheswomen = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
    clothesmen = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
    bags = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
    toys = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
    wedding = Products.objects.filter(category__icontains="Wedding & events")[:1]
    automobiles = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
    lights = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
    security = Products.objects.filter(category__icontains="Security & protection")[:1]
    electronics = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
    Furnitures = Products.objects.filter(category__icontains="Furniture's")[:1]
    coutm = UserInfo.objects.get(user=request.user.pk)
    watrem = coutm.user
    queryse = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
    cout = UserInfo.objects.get(user=request.user.pk)
    watre = cout.full_name
    Mavuno = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)
    Priced = PaidProducts.objects.all()



    queryset_list = Products.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Products.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(username__icontains=query) |
            Q(Price__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 30)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "clothing":clothing,
        "electronics":electronics,
        "security":security,
        "lights":lights,
        "Priced":Priced,
        "automobiles":automobiles,
        "wedding":wedding,
        "toys":toys,
        "bags":bags,
        "clothesmen":clothesmen,
        "clotheswomen":clotheswomen,
        "homegarden":homegarden,
        "phones":phones,
        "health":health,
        "computers":computers,
        "office":office,
        "hair":hair,
        "jewelry":jewelry,
        "sports":sports,
        "others":others,
        "improvements":improvements,
        "Furnitures":Furnitures,
        "object_list": queryset,
        "queryset": queryse,
        "Mavuno": Mavuno,
        "title": "List",
        "page_request_var": page_request_var

    }

    return render(request, 'register_products.html', context)


class RegisterProductsDetails(generic.DetailView):
    model = Products
    template_name = 'PromoDetails.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterProductsDetails, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PayMethodView(generic.TemplateView):
    model = Products
    template_name = 'paymentmethod.html'

    def get_context_data(self, **kwargs):
        context = super(PayMethodView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre)
        return context


class NewDealsView(generic.ListView):
    template_name = 'Newdeals.html'

    def get_queryset(self):
        return Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NewDealsView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        return context
# def register_products(request):
#     query = Products.objects.all()
#     paginator = Paginator(query, 12)  # Show 25 contacts per page
#     page = request.GET.get('page')
#     try:
#         product = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         product = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         product = paginator.page(paginator.num_pages)
#     context = {
#         "query": product
#     }
#     return render(request, 'register_products.html', context)


# class ProductCreate(generic.CreateView):
#     model = Products
#     template_name = 'upload_products.html'
#     form_class = ProductsForm
#     success_url = reverse_lazy("market:register")
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductCreate, self).get_context_data(**kwargs)
#         context['user'] = self.request.user
#         return context
#
#     def form_valid(self, form):
#         cout = UserInfo.objects.get(user=self.request.user.pk)
#         watre = cout.full_name
#         coutre = Products.objects.get(username=watre)
#         coutre.Price_sold = coutre.Price * 2
#         return coutre.save()


class Productedit(DetailView):
    model = Products
    template_name = 'Myproductedit.html'
    success_url = reverse_lazy('market:register')

    def get_context_data(self, **kwargs):
        context = super(Productedit, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
        return context


class ProductUpdate(UpdateView):
    template_name = 'upload_products.html'
    model = Products
    form_class = ProductsForm

    def get_context_data(self, **kwargs):
        context = super(ProductUpdate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
        return context




class ProductDelete(DeleteView):
    model = Products
    success_url = reverse_lazy('market:register')
#
#     # form_class = AlbumForm
#     success_url = reverse_lazy('market:upload-add')
#     fields = [
#         'categories',
#
# ]

    # def get_context_data(self, **kwargs):
    #     context = super(AlbumCreate, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     return context

# class UserCreate(generic.CreateView):
#     model = Userz
#     template_name = 'User.html'
#     # success_url = reverse_lazy('market:upload-add')
#     fields = [
#         'Full_name',
#
#     ]

def albumcreate(request):
    Furnitures = Products.objects.filter(category__icontains="Furniture's")[:1]
    Furnitures = Products.objects.filter(category__icontains="Furniture's")[:1]
    clothing = Products.objects.filter(category__icontains="Clothing")[:1]
    improvements = Products.objects.filter(category__icontains="Home improvement")[:1]
    others = Products.objects.filter(category__icontains="others")[:1]
    sports = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
    jewelry = Products.objects.filter(category__icontains="jewelry & watches")[:1]
    hair = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
    office = Products.objects.filter(category__icontains="office & school supplys")[:1]
    computers = Products.objects.filter(category__icontains="Computers & office")[:1]
    health = Products.objects.filter(category__icontains="Health & Beauty")[:1]
    phones = Products.objects.filter(category__icontains="Phones & accessories")[:1]
    homegarden = Products.objects.filter(category__icontains="Home & garden")[:1]
    clotheswomen = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
    clothesmen = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
    bags = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
    toys = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
    wedding = Products.objects.filter(category__icontains="Wedding & events")[:1]
    automobiles = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
    lights = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
    security = Products.objects.filter(category__icontains="Security & protection")[:1]
    electronics = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
    Furnitures = Products.objects.filter(category__icontains="Furniture's")[:1]
    coutm = UserInfo.objects.get(user=request.user.pk)
    watrem = coutm.user
    queryse= Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)

    cout = UserInfo.objects.get(user=request.user.pk)
    watre = cout.full_name
    Mavuno = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)

    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    # cont, created = Products.objects.get_or_create(category=request.user)
    # instance, crete = Album.objects.get_or_create(user=request.user)
    # form = AlbumForm(request.POST or None,)
    context = {
        "clothing": clothing,
        "electronics": electronics,
        "security": security,
        "lights": lights,
        "automobiles": automobiles,
        "wedding": wedding,
        "toys": toys,
        "bags": bags,
        "clothesmen": clothesmen,
        "clotheswomen": clotheswomen,
        "homegarden": homegarden,
        "phones": phones,
        "health": health,
        "computers": computers,
        "office": office,
        "hair": hair,
        "jewelry": jewelry,
        "sports": sports,
        "others": others,
        "improvements": improvements,
        "Furnitures": Furnitures,

        "title": title.title(),
        "queryset": queryse,
        "Mavuno": Mavuno
        }
    # if form.is_valid():
    #     user = form.save(commit=False)
    #     user.save()
    #     # cont.album = instance.Full_name
    #     # cont.save()
    #     return redirect(reverse('market:upload-add'))
    return render(request, 'category.html', context)


@login_required(login_url='/login/')
def productcreate(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    # cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    form = ProductsForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)
        user.Price_sold = user.Price * 20/100 + user.Price

        # im = Image.open(user.image)
        # imag = im.filter(ImageFilter.BLUR)
        #
        # imag.save()
        user.save()
        return redirect(reverse('market:register'))
    return render(request, 'upload_products.html', context)


class ProcessorsView(generic.TemplateView):
    template_name = 'processors.html'
    # success_url = reverse_lazy('market:upload-add')
    #
class MpesaView(generic.CreateView):
    model = Mpesa
    template_name = 'Mpesa.html'
    form_class = MpesaForm
    success_url = reverse_lazy('market:register')

    def get_queryset(self):
        return Mpesa.objects.all()


class Processors_listView(generic.TemplateView):
    template_name = 'processors_list.html'
    success_url = reverse_lazy('market:Crediting')

    def get_context_data(self, **kwargs):
        context = super(Processors_listView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        return context
    #


class BuyingView(generic.CreateView):
    template_name = 'buy.html'
    model = Purchases
    form_class = BuyingForm
    success_url = reverse_lazy('market:processors_list')
    context_object_name = "queryset"
    walte = Products.objects.all()


    def get_context_data(self, **kwargs):
        context = super(BuyingView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        context['Prods'] = Products.objects.all()
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        return context



# class CreditCardView(generic.FormView):
#     model = CreditCard
#     template_name = "CreditCard.html"
#     form_class = CreditCardForm
#     success_url = reverse_lazy('market:upload-add')

def creditcardview(request):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" % request.user
    # cout = Userz.objects.get(user=request.user.pk)

    # instance = Products.objects.get(album=request.user.pk)
    form = CreditCardForm(request.POST or None, request.FILES or None, )
    context = {
        "title": title.title(),
        "form": form
    }
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return redirect(reverse('market:register'))
    return render(request, 'CreditCard.html', context)


        # def dispatch(self, request, *args, **kwargs):
    #     return super(BuyingView, self).dispatch(args, **kwargs)

    # def form_invalid(self, form):
    #     obj = form.save(commit=False)
    #     obj.created_by = self.request.user
    #     obj.save()
    #     return http.HttpResponseRedirect(self.get_success_url())
# success_url = reverse_lazy('market:upload-add')




class MarketConditionsView(generic.TemplateView):
    template_name = 'market-conditions.html'
    # success_url = reverse_lazy('market:upload-add')


    def get_context_data(self, **kwargs):
        context = super(MarketConditionsView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)

        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
        return context


class ConfirmationView(generic.TemplateView):
    template_name = 'confirmation.html'
    # success_url = reverse_lazy('market:upload-add')


class SearchView(generic.ListView):
    template_name = 'Searchlist.html'
    model = Products

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(Price__icontains=q) for q in query_list))
            )

        return result


class MarketView(APIView):
    def get(self, request):
        # users = UserInfo.objects.get(user=request.user.pk)
        info = Products.objects.all()
        serializer = MarketSerializers(info, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = MarketSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    #
    # class ApiView(APIView):
    #     def get(self, request):
    #         info = UserInfo.objects.all()
    #         serializer = AppSerializers(info, many=True)
    #         return Response(serializer.data)




# def album(request):
#     title = 'New product'
#     if request.user.is_authenticated:
#         title = "Welcome %s, Enter information about your product you want to sell" % request.user
#     instance = Album.objects.get(user=request.user.pk)
#     form = AlbumForm(request.POST or None, instance=instance)
#     context = {
#         "title": title,
#         "form": form,
#         "button": send,
#         # "queryset": queryset
#     }
#     if form.is_valid():
#         content = form.save(commit=False)
#         content.save()
#         return redirect(upload_products)
#     return render(request, 'category.html', context)
#
# send = "Send"

#
# def upload_products(request):
#     title = 'New product'
#     if request.user.is_authenticated:
#         title = "Welcome %s, Enter information about your product you want to sell" % request.user
#
#     #instance = Products.objects.get(album=request.user.pk)
#     form = ProductsForm(request.POST or None, request.FILES or None)
#     context = {
#         "title": title,
#         "form": form,
#         "button": send,
#         # "queryset": queryset
#     }
#     if form.is_valid():
#         user = form.save(commit=False)
#         #instance.save()
#         user.save()
#         messages.success(request, 'upload success')
#     return render(request, 'upload_products.html', context)


# def purchase(request):
#     queryset = Products.objects.all()
#     title = 'New product'
#     if request.user.is_authenticated:
#         title = "Welcome %s, Enter your information" % request.user
#     # instance = Products.objects.get(album=request.user.pk)
#     form = PurchasesForm(request.POST or None, request.FILES or None)
#     context = {
#         "title": title,
#         "button": send,
#         "form": form,
#
#         "queryset": queryset
#     }
#     if form.is_valid():
#         user = form.save(commit=False)
#         # instance.save()
#         user.save()
#         messages.success(request, 'upload success')
#     return render(request, 'purchase.html', context)


# def promo(request):
#     queryset = Products.objects.all()
#     paginator = Paginator(queryset, 12)  # Show 25 contacts per page
#     page = request.GET.get('page')
#     try:
#         product = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         product = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         product = paginator.page(paginator.num_pages)
#     context = {
#         "queryset": product
#     }
#     return render(request, 'promo_products.html', context
@login_required(login_url='/login/')
def search (request):
    queryset_list =Products.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list= Products.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(username__icontains=query) |
            Q(Price__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var

    }

    return render(request, 'searched.html', context)





class ProdsDetails(DetailView):
    model = Products
    # form_class = BuyingForm
    template_name = "ProductsDetails.html"

    # def get_success_url(self):
    #         return reverse('market:marketing', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ProdsDetails, self).get_context_data(**kwargs)
        # context['form'] = self.get_form()
        context['user'] = self.request.user
        context['form'] = BuyingForm
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)
        return context



    # def post(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden()
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_valid(self, form):
    #     # Here, we would record the user's interest using the message
    #     # passed in form.cleaned_data['message']
    #     return super(ProdsDetails, self).form_valid(form)
from django.views.generic.base import TemplateResponseMixin

from django.contrib import messages
class ProdsForm(FormMessagesMixin, CreateView):
    form_class = BuyingForm
    # form_invalid_message = _(u"Was not created")
    success_url = reverse_lazy('market:register')

    def form_valid(self, form):
        user = form.save(commit=False)
        blocke = UserInfo.objects.get(user=self.request.user.pk)
        walt = Investment.objects.get(user=self.request.user.pk)
        xampesa = Statistics.objects.get(user='xampesa')

        if user.currency == '$':
            if user.processor == Account_balance:
                stock = Products.objects.get(id=user.product_id)
                # pure = Purchases.objects.filter()[0]
                whoa = user.Price_sold * user.quantity
                if user.processor == 'Mpesa':
                    return redirect(reverse('app:mpesa'))
                elif user.processor == 'Tigopesa':
                    return redirect(reverse('app:tigopesa'))
                elif user.processor == 'AirtelMoney':
                    return redirect(reverse('app:airtelmoney'))
                else:
                    if walt.balance >= whoa:
                        if stock.stock_products > 0:
                            walt.balance = walt.balance - whoa
                            stock.stock_products = stock.stock_products - user.quantity
                            sav = Prepurchase.objects.create(userid=user.userid, user=user.user, product_id=user.product_id, product_title=user.product_title, product_owner=user.product_owner, quantity=user.quantity, name_of_receiver=user.name_of_receiver, currency=user.currency, country=user.country, Price_sold=user.Price_sold, Price=user.Price, Region=user.Region, Street=user.Street, processor=user.processor, phone_no=user.phone_no, Receive_acc=user.Receive_acc  )
                            xampesa.total_deposited = xampesa.total_deposited + whoa
                            xampesa.total_balance = xampesa.total_balance + whoa
                            stock.save()
                            walt.save()
                            user.save()
                            sav.save()
                            return redirect(reverse('market:register'))
                        else:
                            messages.error(self.request, "Product is Out of stock")
                            return redirect(reverse('app:account'))
                    else:
                        messages.error(self.request, "Insufficient Balance")
                        return redirect(reverse('market:register'))
            elif user.processor == Perfectmoney:
                stock = Products.objects.get(id=user.product_id)
                perfect = Processors.objects.get(user=self.request.user)
                whoa = user.Price_sold * user.quantity
                if walt.balance >= whoa:
                    if perfect.perfectmoney >= whoa:
                        if stock.stock_products > 0:
                            walt.balance = walt.balance - whoa
                            perfect.perfectmoney = perfect.perfectmoney - whoa
                            stock.stock_products = stock.stock_products - user.quantity
                            xampesa.total_deposited = xampesa.total_deposited + whoa
                            xampesa.total_balance = xampesa.total_balance + whoa
                            stock.save()
                            walt.save()
                            user.save()
                            perfect.save()
                            return redirect(reverse('market:register'))
                        else:
                            messages.error(self.request, "Product is Out of stock")
                            return redirect(reverse('app:account'))

            elif user.processor == Payeer:
                stock = Products.objects.get(id=user.product_id)
                payeer = Processors.objects.get(user=self.request.user)
                whoa = user.Price_sold * user.quantity
                if walt.balance >= whoa:
                    if payeer.payeer >= whoa:
                        if stock.stock_products > 0:
                            walt.balance = walt.balance - whoa
                            payeer.payeer = payeer.payeer - whoa
                            stock.stock_products = stock.stock_products - user.quantity
                            xampesa.total_deposited = xampesa.total_deposited + whoa
                            xampesa.total_balance = xampesa.total_balance + whoa
                            stock.save()
                            walt.save()
                            user.save()
                            payeer.save()
                            return redirect(reverse('market:register'))
                        else:
                            messages.error(self.request, "Product is Out of stock")
                            return redirect(reverse('app:account'))
        elif user.currency == 'BTC':
            bitcoinbal = Processors.objects.get(user=self.request.user)
            stock = Products.objects.get(id=user.product_id)
            whoa = user.Price_sold * user.quantity
            if walt.Bitcoin_balance > 0.0001:
                if whoa < bitcoinbal.bitcoin:
                    if stock.stock_products > 0:
                        stock.stock_products = stock.stock_products - user.quantity
                        walt.Bitcoin_balance = walt.Bitcoin_balance - whoa
                        xampesa.bitcoin_total_deposited = xampesa.bitcoin_total_deposited + whoa
                        xampesa.bitcoin_total_balance = xampesa.bitcoin_total_balance + whoa
                        stock.save()
                        walt.save()
                        xampesa.save()
                        user.save()
                        return redirect(reverse('market:register'))
                    else:
                        messages.error(self.request, "Product is Out of stock")
                        return redirect(reverse('app:account'))
        return redirect(reverse('app:account'))






    # def get_form_valid_message(self):
    #     return u"{0} Created!" .format(self.object.title)


class CredsForm(generic.CreateView):
    form_class = CreditCardForm
    success_url = reverse_lazy('market:register')


class HomeList(generic.ListView):
    model = Products
    template_name = 'home.html'
    context_object_name = "queryset_list"
    Mavuno = Products.objects.all()


    # def get_queryset(self):
    #     cout = UserInfo.objects.get(user=self.request.user.pk)
    #     watre = cout.user
    #     return Purchases.objects.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super(HomeList, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     # cout = UserInfo.objects.get(user=self.request.user.pk)
    #     # watre = cout
    #     context['Mavuno'] = Products.objects.all()
    #     return context
class OrdersList(generic.ListView):
    model = Purchases
    template_name = 'orderlist.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(OrdersList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
        return context

    def get_queryset(self):
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        return Purchases.objects.filter(product_owner=watre).exclude(order_actions='Cancelled')


class Orderdetails(generic.DetailView):
    template_name = 'orderdetails.html'
    model = Purchases

    def get_context_data(self, **kwargs):
        context = super(Orderdetails, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        return context


class OrderReturn(CreateView):
    form_class = ReturnedPurchaseForm
    success_url = reverse_lazy('market:register')

    def form_valid(self, form):
        userclass = form.save(commit=False)
        my = UserInfo.objects.get(user=self.request.user)
        inv = Purchases.objects.get(id=userclass.userid)
        if inv.order_actions == Cancelled:
            return redirect(reverse('market:customers'))
        else:
            whoa = Purchases.objects.filter(id=userclass.userid).update(order_actions=Cancelled)
            inve = inv.buyers_acc
            purch = Investment.objects.filter(account_no=inve)
            myee = inv.Price_sold
            for p in purch:
                print(p.balance)
                p.balance = p.balance + myee
                p.save()
                userclass.save()
                return redirect(reverse('market:register'))


class CustomerOrders(generic.ListView):
    template_name = 'customerorder.html'
    model = Purchases
    success_url = reverse_lazy('market:register')
    time = timezone.now()
    # dateto = datetime.date.today()

    def get_context_data(self, **kwargs):
        context = super(CustomerOrders, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        context['time'] = timezone.now()
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
        # context['range'] = range(context["paginator"].num_pages)
        return context
#
    # def get_queryset(self):
    #     coutm = UserInfo.objects.get(user=self.request.user.pk)
    #     watrem = coutm.user
    #     queryset=Purchases.objects.filter(user=watrem)
    #     return queryset

#
#     context = {
#         'queryset': objz
#     }
#     return render(request, 'home.html', context)






class CustomerOrdersDetails(generic.DetailView):
    template_name = 'customerorderDetails.html'
    model = Purchases
    success_url = reverse_lazy('market:register')


    def get_context_data(self, **kwargs):
        context = super(CustomerOrdersDetails, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        context['time'] = timezone.now()
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        # context['range'] = range(context["paginator"].num_pages)
        return context



class Receiveupdate(generic.DetailView):
    model = Purchases
    template_name = "Receiveupdate.html"


    # def get_context_data(self, **kwargs):
    #     context = super(Receiveupdate, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     coutm = UserInfo.objects.get(user=self.request.user.pk)
    #     watrem = coutm.user
    #     context['queryset'] = Purchases.objects.filter(user=watrem)
    #     return context

#
#
# class ReceiveForme(PaginationMixin, UpdateView):
#     model = Purchases
#     # form_class = BuyingForm
#     success_url = reverse_lazy('market:register')
#     template_name = "Receiveupdate.html"
#
#     # def form_valid(self, form):
#     #     walt = UserInfo.objects.get(user=self.request.user.pk)
#     #     waltem = walt.user
#     #     won = Purchases.objects.filter(user=waltem)[0]
#     #     pric = won.Price
#     #     mine = Investment.objects.get(user=self.request.user.pk)
#     #     Acc = 'X11111111'
#     #     To = won.Receive_acc
#     #     Acc_q = Investment.objects.filter(account_no=Acc)
#     #     Acc_To = Investment.objects.filter(account_no=To)
#     #     for Aq in Acc_q:
#     #         for qt in Acc_To:
#     #             Aq.balance = Aq.balance - pric
#     #             qt.balance = qt.balance - pric
#     #             Aq.save()
#     #             qt.save()
#     #     return redirect(reverse('market:register'))




class DialogUpdate(generic.UpdateView):
    model = Purchases
    template_name = "Receiveupdate.html"


    def get_context_data(self, **kwargs):
        context = super(DialogUpdate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
        return context



class Caret(generic.CreateView):
    form_class = CartForm
    success_url = reverse_lazy('market:cartlist')


class Cartlist(generic.ListView):
    model = Cart
    template_name = 'cartlist.html'

    def get_queryset(self):
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.full_name
        return Cart.objects.filter(username=watrem)


    def get_context_data(self, **kwargs):
        context = super(Cartlist, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['computers'] = Products.objects.filter(category__icontains="Computers & office")[:1]
        context['clothing'] = Products.objects.filter(category__icontains="Clothing")[:1]
        context['improvement'] = Products.objects.filter(category__icontains="Home improvement")[:1]
        context['others'] = Products.objects.filter(category__icontains="others")[:1]
        context['sports'] = Products.objects.filter(category__icontains="Sports & Outdoors")[:1]
        context['jewelry'] = Products.objects.filter(category__icontains="jewelry & watches")[:1]
        context['hair'] = Products.objects.filter(category__icontains="Hair extension's & wigs")[:1]
        context['office'] = Products.objects.filter(category__icontains="office & school supplys")[:1]
        context['health'] = Products.objects.filter(category__icontains="Health & Beauty")[:1]
        context['phones'] = Products.objects.filter(category__icontains="Phones & accessories")[:1]
        context['homegarden'] = Products.objects.filter(category__icontains="Home & garden")[:1]
        context['clotheswomen'] = Products.objects.filter(category__icontains="clothes & accessories Women")[:1]
        context['clothesmen'] = Products.objects.filter(category__icontains="clothes & accessories Men")[:1]
        context['bags'] = Products.objects.filter(category__icontains="Bags & Luggage")[:1]
        context['toys'] = Products.objects.filter(category__icontains="Toys and Hobbies")[:1]
        context['wedding'] = Products.objects.filter(category__icontains="Wedding & events")[:1]
        context['automobiles'] = Products.objects.filter(category__icontains="Automobiles & motorcycles")[:1]
        context['lights'] = Products.objects.filter(category__icontains="Lights & Lighting")[:1]
        context['security'] = Products.objects.filter(category__icontains="Security & protection")[:1]
        context['electronics'] = Products.objects.filter(category__icontains="Electronics & supplies")[:1]
        context['Furnitures'] = Products.objects.filter(category__icontains="Furniture's")[:1]
        context['time'] = timezone.now()
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.full_name
        context['Mavuno'] = Purchases.objects.filter(product_owner=watre).exclude(status='Received').exclude(order_actions=Cancelled)
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.user
        context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received').exclude(order_actions=Cancelled)
        # context['range'] = range(context["paginator"].num_pages)
        return context
    # def get_context_data(self, **kwargs):
    #     context = super(Cartlist, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     coutm = UserInfo.objects.get(user=self.request.user.pk)
    #     watrem = coutm.full_name
    #     print(watrem)
    #     context['Obj'] = Cart.objects.filter(username=watrem)


class Cartdelete(SuccessMessageMixin, DeleteView):
    model = Cart
    template_name = 'cartlist.html'
    success_url = reverse_lazy('market:cartlist')
    success_message = "Post was successfully Deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Cartdelete, self).delete(request, *args, **kwargs)




class Finnished(CreateView):
    form_class = FinnishedForm
    success_url = reverse_lazy('market:customers')


    def form_valid(self, form):
        userm = form.save(commit=False)
        receiver = userm.Receive_acc
        pur_id = userm.purchase_id
        pol = Purchases.objects.get(id=pur_id)
        po = pol.status
        if userm.currency == '$':
            if po != "Received":
                if pol.order_actions != Cancelled:
                    upd = Purchases.objects.filter(id=pur_id).update(status='Received')
                    trans = Investment.objects.get(account_no=receiver)
                    stat = Statistics.objects.get(user='lewicpro')
                    trans.balance = trans.balance + userm.Price
                    prof = userm.Price_sold - userm.Price
                    stat.profit = stat.profit + prof
                    trans.save()
                    userm.save()
                    stat.save()
                    return redirect(reverse('market:customers'))
                else:
                    messages.success(self.request, "Order is already Cancelled")
                    return redirect(reverse('market:register'))

            else:
                messages.success(self.request, "You have already accepted before")
                return redirect(reverse('market:register'))
        elif userm.currency =='BTC':
            if po != "Received":
                if pol.order_actions != Cancelled:
                    upd = Purchases.objects.filter(id=pur_id).update(status='Received')
                    trans = Investment.objects.get(account_no=receiver)
                    stat = Statistics.objects.get(user='xampesa')
                    trans.Bitcoin_balance = trans.Bitcoin_balance + userm.Price
                    prof = userm.Price_sold - userm.Price
                    stat.bitcoin_profit = stat.bitcoin_profit + prof
                    trans.save()
                    userm.save()
                    stat.save()
                    return redirect(reverse('market:customers'))
                else:
                    messages.success(self.request, "Order is already Cancelled")
                    return redirect(reverse('market:register'))

            else:
                messages.success(self.request, "You have already accepted before")
                return redirect(reverse('market:register'))

    #
    # def get_context_data(self, **kwargs):
    #     context = super(Finnished, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     coutm = UserInfo.objects.get(user=self.request.user.pk)
    #     watrem = coutm.user
    #     context['queryset'] = Purchases.objects.filter(user=watrem).exclude(status='Received')
    #     return context
    #
    # def form_valid(self, form):
    #     walt = UserInfo.objects.get(user=self.request.user.pk)
    #     waltem = walt.user
    #     won = Purchases.objects.filter(user=waltem)[0]
    #     pric = won.Price
    #     mine = Investment.objects.get(user=self.request.user.pk)
    #     Acc = '	X08408484'
    #     To = won.Receive_acc
    #     Acc_q = Investment.objects.filter(account_no=Acc)
    #     Acc_To = Investment.objects.filter(account_no=To)
    #     for Aq in Acc_q:
    #         for qt in Acc_To:
    #             Aq.balance = Aq.balance - pric
    #             qt.balance = qt.balance - pric
    #             Aq.save()
    #             qt.save()
    #             return redirect(reverse('market:register'))
    #     return redirect(reverse('market:register'))






class PriceProducts(CreateView):
    model = PaidProducts
    form_class = PriceProductsForm
    success_url = reverse_lazy("market:register")
    template_name = 'paidproducts.html'

    # def get_context_data(self, **kwargs):
    #     context = super(PriceProducts, self).get(*kwargs)
    #     context['user'] = self.request.user
    #     mom = UserInfo.objects.get(user=self.request.user.pk)
    #     ms = mom.user
    #     context['More'] = PaidProducts.objects.filter(username=ms)
    def form_valid(self, form):
        usern = form.save(commit=False)
        bal=Investment.objects.get(user=self.request.user)

        if usern.AdsPackage == Week1:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 8/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 2/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Weeks2:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 9/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 3/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Weeks3:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 10/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 4/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month1:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 13/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 5 /100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month1Weeks2:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 14/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 6/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month2:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 15/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 8/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month2Weeks2:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 18/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 10/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month3:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 19/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 12/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month3Weeks2:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 26/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 13/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month4:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 18/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 16/100
                print('else')
                bal.balance = bal.balance - priceAds

        elif usern.AdsPackage == Month4Weeks2:
            print('first if')
            if usern.Price < 50:
                print('second if')

                priceAds= usern.Price * 28/100
                bal.balance = bal.balance - priceAds

            else:
                priceAds = usern.Price * 18/100
                print('else')
                bal.balance = bal.balance - priceAds
        bal.save()
        usern.save()
        return redirect(reverse('market:register'))




class PriceProductdetails(generic.DetailView):
    model = PaidProducts
    template_name = 'paidproductsdetails.html'




class Ordercomplete(UpdateView):
    model = Purchases
    template_name = 'orderlist.html'
    fields = ['complete']
    success_url = reverse_lazy('market:customers')



class CustomertDismiss(UpdateView):
    model = Purchases
    # form_class = BuyingForm
    template_name = 'customerorder.html'
    fields = ['customers_status']
    success_url = reverse_lazy('market:customers')


    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     updt = Purchases.objects.filter(id=self.request.id.pk).update(customer_status=Delayed)
    #     user.save()
    #     updt.save()
    #     return redirect(reverse("market:customers"))





class SentbysellerDismiss(UpdateView):
    model = Purchases
    # form_class = BuyingForm
    template_name = 'orderlist.html'
    fields = ['sellers_status']
    success_url = reverse_lazy('market:orders')





class MyProductPaiddetails(DetailView):
    model = PaidProducts
    template_name = 'myproductpaid.html'



class PaidProductdelete(DeleteView):
    model = PaidProducts
    template_name = 'myproductpaid.html'
    success_url = reverse_lazy('market:myproducts')




class PaidProductedit(UpdateView):
    model = PaidProducts
    form_class = PriceProductsForm
    template_name = 'paidproducts.html'
    success_url = reverse_lazy('market:myproducts')
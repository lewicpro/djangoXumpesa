from .forms import *
from PIL import Image, ImageFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from .models import *
from django.core.paginator import Paginator
from braces.views import FormMessagesMixin
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden
import operator
from django.http import HttpResponse
from functools import reduce
from rest_framework.response import Response
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, FormMixin, UpdateView, ModelFormMixin
from django.views import generic
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from rest_framework.views import APIView

#


class hire(CreateView):
    template_name = 'uploadjobs.html'
    form_class = hireform
    success_url = reverse_lazy('jobs:all')#

    def get_context_data(self, **kwargs):
        context = super(hire, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        detor = UserInfo.objects.get(user=self.request.user.pk)
        gol = detor.user
        context['Accep'] = AcceptedApp.objects.filter(applier=gol)
        context['Accepte'] = AcceptedApp.objects.filter(applier=gol, reade='Unread')
        return context


class all(ListView):
    model = Jobs
    form_class = Markform
    template_name = 'jobsAll.html'
    success_url = reverse_lazy('jobs:all')

    def get_context_data(self, **kwargs):
        context = super(all, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['object'] = Jobs.objects.all()
        walt = UserInfo.objects.get(user=self.request.user)
        waltem = walt.user
        context['Markedm'] = Marked.objects.filter(full_name=waltem)
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')

        return context


class Mark(CreateView):
    form_class = Markform
    success_url = reverse_lazy('jobs:all')


class Markede(ListView):
    model = Marked
    success_url = reverse_lazy('jobs:all')
    template_name = 'marked.html'
    # paginate_by = 10

    # def get_queryset(self):
    #     walt = UserInfo.objects.get(user=self.request.user)
    #     waltem = walt.user
    #
    #     return Marked.objects.filter(full_name=waltem)

    def get_context_data(self, **kwargs):
        context = super(Markede, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        context['object_list']=Marked.objects.filter(full_name=waltem)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(Markede, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     walt = UserInfo.objects.get(user=self.request.user)
    #     waltem = walt.user
    #     context['Markede'] = Marked.objects.filter(full_name=waltem)



#
# def Mark(request, pk):
#     instance = Jobs.objects.get(pk=pk)
#     form = Markform(request.POST or None, instance=instance)
#     context = {
#         'walt' : instance,
#         'form': form,
#     }
#     if form.is_valid():
#         user = form.save(commit=False)
#         user.save()
#         instance.save()
#         return redirect(reverse('jobs:all'))
#
#
#
#     return render(request, 'marked.html', context)

class Myjobposts(ListView):
    model = Jobs
    template_name = 'myposts.html'

    # def get_queryset(self):
    #     walt = UserInfo.objects.get(user=self.request.user)
    #     waltem = walt.user
    #     return Jobs.objects.filter(full_name=waltem)

    def get_context_data(self, **kwargs):
        context = super(Myjobposts, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        walt = UserInfo.objects.get(user=self.request.user)
        waltem = walt.user
        context['pro'] = Jobs.objects.filter(user=waltem)

        mor = UserInfo.objects.get(user=self.request.user)
        morke = mor.user
        context['Accep'] = AcceptedApp.objects.filter(applier=morke)
        context['Accepte'] = AcceptedApp.objects.filter(applier=morke, reade='Unread')
        context['proma'] = Application.objects.filter(acc_owner=morke).exclude(status="Accepted")
        context['Accep'] = AcceptedApp.objects.filter(applier=morke)
        return context


class alldetailview(DetailView):
    model = Jobs
    template_name = 'jobsAlldetailview.html'

    def get_context_data(self, **kwargs):
        context = super(alldetailview, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['object'] = Jobs.objects.all()
        walt = UserInfo.objects.get(user=self.request.user)
        waltem = walt.user
        context['Markedm'] = Marked.objects.filter(full_name=waltem)
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')

        return context



class Postdelete(SuccessMessageMixin, DeleteView):
    template_name = "myposts.html"
    model = Jobs
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Postdelete, self).delete(request, *args, **kwargs)


class Unmarked(SuccessMessageMixin, DeleteView):
    template_name = "marked.html"
    model = Marked
    success_url = reverse_lazy('jobs:Marked')
    success_message = "Post was successfully Deleted"

    def deleted(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Unmarked, self).delete(request, *args, **kwargs)


class PostUpdate(SuccessMessageMixin, UpdateView):
    template_name = "uploadjobs.html"
    model = Jobs
    form_class = hireform
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"


class UploadCV(CreateView):
    template_name = "uploadcv.html"
    form_class = CV1form
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(UploadCV, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        detor = UserInfo.objects.get(user=self.request.user.pk)
        gol = detor.user
        context['Accep'] = AcceptedApp.objects.filter(applier=gol)
        context['Accepte'] = AcceptedApp.objects.filter(applier=gol, reade='Unread')
        return context
    #
    # def update(self, request, *args, **kwargs):
    #     return " Post was successfully Update"


class CVe(ListView):
    template_name = "uploadcv.html"
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(CVe, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        detor = UserInfo.objects.get(user=self.request.user.pk)
        gol = detor.user
        context['Accep'] = AcceptedApp.objects.filter(applier=gol)
        context['Accepte'] = AcceptedApp.objects.filter(applier=gol, reade='Unread')
        return context


class Personalview(CreateView):
    template_name = "Details.html"
    title = 'Personal Details'
    form_class = CV1form
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Personalview, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Personalview, self).form_valid(form)


class Contact(CreateView):
    template_name = "contact.html"
    form_class = ContactForm
    title = 'Contacts Details'
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Contact, self).form_valid(form)


class Academic(CreateView):
    template_name = "qualifications.html"
    form_class = AcademicForm
    title = 'Academic Qualifications'
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Academic, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Academic, self).form_valid(form)


class Proffesion(CreateView):
    template_name = "profession.html"
    form_class = ProffessionForm
    title = 'Profession'
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Proffesion, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Proffesion, self).form_valid(form)


class Language(CreateView):
    template_name = "language.html"
    form_class = LanguageForm
    title = 'Language Proficiency'
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Language, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Language, self).form_valid(form)


class Work(CreateView):
    template_name = "work.html"
    title = 'Work Experiment'
    form_class = WorkForm
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Work, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Work, self).form_valid(form)


class Training(CreateView):
    template_name = "taining.html"
    form_class = TrainingForm
    title = 'Training & Work Attended'
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Training, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Training, self).form_valid(form)


class Computer(CreateView):
    template_name = "computer.html"
    form_class = ComputerForm
    title = 'Computer Literacy'
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Computer, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Computer, self).form_valid(form)


class Refree(CreateView):
    template_name = "refree.html"
    form_class = RefreeForm
    title = 'Referee Details'
    success_url = reverse_lazy('jobs:posts')
    success_message = "Post was successfully Updated"

    def get_context_data(self, **kwargs):
        context = super(Refree, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = self.title
        us = UserInfo.objects.get(user=self.request.user.pk)
        waltem = us.user
        context['Accep'] = AcceptedApp.objects.filter(applier=waltem)
        context['Accepte'] = AcceptedApp.objects.filter(applier=waltem, reade='Unread')
        return context

    def form_valid(self, form):
        instance= form.save(commit=False)
        instance.user = self.request.user
        # instance.save()
        # return render(self.request, reverse('jobs:posts'))
        return super(Refree, self).form_valid(form)


class Applyi(generic.CreateView):
    form_class = ApplicationForm
    success_url = reverse_lazy('jobs:all')


    def form_valid(self, form):
        userme = form.save(commit=False)
        inv = Investment.objects.get(user=self.request.user)
        use = UserInfo.objects.get(user=self.request.user)
        prem = Processors.objects.get(user=self.request.user)
        stat = Statistics.objects.get(user='lewicpro')

        if prem.perfectmoney > 1:
            inv.balance = inv.balance - 1
            prem.perfectmoney = prem.perfectmoney - 1
            stat.profit = stat.profit + 1

        elif prem.okpay > 1:
            inv.balance = inv.balance - 1
            prem.okpay = prem.okpay - 1
            stat.profit = stat.profit + 1

        elif prem.adcash > 1:
            inv.balance = inv.balance - 1
            prem.adcash = prem.adcash - 1
            stat.profit = stat.profit + 1

        elif prem.payeer > 1:
            inv.balance = inv.balance - 1
            prem.payeer = prem.payeer - 1
            stat.profit = stat.profit + 1

        elif prem.bitcoin > 1:
            inv.balance = inv.balance - 0.0001
            prem.bitcoin = prem.bitcoin - 0.0001
            stat.bitcoin_profit = stat.bitcoin_profit + 0.0001

        inv.save()
        stat.save()
        prem.save()
        userme.save()
        return redirect(reverse('jobs:all'))



class Applicationdisplay(generic.ListView):
    model = Cart
    template_name = 'cartlist.html'

    def get_queryset(self):
        coutm = UserInfo.objects.get(user=self.request.user.pk)
        watrem = coutm.full_name
        return Cart.objects.filter(username=watrem)


class JobsAppliedView(ListView):
    model = Application
    template_name = 'jobsapplied.html'

    def get_context_data(self, **kwargs):
        context = super(JobsAppliedView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        det = UserInfo.objects.get(user=self.request.user.pk)
        gol = det.user
        context['applied'] = Application.objects.filter(user=gol)
        context['Accep'] = AcceptedApp.objects.filter(applier=gol)
        context['Accepte'] = AcceptedApp.objects.filter(applier=gol, reade='Unread')
        return context


class ApplicationDelete(SuccessMessageMixin, DeleteView):
    template_name = "jobsapplied.html"
    model = Application
    success_url = reverse_lazy('jobs:Jobsapplied')
    success_message = "Post was successfully Deleted"


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ApplicationDelete, self).delete(request, *args, **kwargs)


class ApplicationList(ListView):
    model = Application
    template_name = "Appliedlist.html"

    def get_context_data(self, **kwargs):
        context = super(ApplicationList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        det = UserInfo.objects.get(user=self.request.user.pk)
        gol = det.user
        context['List'] = Application.objects.filter(acc_owner=gol).exclude(status="Accepted")
        return context


class ApplicationDetails(DetailView):
    model = Application
    template_name = "Applicationdetail.html"


class Accepted(CreateView):
    form_class = AcceptedForm
    success_url = reverse_lazy('jobs:all')

    def form_valid(self, form):
        userm = form.save(commit=False)
        mor = UserInfo.objects.get(user=self.request.user.pk)
        walr = mor.user
        data = Application.objects.filter(id=userm.job_id).update(status="Accepted")
        userm.save()
        return redirect(reverse("jobs:all"))


class AcceptedDetails(ListView):
    model = AcceptedApp
    template_name = 'acceptedlist.html'

    def get_context_data(self, **kwargs):
        context = super(AcceptedDetails, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        detor = UserInfo.objects.get(user=self.request.user.pk)
        gol = detor.user
        context['Accep'] = AcceptedApp.objects.filter(applier=gol)
        context['Accepte'] = AcceptedApp.objects.filter(applier=gol, reade='Unread')
        return context

class Acceptedreads(UpdateView):
    model = AcceptedApp
    fields = ['reade']
    template_name = 'acceptedlist.html'
    success_url = reverse_lazy('jobs:Acceptdetauils')

    def get_context_data(self, **kwargs):
        context = super(Acceptedreads, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        detor = UserInfo.objects.get(user=self.request.user.pk)
        gol = detor.user
        context['Accep'] = AcceptedApp.objects.filter(applier=gol)
        context['Accepte'] = AcceptedApp.objects.filter(applier=gol, reade='Unread')
        return context




class msgdelete(DeleteView):
    model = AcceptedApp
    template_name = 'acceptedlist.html'
    success_url = reverse_lazy('jobs:Acceptdetauils')

    def get_context_data(self, **kwargs):
        context = super(Acceptedreads, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        detor = UserInfo.objects.get(user=self.request.user.pk)
        gol = detor.user
        context['Accep'] = AcceptedApp.objects.filter(applier=gol)
        context['Accepte'] = AcceptedApp.objects.filter(applier=gol, reade='Unread')
        return context
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def representatives(request):
    title = 'Representative'
    queryset = Representative.objects.filter(status="Rejected", user=request.user)

    if queryset:
        if request.user.is_authenticated():
            title = "Welcome %s, fill up the representative request " % request.user
            Request = "Request"
        instance = Representative.objects.get(user=request.user.pk)
        form = RepresentativesForm(request.POST or None, instance=instance)
        context = {
            "title": title,
            "form": form,
            "button": Request,
            "queryset": queryset
        }

        if form.is_valid():
            user = form.save(commit=False)
            instance.save()
            user.save()
            messages.success(request, 'Request sent')
        return render(request, 'representatives.html', context)
    else:
        if request.user.is_authenticated():
            title = "Welcome %s, Already a representative, give your suggestions about the platform " % request.user
            send = "Send"
        form = SuggestForm(request.POST or None)
        context = {
            "title": title,
            "form": form,
            "button": send,
            #"queryset": queryset
        }

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Message sent')
        return render(request, 'representatives.html', context)


def accepted(request):
    query = Representative.objects.filter(status="Accepted")
    paginator = Paginator(query, 25)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        representative = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        representative = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        representative = paginator.page(paginator.num_pages)
    context = {
        "query": representative

    }
    return render(request, 'accepted.html', context)





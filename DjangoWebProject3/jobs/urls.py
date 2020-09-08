from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'jobs'
urlpatterns = [
    url(r'^$', views.all.as_view(), name='all'),
    url(r'^Hire', login_required(views.hire.as_view()), name='jobs'),
    url(r'^post/(?P<pk>[0-9]+)/$', login_required(views.alldetailview.as_view()), name='alldetails'),
    url(r'^myposts/', login_required(views.Myjobposts.as_view()), name='posts'),
    url(r'^post/accepted/delete/(?P<pk>[0-9]+)$', login_required(views.Postdelete.as_view()), name='postdelete'),
    url(r'^post/(?P<pk>[0-9]+)$', login_required(views.msgdelete.as_view()), name='msgdelete'),
    url(r'^post/(?P<pk>[0-9]+)/update$', login_required(views.PostUpdate.as_view()), name='update'),
    url(r'^post/mark/(?P<pk>[0-9]+)$', login_required(views.Mark.as_view()), name='Mark'),
    url(r'^post/marked/$', login_required(views.Markede.as_view()), name='Marked'),
    url(r'^post/Unmark/(?P<pk>[0-9]+)$', login_required(views.Unmarked.as_view()), name='unmark'),
    url(r'^post/Applied/(?P<pk>[0-9]+)$', login_required(views.ApplicationDelete.as_view()), name='deleteapp'),
    url(r'^post/Unmark/$', login_required(views.UploadCV.as_view()), name='Upload'),
    url(r'^post/contact/$', login_required(views.Contact.as_view()), name='contactdetails'),
    url(r'^post/personal/$', login_required(views.Personalview.as_view()), name='personal'),
    url(r'^post/academic/$', login_required(views.Academic.as_view()), name='academic'),
    url(r'^post/proffesion/$', login_required(views.Proffesion.as_view()), name='profession'),
    url(r'^post/language/$', login_required(views.Language.as_view()), name='language'),
    url(r'^post/Work/$', login_required(views.Work.as_view()), name='Work'),
    url(r'^post/Training/$', login_required(views.Training.as_view()), name='Training'),
    url(r'^post/Computer/$', login_required(views.Computer.as_view()), name='Computer'),
    url(r'^post/Referee/$', login_required(views.Refree.as_view()), name='Refree'),
    url(r'^post/Apply/(?P<pk>[0-9]+)$', login_required(views.Applyi.as_view()), name='Applye'),
    url(r'^post/Requested/$', login_required(views.ApplicationList.as_view()), name='Applist'),
    url(r'^post/Accept/$', login_required(views.Accepted.as_view()), name='Accept'),
    url(r'^post/accepted/$', login_required(views.AcceptedDetails.as_view()), name='Acceptdetauils'),
    url(r'^post/accepted/(?P<pk>[0-9]+)$', login_required(views.Acceptedreads.as_view()), name='Acceptedreads'),
    url(r'^post/Requested/(?P<pk>[0-9]+)/$', login_required(views.ApplicationDetails.as_view()), name='Appdetails'),
    url(r'^post/Applied/$', login_required(views.JobsAppliedView.as_view()), name='Jobsapplied'),
    # url(r'^upload', login_required(views.jobs.as_view()), name='jobs'),
  ]
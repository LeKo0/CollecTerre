from django.conf.urls import url
from organisations.views import HomeView, InscriptionView, GestionView, ProfilView
from django.contrib.auth.views import (login, logout)
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/home/organisations', permanent=False), name="redirect"),
    url(r'^inscription/$', InscriptionView.as_view(), name="inscription"),
   
    url(r'^login/$', login, {'template_name':'organisations/login.html'}, name="login"),
    url(r'^logout/$', logout, {'template_name':'organisations/logout.html'}, name="logout"),
    url(r'^profil/(?P<pk>\d+)/$', ProfilView.as_view(), name='profil')
]

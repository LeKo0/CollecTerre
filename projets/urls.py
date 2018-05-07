from django.conf.urls import url
from projets.views import HomeView, SoumissionView, ProjetView, ProjetCreateView, SoumissionView
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/home/projets', permanent=False), name="redirect"),
    url(r'^(?P<pk>\d+)/$', ProjetView.as_view(), name='projet'),
    url(r'^gestion/$', ProjetCreateView.as_view(), name='projet_create'),
    url(r'^(?P<pk>\d+)/soumission$', SoumissionView.as_view(), name='soumission'),
]

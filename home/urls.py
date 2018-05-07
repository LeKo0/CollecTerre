from django.conf.urls import url
from home.views import HomeView, OrganisationsView, ProjetsView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^organisations/$', OrganisationsView.as_view(), name="organisations"),
    url(r'^projets/$', ProjetsView.as_view(), name="projets"),
]

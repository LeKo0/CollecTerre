from django.views.generic import TemplateView
from django.shortcuts import render
from organisations.models import Organisation
from projets.models import Projet


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        last_four = Projet.objects.all().order_by('-id')[:4]

        return render(request, self.template_name, {'list' : last_four})

class OrganisationsView(TemplateView):
    template_name = 'home/organisations.html'

    def get(self, request):
        orgs_list = Organisation.objects.all().order_by('-id')
        return render(request, self.template_name, {'list' : orgs_list})

class ProjetsView(TemplateView):
    template_name = 'home/projets.html'

    def get(self, request):
        proj_list = Projet.objects.all().order_by('-id')
        return render(request, self.template_name, {'list' : proj_list})

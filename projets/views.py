from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from projets.models import Projet, Zone, Soumission
from organisations.models import Organisation
from projets.forms import ProjetForm, SoumissionForm
from django.urls import reverse
from django.http import HttpResponseRedirect
#import re
import json

class HomeView(TemplateView):
    template_name = 'projets/home.html'

    def get(self, request):
        return render(request, self.template_name)

class SoumissionView(TemplateView):
    template_name = 'projets/soumission.html'

    def get(self, request, pk):
        
        form = SoumissionForm()
        args = {'form':form}

        return render(request, self.template_name, args)


    def post(self, request, pk):

        form = SoumissionForm(request.POST, request.FILES)

        if form.is_valid():
            sub = form.save(commit=False)
            sub.projet = Projet.objects.get(pk=pk)
            sub.save()
            return redirect(reverse('home:home'))



class ProjetView(TemplateView):
    template_name = 'projets/projet.html'

    def get(self, request, pk):
        projet = Projet.objects.get(pk=pk)
        org = Organisation.objects.get(id=projet.organisation_id)
        soumissions = Soumission.objects.filter(projet_id=projet.id)
        

        if projet.zone_id is not None:
            zone_id=projet.zone_id
            poly = Zone.objects.get(id=zone_id).mpoly.json #.split('{"type": "MultiPolygon", "coordinates":', 1)[1]
            dic = json.loads(poly)
            poly_fix = dic['coordinates']
        
        else:
            poly_fix = None
        
        args = {'projet' : projet, 'org' : org, 'poly' : poly_fix, 'soumissions' : soumissions,}

        return render(request, self.template_name, args)
 
class ProjetCreateView(TemplateView):
    template_name = 'projets/projet_create.html'

    def get(self, request):
        form = ProjetForm()
        args = {'form':form}
        
        return render(request, self.template_name, args)

    def post(self, request):    
        
        form = ProjetForm(request.POST)
        
        if form.is_valid():

            form.save()
            return redirect(reverse('home:home'))



from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from organisations.models import Organisation
from projets.models import Projet
from organisations.forms import RegistrationForm

class HomeView(TemplateView):
    template_name = 'organisations/home.html'

    def get(self, request):
        return render(request, self.template_name)

class InscriptionView(TemplateView):
    template_name = 'organisations/inscription.html'
    def post(self, request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    def get(self, request):
        form = RegistrationForm()
        args = {'form': form}
        return render(request, self.template_name , args)

class GestionView(TemplateView):
    template_name = 'organisations/gestion.html'

    def get(self, request):
        return render(request, self.template_name)



class ProfilView(TemplateView):
    template_name = 'organisations/profil.html'

    def get(self, request, pk):
        organisation = Organisation.objects.get(pk=pk)
        projets = Projet.objects.filter(organisation_id=organisation.id)
        args = {'org':organisation,
                'projets':projets,}

        return render(request, self.template_name, args)



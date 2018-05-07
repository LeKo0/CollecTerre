from django.forms import ModelForm
from projets.models import Projet, Soumission

class ProjetForm(ModelForm):
    class Meta:
        model = Projet
        fields = ['organisation','nom','description','zone','categorie']

class SoumissionForm(ModelForm):
    class Meta:
        model = Soumission
        fields = ['type_fichier','nom','email','fichier']

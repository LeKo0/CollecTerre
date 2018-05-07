from django import forms
from .models import Organisation
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

   class Meta:
        model = Organisation
        fields = ('username','website', 'first_name','last_name','email','password1','password2', 'phone', 'description', 'nom', 'image', )

from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

class Organisation(AbstractUser):

    image = models.ImageField(upload_to='organisations_image', blank=True, null=True)   
    nom = models.CharField(max_length=150, default='')
    description = models.TextField(default='')
    website = models.URLField(default='', blank=True, null=True)
    email = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nom

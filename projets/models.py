from organisations.models import Organisation
from django.contrib.gis.db import models

class Zone(models.Model):

    meta = models.CharField('META', max_length=50)
    nom = models.TextField('Nom')
    description = models.TextField('Description')
    url = models.URLField('En savoir plus : ', max_length=300)

    # Par défaut ESPG : WGS84 (srid=4326)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "zones"


class Projet(models.Model):

    CATEGORIES = (
            ('FO','Forêt'),
            ('EA','Eau'),
            ('AN','Animaux'),
            ('AI','Air'),
            ('IN','Insectes'),
            ('PL','Plantes'),
            ('RC','Rechauffement climatique'),
            ('NA','Aucune'),
            )

    categorie = models.CharField(max_length=10,choices=CATEGORIES,default='NA')
    nom = models.CharField(max_length=150, default='')
    description = models.TextField(default='')
    organisation = models.ForeignKey(Organisation)
    zone = models.ForeignKey(Zone, blank=True, null=True)
    image = models.ImageField(upload_to='projets_image', blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "projets"

class Soumission(models.Model):

    TYPE_FICHIER = (
            ('TX','Texte'),
            ('IM','Image'),
            ('PD','PDF'),
            ('AU','Autre'),
            ('FC','Feuille de calcul'),
            )
    type_fichier = models.CharField(max_length=2,choices=TYPE_FICHIER,default='AU')
    projet = models.ForeignKey(Projet)
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=75, blank=True, null=True)
    fichier = models.FileField(upload_to='soumission')

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "soumissions"


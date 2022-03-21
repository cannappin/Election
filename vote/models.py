
from pickle import TRUE
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date_question = models.DateTimeField('date de publication')

    def __str__ (self):
        return self.question_text

class Realisateur(models.Model):
    nom_realisateur = models.CharField(max_length=30)

    def __str__ (self):
        return self.nom_realisateur

class Genre(models.Model):
    nom_genre = models.CharField(max_length=30)
    question = models.ManyToManyField(Question, blank=True)
    definition_genre = models.CharField(max_length=255, blank = True , null=True)

    def __str__ (self):
        return self.nom_genre

class Acteur(models.Model):
    nom_acteur = models.CharField(max_length=50)
    age_acteur = models.DateField
    experience_acteur = models.DateField(blank=TRUE, null=True)
    pays_acteur = models.CharField(max_length=50)
    image_acteur = models.CharField(max_length=255)

    def __str__ (self):
        return self.nom_acteur


class Plateform(models.Model):
    nom_plateform = models.CharField(max_length=50)
    prix_plateform = models.FloatField(default=0)

    def __str__ (self):
        return self.nom_plateform


class Serie(models.Model):
    nom_serie = models.CharField(max_length=20)
    description_serie = models.CharField(max_length=255)
    # description_serie = models.TextField()
    image_serie = models.CharField(max_length=255)
    votes_serie = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre, blank=True)
    acteur = models.ManyToManyField(Acteur, blank=True)
    question = models.ManyToManyField(Question, blank=True)
    plateform = models.ManyToManyField(Plateform, blank=True)    
    realisateur_serie = models.ForeignKey(Realisateur, on_delete=models.CASCADE)

    def __str__ (self):
        affiche = f"{self.nom_serie}, {self.realisateur_serie}"
        return affiche










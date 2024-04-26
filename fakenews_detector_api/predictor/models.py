from django.db import models

# Create your models here.

class PostRequest(models.Model):
    URL = models.URLField(max_length=200)
    titre=models.CharField(max_length=200)
    auteur=models.CharField(max_length=200)
    contenu=models.TextField()
    prediction=models.CharField(max_length=200, blank=True, null=True)
    
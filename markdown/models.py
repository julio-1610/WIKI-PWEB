from django.db import models

# Create your models here.
class Markdown(models.Model):
  nombre = models.CharField(max_length = 80)
  autor = models.CharField(max_length = 80)
  texto = models.TextField()

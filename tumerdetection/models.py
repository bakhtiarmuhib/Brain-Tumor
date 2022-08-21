from django.db import models

# Create your models here.

class DetectionImage(models.Model):
    
    image = models.FileField(upload_to='photos/')
   

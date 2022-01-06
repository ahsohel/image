from django.db import models

# Create your models here.

class image_up(models.Model):
    name = models.CharField(max_length=400)
    image_logo = models.CharField(max_length=400)
    image_benner = models.CharField(max_length=400)
    def __str__(self):
        return self.name +"----"+self.image_logo +self.image_benner

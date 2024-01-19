from django.db import models

# Create your models here.


class Cisterna(models.Model):
    volume = models.IntegerField('Volume')

    def __str__(self):
        return self.volume

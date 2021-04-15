from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    greens = models.CharField(max_length=50)
    fairways = models.CharField(max_length=50)
    putts = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
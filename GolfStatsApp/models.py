from django.db import models
from users.models import User

# Create your models here.

class Round(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    greens = models.CharField(max_length=50)
    fairways = models.CharField(max_length=50)
    putts = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
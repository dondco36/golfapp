from django.db import models
# from GolfStatsApp import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, models

class User(AbstractUser):
    id = models.AutoField(primary_key=True),

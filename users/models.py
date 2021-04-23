from django.db import models
# from GolfStatsApp import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, models

class User(AbstractUser):
    id = models.AutoField(primary_key=True),

    # def scoreAverager():
    #     average_score = 0
    #     for round in round_set:
    #         average_score += round.score
    #     average_score = average_score/count(round_set)
    #     return average_score

    # average_score = models.IntegerField(default=scoreAverager())
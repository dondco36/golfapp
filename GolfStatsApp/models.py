from django.db import models
from users.models import User

# Create your models here.

class Round(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.CharField(max_length=100)
    par = models.IntegerField()
    score = models.IntegerField()
    greens = models.IntegerField()
    fairways_hit = models.IntegerField()
    total_fairways = models.IntegerField()
    putts = models.IntegerField()

    @property
    def greens_percentage(self):
        return round((self.greens/18)*100, 2)
    
    @property
    def fairways_percentage(self):
        return round((self.fairways_hit/self.total_fairways)*100, 2)

    def __str__(self):
        return f'{self.name}'
from django.db import models

# Create your models here.

class Sports(models.Model):
    team = models.CharField("team name", max_length="50")
    cat = models.CharField("category", max_length="20")
    in_season = models.BooleanField(default=True)
    
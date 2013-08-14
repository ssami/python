from django.db import models

# Create your models here.



class SearchResult(models.Model):
	word = models.CharField(max_length=5000)
	document = models.CharField(max_length=500)
	index_rank = models.IntegerField(default=0)

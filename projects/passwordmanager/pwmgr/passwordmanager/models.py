from django.db import models

# Create your models here.


class Password(models.Model):
	site = models.CharField(max_length=500, primary_key=True)
	username = models.CharField(max_length=500)
	password = models.CharField(max_length=500)
	security_qn = models.CharField(max_length=500, blank=True)
	security_ans = models.CharField(max_length=500, blank=True)


	def __unicode__(self):
		return self.pk	

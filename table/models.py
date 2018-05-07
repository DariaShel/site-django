from django.db import models

# Create your models here.
class DashaTable(models.Model):
	title = models.CharField(max_length=20)
	image = models.CharField(max_length=30)
	timestamp = models.DateField()
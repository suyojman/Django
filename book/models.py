from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=30, blank=False)
	price = models.IntegerField()
	
	def __str__(self):
		return self.title
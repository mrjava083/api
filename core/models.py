from django.db import models

# Create your models here.

class Mega(models.Model):
	title = models.CharField(max_length=255)	
	slug = models.SlugField(max_length=255,unique=True)
	body = models.TextField()

	def __str__(self):
		return self.title

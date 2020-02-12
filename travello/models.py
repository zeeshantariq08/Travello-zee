from django.db import models

# Create your models here.

class Destination(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.IntegerField()
	offer = models.BooleanField(default=False)
	image_url = models.ImageField(upload_to='uploads')



from django.db import models

# Create your models here.
class blog(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	image = models.ImageField(upload_to='images/')
	body = models.CharField(max_length=5000)
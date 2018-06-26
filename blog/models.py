from django.db import models

class blog(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	image = models.ImageField(upload_to='images/')
	body = models.TextField(max_length=5000)
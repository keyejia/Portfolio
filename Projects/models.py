from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
	langAndFram = models.CharField(max_length=500)
	appURL = models.URLField(max_length=200)
	SourceURL = models.URLField(max_length=400)

	def __str__(self):
		return self.title
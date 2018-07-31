from markdown2 import Markdown
from django.db import models
from markdownx.models import MarkdownxField

class blog(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	image = models.ImageField(upload_to='images/', blank=True)
	summary = models.TextField()
	body = MarkdownxField()

	def __str__(self):
		return self.title

	def summaryf(self):
                return self.body[:300]

	def formatted_markdown(self):
		markdown = Markdown()
		return (markdown.convert(self.body))

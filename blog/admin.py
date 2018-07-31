from django.contrib import admin
from .models import blog
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(blog, MarkdownxModelAdmin)


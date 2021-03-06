from django.shortcuts import render, get_object_or_404
from .models import blog
# Create your views here.
def allblogs(request):
	blogs = blog.objects.order_by('date').reverse()
	return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
	cblog = get_object_or_404(blog, pk=blog_id)
	return render(request, 'blog/detail.html', {'cblog': cblog})
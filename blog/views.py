from django.shortcuts import render
from blog.models import BlogPost

def create_blog_view(request):
	return render(request, "blog/create.html", {})
# Create your views here.

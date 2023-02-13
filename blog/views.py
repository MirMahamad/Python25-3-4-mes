from django.http import HttpResponse
from django.shortcuts import render
from . import models

def hello_view(request):
    return HttpResponse('<h1>Hello I love Django</h1>')

def blog_view(request):
    blog = models.Post.objects.all()
    return render(request, 'blog.html', {'blog': blog})

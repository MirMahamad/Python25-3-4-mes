from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models

def hello_view(request):
    return HttpResponse('<h1>Hello I love Django</h1>')

def blog_view(request):
    blog = models.Post.objects.all()
    return render(request, 'blog.html', {'blog': blog})

def post_detailview(request, id):
    post_id = get_object_or_404(models.Post, id=id)
    return render(request, 'post_detail.html', {'post_id': post_id})
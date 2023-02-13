from django.shortcuts import render
from . import models


def book_view(request):
    book = models.Book.objects.all()
    return render(request, 'blog.html', {'blog': book})
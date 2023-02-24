from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def hello_view(request):
    return HttpResponse('<h1>Hello I love Django</h1>')


def blog_view(request):
    blog = models.Post.objects.all()
    return render(request, 'blog.html', {'blog': blog})


def post_detailview(request, id):
    post_id = get_object_or_404(models.Post, id=id)
    return render(request, 'post_detail.html', {'post_id': post_id})


#Добавление фильма через формы
def create_post_view(request):
    method = request.method
    if method == 'POST':
        form = forms.BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Фильм успешно добавлен!!!</h2>')

    else:
        form = forms.BlogForm()

    return render(request, 'add_post.html', {'form': form})


def update_post_view(request, id):
    blog_object = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        form = forms.BlogForm(instance=blog_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2> Фильм успешно обновлен!</h2>')
    else:
        form = forms.BlogForm(instance=blog_object)

    return render(request, 'update_post.html', {
                                                    'form': form,
                                                    'object': blog_object
                                                   })


def delete_post_view(request, id):
    show_object = get_object_or_404(models.Post, id=id)
    show_object.delete()
    return HttpResponse('<h2>Фильм успешно удален</h2>')
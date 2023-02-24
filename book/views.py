from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def bookview(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})


def book_detailview(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})


#Добавление фильма через формы
def create_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Фильм успешно добавлен!!!</h2>')

    else:
        form = forms.BookForm()

    return render(request, 'add_book.html', {'form': form})


def update_book_view(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2> Фильм успешно обновлен!</h2>')
    else:
        form = forms.BookForm(instance=book_object)

    return render(request, 'update_book.html', {
                                                    'form': form,
                                                    'object': book_object
                                                   })


def delete_book_view(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    show_object.delete()
    return HttpResponse('<h2>Фильм успешно удален</h2>')
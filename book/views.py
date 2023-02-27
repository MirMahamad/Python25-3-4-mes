from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


#вывод полной информации по id


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)


#Добавление фильма через формы

class BookCreateView(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/book/'


    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


class BookUpdateView(generic.UpdateView):
    template_name = 'update_book.html'
    form_class = forms.BookForm
    success_url = "/book/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    template_name = 'confirm_delete_book.html'
    success_url = '/book/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)















# def bookview(request):
#     book = models.Book.objects.all()
#     return render(request, 'book.html', {'book': book})
#
#
# def book_detailview(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     return render(request, 'book_detail.html', {'book_id': book_id})
#
#
# #Добавление фильма через формы
# def create_book_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>Фильм успешно добавлен!!!</h2>')
#
#     else:
#         form = forms.BookForm()
#
#     return render(request, 'add_book.html', {'form': form})
#
#
# def update_book_view(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2> Фильм успешно обновлен!</h2>')
#     else:
#         form = forms.BookForm(instance=book_object)
#
#     return render(request, 'update_book.html', {
#                                                     'form': form,
#                                                     'object': book_object
#                                                    })
#
#
# def delete_book_view(request, id):
#     show_object = get_object_or_404(models.Book, id=id)
#     show_object.delete()
#     return HttpResponse('<h2>Фильм успешно удален</h2>')
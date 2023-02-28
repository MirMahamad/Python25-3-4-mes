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


'''Комментарий под книгой'''
class CreateCommentView(generic.CreateView):
    template_name = 'form_for_comment.html'
    form_class = forms.CommentForm
    queryset = models.RatingBook.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCommentView, self).form_valid(form=form)
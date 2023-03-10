from django.db import models


class Book(models.Model):
    LIST = (
        ('AUTOBIOGRAPHY', 'AUTOBIOGRAPHY'),
        ('SPEECH', 'SPEECH'),
        ('ESSAY', 'ESSAY'),
        ('BIOGRAPHY', 'BIOGRAPHY'),
        ('DIARY', 'DIARY')
    )

    title = models.CharField('Название книги', max_length=100, null=True)
    description = models.TextField("Описание книги", null=True)
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колличество книг', null=True)
    genre = models.CharField(max_length=100, choices=LIST, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class RatingBook (models.Model):

    RATING = (
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    )

    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_object')
    rate = models.IntegerField('Оценка: ', choices=RATING)
    comment = models.TextField('Комментарий: ')
    created_date = models.DateTimeField(auto_now_add=True)
from django.db import models


class TVShow(models.Model):
    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('MELODRAMME', 'MELODRAMME')
    )

    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма', null=True)
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колличество фильмов', null=True)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)
    video = models.URLField(null=True)
    price = models.PositiveIntegerField('Цена билета', null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

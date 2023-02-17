from django.db import models


class Post(models.Model):
    LIST = (
        ('NEWS', 'NEWS'),
        ('OLD', 'OLD'),
    )

    title = models.CharField('Название поста', max_length=100, null=True)
    description = models.TextField("Дополнитенльное описание поста", null=True)
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колличество статей в посте', null=True)
    genre = models.CharField(max_length=100, choices=LIST, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

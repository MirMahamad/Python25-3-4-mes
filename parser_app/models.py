from django.db import models


class CarParser(models.Model):
    title_url = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    price = models.CharField(max_length=100, null=True)
    info = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title_text


from django.contrib import admin
from . import models

admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.Cloth)
admin.site.register(models.Tag)

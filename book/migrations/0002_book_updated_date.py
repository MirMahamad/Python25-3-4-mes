# Generated by Django 4.1.6 on 2023-02-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

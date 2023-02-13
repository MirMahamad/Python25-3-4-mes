from django.urls import path
from . import views


urlpatterns = [
    path('book_link', views.book_view, name='books'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('book', views.bookview, name='book'),
    path('book/<int:id>/', views.book_detailview, name='details'),
    path('book/<int:id>/update/', views.update_book_view, name='update'),
    path('book/<int:id>/delete/', views.delete_book_view, name='delete'),
    path('add-book/', views.create_book_view, name='create'),
]

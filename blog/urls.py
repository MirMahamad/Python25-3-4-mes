from django.urls import path
from . import views


urlpatterns = [
    path('hello_link/', views.hello_view, name='hello'),
    path('blog_link', views.blog_view, name='blog')
]
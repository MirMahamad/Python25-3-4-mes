from django.urls import path
from . import views


urlpatterns = [
    path('hello_link/', views.hello_view, name='hello'),
    path('blog', views.blog_view, name='blog'),
    path('blog/<int:id>/', views.post_detailview, name='details'),
    path('blog/<int:id>/update/', views.update_post_view, name='update'),
    path('blog/<int:id>/delete/', views.delete_post_view, name='delete'),
    path('add-blog/', views.create_post_view, name='create'),
]
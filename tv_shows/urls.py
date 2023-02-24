from django.urls import path
from . import views


urlpatterns = [
    path('tvshow/', views.tv_showview, name='show'),
    path('tvshow/<int:id>/', views.tv_show_detailview, name='details'),
    path('tvshow/<int:id>/update/', views.update_tv_show_view, name='update'),
    path('tvshow/<int:id>/delete/', views.delete_tv_show_view, name='delete'),
    path('add-tv/', views.create_tv_show_view, name='create'),
]
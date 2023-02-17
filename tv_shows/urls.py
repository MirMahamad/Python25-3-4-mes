from django.urls import path
from . import views

urlpatterns = [
    path('tvshow/', views.tv_showview, name='show'),
    path('tvshow/<int:id>/', views.tv_show_detailview, name='details'),
]
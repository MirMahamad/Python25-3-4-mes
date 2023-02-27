from django.urls import path
from . import views


urlpatterns = [
    path('tvshow/', views.TvShowView.as_view(), name='show'),
    path('tvshow/<int:id>/', views.TvShowDetailView.as_view(), name='details'),
    path('tvshow/<int:id>/update/', views.TvShowUpdateView.as_view(), name='update'),
    path('tvshow/<int:id>/delete/', views.TvShowDeleteView.as_view(), name='delete'),
    path('add-tv/', views.TvShowCreateView.as_view(), name='create'),
]
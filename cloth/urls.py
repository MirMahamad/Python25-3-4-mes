from django.urls import path
from . import views

urlpatterns = [
    path("cloths/", views.ClothListView.as_view(), name="cloths"),
    path("cloths/<int:id>/", views.ClothDetailView.as_view(), name="detail"),
    path("add-order/", views.OrderCreateView.as_view(), name="add"),
]

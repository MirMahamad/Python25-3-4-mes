from django.urls import path
from . import views

app_name = 'parse'
urlpatterns = [
    path('car-list/', views.ParserView.as_view(), name='car-list'),
    path('parsing/', views.ParserFormView.as_view(), name='parser-car'),
]
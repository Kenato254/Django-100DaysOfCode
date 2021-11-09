from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = "theater"

urlpatterns = [
    path('', views.list_countries_view, name="list-view"),
    path('search/', views.search_view, name="search-view"),
    path('dogs/', views.dogs_view, name='dogs-view'),
    path('dogs/<int:dog_pk>/', views.dog_detail_view, name='dog-view'),
    path('dogs/<int:dog_pk>/copy/', views.dog_copy_view, name='dog-view-copy'),
    path('dogs/<int:dog_pk>/delete/', views.dog_delete_view, name='dog-delete'),

]

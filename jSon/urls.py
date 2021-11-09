from django.urls import path

from . import views

app_name = 'jSon'

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('authors-create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/', views.AuthorView.as_view(), name='author-detail'),
]

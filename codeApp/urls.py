from django.contrib.auth.decorators import login_required
from django.urls import path

app_name = 'codeApp'

from . import views

urlpatterns = [
    path('book-list/', views.BookListView.as_view(), name='view-books'),
    path('add-book/', views.BookAddView.as_view(), name='add-book'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='view-book'),    
    
    # This approach applies the decorator on a per-instance basis. 
    path('book/<int:pk>/update/', login_required(views.BookUpdateView.as_view()), name='update-book'),    
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete-book'),    
    path('contact-me/', views.ContactFormView.as_view(), name='contact-form'),
    path('json/', views.JsonTemplateView.as_view(), name='json-data'),
    # path('book-pag/<int:pk>/', views.BokListView.as_view(), name='book-pag'),
    # path('authors-list/', views.BokListView.as_view(), name='authors-list')
]

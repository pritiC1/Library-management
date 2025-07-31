from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book-list'),
    path('add/', views.add_book, name='add-book'),
    path('edit/<int:id>/', views.edit_book, name='edit-book'),
    path('delete/<int:id>/', views.delete_book, name='delete-book'),
    path('search/', views.search_books, name='search-books'),
]

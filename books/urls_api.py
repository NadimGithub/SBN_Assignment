from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateAPI.as_view(), name='api_books_list_create'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDeleteAPI.as_view(), name='api_book_detail'),
]

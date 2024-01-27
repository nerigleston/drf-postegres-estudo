from django.urls import path, re_path
from .views import (
    get_author_list, create_author, get_author_detail, update_author, delete_author,
    get_book_list, create_book, get_book_detail, update_book, delete_book, filter_book_date, filter_book_daterange
)

urlpatterns = [
    path('authors/', get_author_list, name='author-list'),
    path('authors/<int:pk>/', get_author_detail, name='author-detail'),
    path('authors/create/', create_author, name='author-create'),
    path('authors/update/<int:pk>/', update_author, name='author-update'),
    path('authors/delete/<int:pk>/', delete_author, name='author-delete'),

    path('books/', get_book_list, name='book-list'),
    path('books/<int:pk>/', get_book_detail, name='book-detail'),
    path('books/create/', create_book, name='book-create'),
    path('books/update/<int:pk>/', update_book, name='book-update'),
    path('books/delete/<int:pk>/', delete_book, name='book-delete'),
    path('books/filter/', filter_book_date, name='book-filter'),
    path('books/filter_range/', filter_book_daterange, name='book-filter-range'),
]

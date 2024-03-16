from django.urls import path
from . import views

app_name = 'books_api'  # views of this app indentified by this name

urlpatterns = [
        path('books', views.getBooks, name='books'),
        path('books/<int:bookId>', views.getBookById, name='getBookById'),
]

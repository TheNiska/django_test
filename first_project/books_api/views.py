from django.shortcuts import render
from .models import Book
from django.forms.models import model_to_dict
from django.http import JsonResponse, QueryDict

# request_body = QueryDict(request.body)

# Create your views here.
def getBooks(request):
    books = Book.objects.all()
    return JsonResponse(model_to_dict(books))


def getBookById(request, bookId):
    book = Book.objects.get(pk=bookId)
    return JsonResponse(model_to_dict(book))

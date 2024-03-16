from django.shortcuts import render
from .models import Book
from django.forms.models import model_to_dict
from django.http import JsonResponse, QueryDict
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json


# Create your views here.
@csrf_exempt
def getBooks(request):
    if request.method == 'POST':
        if request.content_type == "application/json":
            data = json.loads(request.body.decode("utf-8"))
        else:
            data = request.POST

        title = data.get('title')
        author = data.get('author')
        price = data.get('price')
        inventory = data.get('inventory')

        new_book = Book(
            title=title, author=author, price=price, inventory=inventory
        )

        try:
            new_book.save()
        except IntegrityError:
            return JsonResponse({'error': 'true'}, status=400)
        else:
            return JsonResponse(model_to_dict(new_book), status=201)

    elif request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse(
            {"books": list(books)},
            json_dumps_params={'ensure_ascii': False}
        )


@csrf_exempt
def getBookById(request, bookId):
    if request.method == 'GET':
        book = Book.objects.get(pk=bookId)
        return JsonResponse(
            model_to_dict(book),
            json_dumps_params={'ensure_ascii': False}
        )

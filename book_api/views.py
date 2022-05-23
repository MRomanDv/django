from django.shortcuts import render
from book_api.models import Book
from django.http import JsonResponse

# Create your views here. can be a class or function will return data from specific endpoint, view is responsable for the Logic to create and return the data

def books_list(request):
    books = Book.objects.all() #Complex Data
    books_python = list(books.values()) #form of list python data structure
    return JsonResponse({
        "books":books_python
    })
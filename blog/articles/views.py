from django.shortcuts import render
from django.http import Http404
from .models import Book


def archive(request):
    return render(request, 'archive.html', {"books": Book.objects.all()})


def get_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return render(request, 'book.html', {"book": book})
    except Book.DoesNotExist:
        raise Http404
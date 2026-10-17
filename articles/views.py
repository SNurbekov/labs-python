from django.shortcuts import render
from .models import Book


def archive(request):
    return render(request, 'archive.html', {"books": Book.objects.all()})
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Book


def archive(request):
    return render(request, 'archive.html', {"books": Book.objects.all()})


def get_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return render(request, 'book.html', {"book": book})
    except Book.DoesNotExist:
        raise Http404


def create_book(request):
    if request.user.is_anonymous:
        raise Http404("Только авторизованные пользователи могут добавлять книги")

    if request.method == "POST":
        form = {
            'title': request.POST.get("title", ""),
            'author': request.POST.get("author", ""),
            'genre': request.POST.get("genre", ""),
            'deposit': request.POST.get("deposit", ""),
            'rent_price': request.POST.get("rent_price", ""),
        }

        if form["title"] and form["author"]:
            book = Book.objects.create(
                title=form["title"],
                author=form["author"],
                genre=form["genre"],
                deposit=form["deposit"] or 0,
                rent_price=form["rent_price"] or 0
            )
            return redirect('get_book', book_id=book.id)
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_book.html', {'form': form})
    else:
        return render(request, 'create_book.html', {})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if not username or not password:
            return render(request, 'register.html', {'error': 'Заполните все поля'})

        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {'error': 'Пользователь с таким именем уже есть'})
        except User.DoesNotExist:
            User.objects.create_user(username, '', password)
            return redirect('login')
    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('archive')
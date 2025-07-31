from django.shortcuts import render
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


def index(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books, 'query': query})

from django.shortcuts import render, redirect
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt  # (use only during development; remove in production)
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        published_date = request.POST['published_date']
        genre = request.POST['genre']
        
        # Save to database
        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            published_date=published_date,
            genre=genre
        )
        return redirect('/')  # redirect to book list

    return render(request, 'books/add.html')


@csrf_exempt
def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.published_date = request.POST['published_date']
        book.genre = request.POST['genre']
        book.save()
        return redirect('/')

    return render(request, 'books/edit.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('/')



def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})
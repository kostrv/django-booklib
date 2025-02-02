from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else []
    return render(request, 'books/search.html', {'books': books})

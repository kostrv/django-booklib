from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def search_books(request):
    query = request.GET.get('q', '').strip().lower()  # Приводим запрос к нижнему регистру

    if query:
        words = query.split()  # Разбиваем строку запроса на отдельные слова
        filters = Q()

        for word in words:
            filters |= Q(title__icontains=word)  

        books = Book.objects.filter(filters)
    else:
        books = []

    return render(request, 'books/search.html', {'books': books})
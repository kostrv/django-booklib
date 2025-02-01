from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Страница с подробностями книги
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

# Поиск книг
def search_books(request):
    query = request.GET.get("q")
    books = Book.objects.filter(title__icontains=query) if query else []
    return render(request, "search.html", {"books": books})

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_catalog.settings')
django.setup()

from books.models import Author, Book, BookDetail

# Данные для авторов
authors_data = [
    {'id': 1, 'name': 'Harper Lee', 'img_src': 'https://example.com/harper_lee.jpg', 'years_of_age': '89', 'bio': 'American novelist widely known for "To Kill a Mockingbird."', 'works': 'To Kill a Mockingbird'},
    {'id': 2, 'name': 'George Orwell', 'img_src': 'https://example.com/george_orwell.jpg', 'years_of_age': '46', 'bio': 'English novelist famous for "1984" and "Animal Farm."', 'works': '1984, Animal Farm'},
    {'id': 3, 'name': 'Jane Austen', 'img_src': 'https://example.com/jane_austen.jpg', 'years_of_age': '41', 'bio': 'English novelist known for "Pride and Prejudice."', 'works': 'Pride and Prejudice'},
]

# Данные для книг
books_data = [
    {'title': 'To Kill a Mockingbird', 'author_id': 1, 'img_src': 'https://example.com/mockingbird.jpg', 'publication_date': '1960-07-11', 'short_desc': 'A novel about racial injustice.'},
    {'title': '1984', 'author_id': 2, 'img_src': 'https://example.com/1984.jpg', 'publication_date': '1949-06-08', 'short_desc': 'Dystopian novel about totalitarianism.'},
    {'title': 'Pride and Prejudice', 'author_id': 3, 'img_src': 'https://example.com/pride_prejudice.jpg', 'publication_date': '1813-01-28', 'short_desc': 'A classic novel of manners.'},
]

book_details_data = [
    {'book_title': 'To Kill a Mockingbird', 'description': 'A novel that explores themes of racism and morality in the Deep South.'},
    {'book_title': '1984', 'description': 'A story about a dystopian future where the government watches every move.'},
    {'book_title': 'Pride and Prejudice', 'description': 'A romantic novel that also critiques social class and gender roles.'},
]

# Добавляем авторов
for author in authors_data:
    Author.objects.create(**author)

# Добавляем книги
for book in books_data:
    author = Author.objects.get(id=book['author_id'])
    Book.objects.create(title=book['title'], author=author, img_src=book['img_src'], publication_date=book['publication_date'], short_desc=book['short_desc'])

# Добавляем описание книг
for detail in book_details_data:
    book = Book.objects.get(title=detail['book_title'])
    BookDetail.objects.create(book=book, description=detail['description'])

print('Database updated successfully!')

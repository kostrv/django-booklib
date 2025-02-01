from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    img_src = models.URLField(blank=True, null=True)
    years_of_age = models.CharField(max_length=50)  # Если не только числа
    bio = models.TextField()
    works = models.TextField(blank=True, null=True)  # Перечень книг через запятую

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    img_src = models.URLField(blank=True, null=True)
    publication_date = models.DateField()
    short_desc = models.TextField()

    def __str__(self):
        return self.title


class BookDetail(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()

    def __str__(self):
        return f'Details of {self.book.title}'
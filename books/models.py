from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, db_collation='NOCASE')  
    img_src = models.URLField(blank=True, null=True)
    years_of_age = models.CharField(max_length=50)  
    bio = models.TextField()
    works = models.TextField(blank=True, null=True) 

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, db_collation='NOCASE')  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  
    img_src = models.URLField(blank=True, null=True)
    publication_date = models.DateField()
    short_desc = models.TextField()

    class Meta:
        db_table = 'book'
        ordering = ['title']

    def __str__(self):
        return self.title


class BookDetail(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='details')
    description = models.TextField(db_collation='NOCASE')

    class Meta:
        db_table = 'book_detail'

    def __str__(self):
        return f'Details of {self.book.title}'

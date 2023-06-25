from django.db import models
from books.models import Book

def get_books_in_store(store_id):
    store_books = Book.objects.filter(store_id=store_id)
    return store_books

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    book_list = models.ManyToManyField("Book", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

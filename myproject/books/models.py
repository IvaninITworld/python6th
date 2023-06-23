from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    publication_date = models.DateField()

    # CASCADE 를 사용하려고 하면 자동완성으로 () 가 붙는데 사용하지 않는 이유는 뭘까 ?
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name
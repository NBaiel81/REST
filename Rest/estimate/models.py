from django.db import models
from api.models import Book

class Rate(models.Model):
    star =models.PositiveIntegerField()
    book =models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.book.title

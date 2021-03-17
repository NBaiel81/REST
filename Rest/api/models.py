from django.contrib.auth.models import User
from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=200)
    year =models.DateField()
    description=models.CharField(max_length=200)
    abbr=models.CharField(max_length=20,unique=True)
    book_file=models.FileField(blank=True)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL, blank=True, null=True,related_name='books')
    price=models.PositiveIntegerField(verbose_name=None)
    sale=models.BooleanField(default=False)
    sale_amount=models.PositiveIntegerField()
    def __str__(self):
        return self.title

class Author(models.Model):
    name=models.CharField(max_length=200)
    bio=models.TextField(blank=True)
    date_birth=models.DateField()
    date_death=models.DateField(blank=True,null=True)
    country=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Order(models.Model):
    statuses=(
        ('pending','pending'),
        ('finished','finished'),
    )
    quantity=models.PositiveIntegerField(default=1)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    book=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    date_create=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=200, null=True)
    status=models.CharField(choices=statuses,max_length=20, default='pending')
    payment_type = models.CharField(choices=(
        ('card','card'),
        ('cash','cash'),
    ),max_length=10,default='cash')

    def __str__(self):
        return f'заказ с товаром: {self.book.title}'




from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','description','year']

class AuthorSerializer(serializers.ModelSerializer):
    books=BookSerializer(many=True)
    class Meta:
        model=Author
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user','book','address','date_create','status']
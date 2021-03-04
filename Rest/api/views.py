from django.shortcuts import render
from rest_framework.response import Response

from .serializers import *
from rest_framework import views

class UserView(views.APIView):
    def get(self,request,*args,**kwargs):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)
class BookView(views.APIView):
    def get(self,request,*args,**kwargs):
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'Ok'})

class AuthorView(views.APIView):
    def get(self,request,*args,**kwargs):
        authors=Author.objects.all()
        serializer=AuthorSerializer(authors,many=True)
        return Response(serializer.data)



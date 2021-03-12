from rest_framework import status
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from api.models import Book
from .serializers import BookDetailSerializer, CommentCreateSerializer


class BookDetailView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            book = Book.objects.get(id=kwargs['book_id'])
        except Book.DoesNotExist:
            return Response({"data":"NotFound"},status=status.HTTP_404_NOT_FOUND)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            book=Book.objects.get(id=kwargs['book_id'])
            text = serializer.data.get('text')
            Comment.objects.create(book=book,text=text,user=request.user)
            return Response({"data":"comment create succesfully!"})
        return Response(serializer.errors)


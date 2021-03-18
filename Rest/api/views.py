from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
from rest_framework import views
from datetime import datetime
from django.utils import timezone


class UserView(views.APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class BookView(views.APIView):
    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'Ok'})


class AuthorView(views.APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class OrderAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "id": 1,
            "user": 1,
            "book": 2,
            "address": "Lalaland",
            "date_created": "2021-03-05T16:49:28.748633+06:00",
            "status": "pending"
        })

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ModifyOrder(views.APIView):
    def put(self, request, order_id):
        order = Order.objects.get(id=order_id)
        hours=timezone.now().hour * 60
        minutes=timezone.now().minute
        result1=hours+minutes
        result2=(order.date_create.hour*60)+order.date_create.minute
        serializer=OrderSerializer(order,data=request.data)
        print(abs(result1-result2))
        if serializer.is_valid():
            if abs(result1-result2)<=5:
                serializer.save()
                return Response({"data":"OK!!!"})
            else:
                return Response({"data":"Time is up!"})
        return Response(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, order_id):

        order = Order.objects.get(id=order_id)
        order.delete()
        return Response({'data': 'successfully deleted!'})


class MyOrderAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class BookDemoView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(abbr=kwargs['abbr'])
        except Book.DoesNotExist:
            return Response({'data': 'Book not found!'}, status=status.HTTP_404_NOT_FOUND)
        demo = book.book_file.open()
        return Response({'demo': demo.read()[:5]})

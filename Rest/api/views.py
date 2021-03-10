from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
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

    def post(self,request,*args,**kwargs):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ModifyOrder(views.APIView):
    def put(self,request,order_id):
        order=Order.objects.get(id=order_id)
        print(request.data)
        serializer=OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,order_id):
        order=Order.objects.get(id=order_id)
        order.delete()
        return Response({'data':'successfully deleted!'})

class MyOrderAPIView(views.APIView):
    def get(self,request,*args,**kwargs):
        orders=Order.objects.filter(user=request.user)
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data)
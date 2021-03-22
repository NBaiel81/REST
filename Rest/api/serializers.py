from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField()
    class Meta:
        model=Book
        fields=['id','title','description','year','author']

class AuthorSerializer(serializers.ModelSerializer):
    books=BookSerializer(many=True)
    class Meta:
        model=Author
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    promo=serializers.SerializerMethodField()
    class Meta:
        model=Order
        fields=['id','user','book','address','date_create','status','payment_type','quantity','total_price','promo','promocode']

    def get_total_price(self,obj):
        total_price = 0
        try:
            total_price +=obj.quantity * obj.book.price
            if obj.address is None:
                obj.address = obj.user.profile.address
            obj.total_price = total_price
            if obj.payment_type == 'card':
                if obj.user.profile.wallet >= total_price:
                    obj.user.profile.wallet -=total_price
                    obj.user.profile.save()
                    obj.save()
                else:
                    obj.delete()
                    raise ValidationError("Not enough money!")
            else:
                obj.save()
            return total_price
        except AttributeError:
            return 0
    def get_promo(self,obj):
        promocode = 'LALA'
        if obj.promocode ==promocode:
            obj.total_price -=100
            obj.save()


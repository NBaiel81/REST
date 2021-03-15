from estimate.serializers import RateModelSerializer
from .models import Comment
from api.models import Book
from rest_framework.serializers import ModelSerializer,Serializer, CharField, SerializerMethodField
from estimate import *
from estimate.models import Rate
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class BookDetailSerializer(ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id','title','description','year','author','comment_set']

class CommentCreateSerializer(Serializer):
    text= CharField(allow_blank=False)

class BookDetailSerializer(ModelSerializer):
    rate_set=RateModelSerializer(many=True)
    comment_set=CommentSerializer(many=True)
    avg_rate=SerializerMethodField()
    class Meta:
        model=Book
        fields=['id','title','description','price','year','author','comment_set','rate_set','avg_rate']

    def get_avg_rate(self,obj):
        count=0
        total_sum=0
        for rate in obj.rate_set.all():
            count+=1
            total_sum+=rate.star
            print(count)
            print(total_sum)
            print('eee')
        return round(total_sum/count,1)






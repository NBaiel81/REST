from rest_framework import serializers


class RateSerializer(serializers.Serializer):
    star = serializers.IntegerField(min_value=0,max_value=10)
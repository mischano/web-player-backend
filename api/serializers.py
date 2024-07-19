from rest_framework import serializers

class MyDataSerializer(serializers.Serializer):
    key1 = serializers.CharField(max_length=100)
    key2 = serializers.IntegerField()
    
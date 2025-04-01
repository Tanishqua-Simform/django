from rest_framework import serializers
from .models import BookModel
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=BookModel.objects.all())

    class Meta:
        model = User
        fields = "__all__"
from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')




class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'bio')



class BookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ("id", "name", "title", "category", "author")




##############  Nested serializer
# class BookSerializers(serializers.ModelSerializer):
#     category = CategorySerializers()
#     author = AuthorSerializers()
#
#     class Meta:
#         model = Book
#         fields = ('id', 'name', 'title', 'category', 'author')

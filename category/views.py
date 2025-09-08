from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView, Response
from rest_framework import status




class CategoryAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AuthorAPI(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializers(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):  # xatoni DRF o‘zi qaytaradi
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class BookAPI(APIView):
    def get(self, request):
        books = Book.objects.select_related("author", "category")  # optimizatsiya
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

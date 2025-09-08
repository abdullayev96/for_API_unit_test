from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView, Response
from rest_framework.generics import *
from rest_framework import status
from rest_framework import filters



class CategoryAPI(APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializers(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Kategoriya topilmadi!"},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AuthorAPI(APIView):
    def get(self, request):
        try:
            author = Author.objects.all()
            serializer = AuthorSerializers(author, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Author  topilmadi!"},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db import models
from basemodel.models import BaseModel



class Category(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name



class Author(BaseModel):
    full_name = models.CharField(max_length=200, verbose_name="Author nomi")
    bio = models.TextField()

    def __str__(self):
        return self.full_name



class Book(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Kitob nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.TextField(verbose_name="Kitob haqida")


    def __str__(self):
        return self.name



from django.urls import path
from .views import *



urlpatterns = [
    path('category', CategoryAPI.as_view(), name="category-list"),
    path('author', AuthorAPI.as_view(), name="author-list")

]
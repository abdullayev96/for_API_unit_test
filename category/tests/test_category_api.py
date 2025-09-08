from rest_framework.test import APITestCase
from rest_framework import status
from category.models import Book, Category, Author
from category.serializers import *
from django.urls import reverse


class CategoryAPITest(APITestCase):

    def setUp(self):
        self.list_url = reverse("category-list")  # urls.py da name berib qo‘ysangiz yaxshi
        self.category = Category.objects.create(name="History")

    def test_get_categories(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "History")

    def test_create_category(self):
        data = {"name": "Science"}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.last().name, "Science")

    def test_create_invalid_category(self):
        data = {"name": ""}  # invalid
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)



class BookAPITest(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Fantasy")
        self.author = Author.objects.create(full_name="J.R.R. Tolkien", bio="LOTR muallifi")
        self.book = Book.objects.create(
            name="The Hobbit",
            title="The Hobbit haqida",
            category=self.category,
            author=self.author
        )
        self.url = reverse("book-list")

    # ✅ To‘g‘ri GET request
    def test_get_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ✅ To‘g‘ri POST request
    def test_create_book(self):
        data = {
            "name": "The Lord of the Rings",
            "title": "Epic fantasy trilogy",
            "category": self.category.id,
            "author": self.author.id
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)


    # ❌ Invalid POST: bo‘sh name
    def test_create_book_invalid_name(self):
        data = {
            "name": "",
            "title": "Epic fantasy",
            "category": self.category.id,
            "author": self.author.id
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)

    # ❌ Invalid POST: noto‘g‘ri category
    def test_create_book_invalid_category(self):
        data = {
            "name": "Invalid Book",
            "title": "Test",
            "category": 999,  # mavjud bo‘lmagan id
            "author": self.author.id
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("category", response.data)

    # ❌ Invalid POST: noto‘g‘ri author
    def test_create_book_invalid_author(self):
        data = {
            "name": "Invalid Book",
            "title": "Test",
            "category": self.category.id,
            "author": 999  # mavjud bo‘lmagan id
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("author", response.data)




# class BookAPITest(APITestCase):
#
#     def setUp(self):
#         self.category = Category.objects.create(name="Fantasy")
#         self.author = Author.objects.create(full_name="J.R.R. Tolkien", bio="LOTR muallifi")
#         self.book = Book.objects.create(
#             name="The Hobbit",
#             title="The Hobbit haqida",
#             category=self.category,
#             author=self.author
#         )
#         self.url = reverse("book-list")  # BookAPI URL name
#
#     def test_get_books(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]["name"], self.book.name)
#
#     def test_create_book(self):
#         data = {
#             "name": "The Lord of the Rings",
#             "title": "Epic fantasy trilogy",
#             "category": self.category.id,
#             "author": self.author.id
#         }
#         response = self.client.post(self.url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Book.objects.count(), 2)
#         self.assertEqual(Book.objects.last().name, "The Lord of the Rings")
#
#     def test_create_invalid_book(self):
#         data = {
#             "name": "",  # bo'sh name invalid
#             "title": "Invalid book",
#             "category": self.category.id,
#             "author": self.author.id
#         }
#         response = self.client.post(self.url, data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn("name", response.data)
#

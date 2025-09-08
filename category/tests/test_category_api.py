from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from category.models import Category


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

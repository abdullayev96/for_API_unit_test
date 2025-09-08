from django.test import TestCase
from category.models import *
from category.serializers import *


class CategorySerializerTest(TestCase):
    def test_missing_name(self):
        data = {}
        serializer = CategorySerializers(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_empty_name(self):
        data = {"name": ""}
        serializer = CategorySerializers(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    # def test_invalid_expectation(self):       ###  Error holat
    #     data = {"name": ""}  # bu invalid bo‘lishi kerak
    #     serializer = CategorySerializers(data=data)
    #     # ❌ ataylab noto‘g‘ri kutilgan natija
    #     self.assertTrue(serializer.is_valid())

    def test_create_category(self):
        data = {"name": "Science"}
        serializer = CategorySerializers(data=data)
        self.assertTrue(serializer.is_valid())
        category = serializer.save()
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, "Science")

    def test_update_category(self):
        category = Category.objects.create(name="History")
        data = {"name": "World History"}
        serializer = CategorySerializers(category, data=data)
        self.assertTrue(serializer.is_valid())
        updated_category = serializer.save()
        self.assertEqual(updated_category.name, "World History")




class AuthorSerializerTest(TestCase):
    def test_missing_name(self):
        data = {"bio": "Some bio"}
        serializer = AuthorSerializers(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("full_name", serializer.errors)

    def test_empty_name(self):
        data = {"full_name": "", "bio": "Some bio"}
        serializer = AuthorSerializers(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("full_name", serializer.errors)

    def test_create_author(self):
        data = {"full_name": "Science", "bio": "Bigg"}
        serializer = AuthorSerializers(data=data)
        self.assertTrue(serializer.is_valid())
        author = serializer.save()
        self.assertIsInstance(author, Author)
        self.assertEqual(author.full_name, "Science")

    def test_update_author(self):
        author = Author.objects.create(full_name="History", bio="old")
        data = {"full_name": "World History", "bio": "All"}
        serializer = AuthorSerializers(author, data=data)
        self.assertTrue(serializer.is_valid())
        updated_author = serializer.save()
        self.assertEqual(updated_author.full_name, "World History")
        self.assertEqual(updated_author.bio, "All")

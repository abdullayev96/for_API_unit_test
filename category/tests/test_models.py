# library/tests/test_models.py
from django.test import TestCase
from category.models import Category, Author, Book



class CategoryModelTest(TestCase):
    def test_str_method(self):
        category = Category.objects.create(name="Science")
        self.assertEqual(str(category), "Science")



class AuthorModelTest(TestCase):
    def test_str_method(self):
        author = Author.objects.create(
            full_name="J.K. Rowling",
            bio="Harry Potter kitoblari muallifi"
        )
        self.assertEqual(str(author), "J.K. Rowling")



class BookModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fantasy")
        self.author = Author.objects.create(full_name="J.R.R. Tolkien", bio="LOTR muallifi")

    def test_str_method(self):
        book = Book.objects.create(
            name="The Hobbit",
            title="The Hobbit haqida",
            category=self.category,
            author=self.author
        )
        self.assertEqual(str(book), "The Hobbit")

    def test_relationships(self):
        book = Book.objects.create(
            name="The Lord of the Rings",
            title="Epik fantasy trilogiya",
            category=self.category,
            author=self.author
        )

        # Category orqali kitobni olish
        self.assertIn(book, self.category.books.all())

        # Author orqali kitobni olish
        self.assertIn(book, self.author.books.all())

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from apps.books.models import Book, BookCopy


class BookAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.book_payload = {
            "isbn": "123456789",
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "genre": "NON_FICTION"
            }

        self.book = Book.objects.create(**self.book_payload)

    def test_create_book_success(self):
        self.book_payload["isbn"] = "101112131415"
        response = self.client.post("/api/v1/books/", self.book_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_missing_title(self):
        payload = {
            "isbn": "12345678910",
            "author": "Test",
            "genre": "SELF_HELP"
        }
        response = self.client.post("/api/v1/books/", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_response = {
                                "title": [
                                    "This field is required."
                                ]
                            }
        self.assertEqual(response.json(), expected_response)

    def test_get_all_books(self):
        response = self.client.get("/api/v1/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_get_single_book(self):
        response = self.client.get(f"/api/v1/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existing_book(self):
        response = self.client.get("/api/v1/books/9999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        expected_result = {
            "detail": "No Book matches the given query."
        }
        self.assertEqual(response.json(), expected_result)

    def test_update_book(self):
        payload = {
            "isbn": "123456789",
            "title": "Updated Title",
            "author": "James Clear",
            "genre": "SELF_HELP"
        }
        response = self.client.put(f"/api/v1/books/{self.book.id}/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(f"/api/v1/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bulk_update_books(self):
        book2 = Book.objects.create(
            title="Deep Work",
            author="Cal Newport",
            genre="SELF_HELP"
        )

        payload = [
            { "id": self.book.id, "genre": "FICTION" },
            { "id": book2.id, "author": "Alex Xu Sr" }
            ]

        response = self.client.patch("/api/v1/books/bulk-update/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        book2.refresh_from_db()

        self.assertEqual(self.book.genre, "FICTION")
        self.assertEqual(book2.author, "Alex Xu Sr")

    def test_create_book_copy(self):
        payload = {
            "barcode" : "123456789",
            "book": self.book.id,
            "status": "AVAILABLE"
        }

        response = self.client.post("/api/v1/books/book-copies/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookCopy.objects.count(), 1)

    def test_get_book_copies(self):
        BookCopy.objects.create(barcode= "123456789", book=self.book, status="AVAILABLE")

        response = self.client.get("/api/v1/books/book-copies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_bulk_update_book_copies(self):
        copy1 = BookCopy.objects.create(barcode= "123456789", book=self.book, status="AVAILABLE")
        copy2 = BookCopy.objects.create(barcode= "987654321", book=self.book, status="AVAILABLE")

        payload = [
              { "id": copy1.id, "status": "LOST" },
              { "id": copy2.id, "status": "ISSUED" }
            ]

        response = self.client.patch(
            "/api/v1/books/book-copies/bulk-update/",
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        copy1.refresh_from_db()
        copy2.refresh_from_db()

        self.assertEqual(copy1.status, "LOST")
        self.assertEqual(copy2.status, "ISSUED")

    def test_delete_book_copy(self):
        copy1 = BookCopy.objects.create(barcode="123456789", book=self.book, status="AVAILABLE")
        copy2 = BookCopy.objects.create(barcode="987654321", book=self.book, status="AVAILABLE")
        payload = {
            "copy_barcodes": [
                copy1.barcode,
                copy2.barcode
            ]
        }
        response = self.client.delete(f"/api/v1/books/copies/", payload)
        expected = {'message': {'copies_deleted': 2, 'books_deleted': 1}}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)
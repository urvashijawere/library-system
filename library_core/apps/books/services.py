from itertools import batched

from django.db import transaction
from .models import Book, BookCopy


class BookService:

    @staticmethod
    @transaction.atomic
    def add_book_copies(validated_data):
        isbn = validated_data["isbn"]
        title = validated_data.get("title")
        author = validated_data.get("author")
        genre = validated_data.get("genre")
        copies_data = validated_data["copies"]

        # Lock or get book safely
        book, created = Book.objects.get_or_create(isbn=isbn, defaults={"title": title, "author": author,
                                                                        "genre": genre})

        copies = [BookCopy(barcode=copy["barcode"], book=book) for copy in copies_data]

        BookCopy.objects.bulk_create(copies)
        return {
            "book_created": created,
            "copies_added": len(copies)
        }

    @staticmethod
    @transaction.atomic
    def delete_book_copies(validated_data):
        # Lock rows for safety
        barcodes = validated_data["copy_barcodes"]
        copies = (BookCopy.objects.select_for_update().filter(barcode__in=barcodes).select_related("book"))
        if not copies.exists():
            raise ValueError("No matching copies found.")

        # Track affected books
        books = set(copy.book for copy in copies)
        deleted_count = copies.count()
        copies.delete()
        deleted_books = 0

        # Check remaining copies per book
        for book in books:
            remaining = BookCopy.objects.filter(book=book).count()
            if remaining == 0:
                book.delete()
                deleted_books += 1

        return {"copies_deleted": deleted_count, "books_deleted": deleted_books}
from django.db import models


class Book(models.Model):
    """
    Book details
    """
    class Genre(models.TextChoices):
        FICTION = "FICTION", "Fiction"
        NON_FICTION = "NON_FICTION", "Non-Fiction"
        MYSTERY = "MYSTERY", "Mystery"
        FANTASY = "FANTASY", "Fantasy"
        SCIENCE_FICTION = "SCIENCE_FICTION", "Science Fiction"
        BIOGRAPHY = "BIOGRAPHY", "Biography"
        HISTORY = "HISTORY", "History"
        ROMANCE = "ROMANCE", "Romance"
        HORROR = "HORROR", "Horror"
        SELF_HELP = "SELF_HELP", "Self Help"

    isbn = models.CharField(max_length=20, db_index=True, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=20, choices=Genre, default=Genre.FICTION)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookCopy(models.Model):
    """
    Physical copy of a book in library,
    we can have multiple copies of same book
    """

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        ISSUED = "ISSUED", "Issued"
        RESERVED = "RESERVED", "Reserved"
        LOST = "LOST", "Lost"

    barcode = models.CharField(max_length=255, unique=True)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="copies",)
    status = models.CharField(max_length=20, choices=Status, default=Status.AVAILABLE, db_index=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

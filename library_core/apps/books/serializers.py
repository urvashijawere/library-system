from rest_framework import serializers
from .models import Book, BookCopy

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = "__all__"


class BookCopyInputSerializer(serializers.Serializer):
    barcode = serializers.CharField(max_length=255)


class AddBookCopiesSerializer(serializers.Serializer):
    isbn = serializers.CharField(max_length=20)
    title = serializers.CharField(max_length=255, required=False)
    author = serializers.CharField(max_length=255, required=False)
    genre = serializers.CharField(max_length=20, required=False)
    copies = BookCopyInputSerializer(many=True)

    def validate(self, data):
        barcodes = [copy["barcode"] for copy in data["copies"]]

        # Check duplicate barcodes inside request
        if len(barcodes) != len(set(barcodes)):
            raise serializers.ValidationError(
                "Duplicate barcodes found in request payload."
            )

        # Exist in database
        existing = BookCopy.objects.filter(barcode__in=barcodes).values_list("barcode", flat=True)
        if existing:
            raise serializers.ValidationError(
                f"These barcodes already exist: {list(existing)}"
            )
        return data

class DeleteBookCopySerializer(serializers.Serializer):
    copy_ids = serializers.ListField(child=serializers.IntegerField(), allow_empty=False)
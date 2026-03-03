from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from .models import IssueRecord


class IssueService:

    @staticmethod
    @transaction.atomic
    def issue_book(validated_data):
        book_copy = validated_data["book_copy"]
        member_id = validated_data["member_id"]
        due_date = validated_data["due_date"]

        # Prevent issuing already issued book
        if book_copy.status == "ISSUED":
            raise ValidationError("Book copy is already issued")

        record = IssueRecord.objects.create(book_copy=book_copy, member_id=member_id, due_date=due_date,
                                            status=IssueRecord.IssueStatus.ACTIVE)
        book_copy.status = "ISSUED"
        book_copy.save(update_fields=["status"])

        return {"message": "Book issued successfully", "record_id": record.id}


    @staticmethod
    @transaction.atomic
    def return_book(validated_data):
        book_copy = validated_data["book_copy"]
        member_id = validated_data["member_id"]

        record = IssueRecord.objects.select_related("book_copy").get(member_id=member_id, book_copy=book_copy,
                                                                     status=IssueRecord.IssueStatus.ACTIVE)

        if record.status != IssueRecord.IssueStatus.ACTIVE:
            raise ValidationError("Book is not currently issued")

        record.status = IssueRecord.IssueStatus.RETURNED
        record.returned_at = timezone.now()
        record.save(update_fields=["status", "returned_at"])

        book_copy = record.book_copy
        book_copy.status = "AVAILABLE"
        book_copy.save(update_fields=["status"])

        return {"message": "Book returned successfully"}
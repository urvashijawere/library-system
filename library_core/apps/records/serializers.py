from rest_framework import serializers
from .models import IssueRecord
from apps.books.models import BookCopy, Book
from apps.users.models import MemberProfile


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title"]


class BookCopyMiniSerializer(serializers.ModelSerializer):
    book = BookMiniSerializer()

    class Meta:
        model = BookCopy
        fields = ["id", "barcode", "book"]


class MemberMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberProfile
        fields = ["id", "membership_id"]


class IssueSerializer(serializers.ModelSerializer):
    book_copy = BookCopyMiniSerializer()
    member = MemberMiniSerializer()

    class Meta:
        model = IssueRecord
        fields = [
            "id",
            "book_copy",
            "member",
            "issued_at",
            "due_date",
            "returned_at",
            "status",
            "fine_amount",
        ]


class IssueRecordSerializer(serializers.Serializer):
    barcode = serializers.CharField()
    membership_id = serializers.CharField()
    due_date = serializers.DateTimeField()

    def validate(self, data):
        try:
            copy = BookCopy.objects.get(barcode=data["barcode"])
        except BookCopy.DoesNotExist:
            raise serializers.ValidationError("Book copy not found")

        if copy.status != "AVAILABLE":
            raise serializers.ValidationError("Book copy is not available")

        try:
            member = MemberProfile.objects.get(membership_id=data["membership_id"])
        except MemberProfile.DoesNotExist:
            raise serializers.ValidationError("Member not found")

        data["book_copy"] = copy
        data["member"] = member
        return data


class ReturnRecordSerializer(serializers.Serializer):
    book_copy_id = serializers.IntegerField()
    member_id = serializers.IntegerField()

    def validate(self, data):
        try:
            copy = BookCopy.objects.get(id=data["book_copy_id"])
        except BookCopy.DoesNotExist:
            raise serializers.ValidationError("Book copy not found")

        data["book_copy"] = copy
        return data
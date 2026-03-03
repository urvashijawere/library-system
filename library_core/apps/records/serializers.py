from rest_framework import serializers
from .models import IssueRecord
from apps.books.models import BookCopy


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueRecord
        fields = "__all__"


class IssueRecordSerializer(serializers.Serializer):
    book_copy_id = serializers.IntegerField()
    member_id = serializers.IntegerField()
    due_date = serializers.DateTimeField()

    def validate(self, data):
        try:
            copy = BookCopy.objects.get(id=data["book_copy_id"])
        except BookCopy.DoesNotExist:
            raise serializers.ValidationError("Book copy not found")

        if copy.status != "AVAILABLE":
            raise serializers.ValidationError("Book copy is not available")

        data["book_copy"] = copy
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
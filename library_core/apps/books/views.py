from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Book, BookCopy
from apps.records.models import IssueRecord
from .serializers import BookSerializer, BookCopySerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Exact filtering
    filterset_fields = ['author', 'title']

    # Search (partial match)
    search_fields = ['title', 'author']

    # Ordering
    ordering_fields = ['title', 'created_at']


class BookCopyViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

    # Exact filtering
    filterset_fields = ['created_at', 'status']

    # Search (partial match)
    search_fields = ['created_at', 'status']

    # Ordering
    ordering_fields = ['created_at', 'status']

    @action(detail=True, methods=["post"])
    def issue(self, request, pk=None):
        copy = self.get_object()

        if copy.status != "AVAILABLE":
            return Response(
                {"error": "Book not available"},
                status=status.HTTP_400_BAD_REQUEST
            )

        member_id = request.data.get("member")
        due_date = request.data.get("due_date")

        IssueRecord.objects.create(
            member_id=member_id,
            book_copy=copy,
            due_date=due_date
        )

        copy.status = "ISSUED"
        copy.save()

        return Response({"message": "Book issued successfully"})

    @action(detail=True, methods=["post"])
    def returnbook(self, request, pk=None):
        copy = self.get_object()

        record = IssueRecord.objects.filter(
            book_copy=copy,
            status="ISSUED"
        ).first()

        if not record:
            return Response({"error": "No active borrow record"})

        record.returned_at = timezone.now()
        record.status = "RETURNED"
        record.save()

        copy.status = "AVAILABLE"
        copy.save()

        return Response({"message": "Book returned successfully"})
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Book, BookCopy
from .services import BookService
from apps.records.models import IssueRecord
from .serializers import BookSerializer, BookCopySerializer, AddBookCopiesSerializer, DeleteBookCopySerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filterset_fields = ['author', 'title', 'isbn', 'genre']
    search_fields = ['title', 'author', 'isbn', 'genre']
    ordering_fields = ['title', 'created_at']

    @action(detail=False, methods=["patch"], url_path="bulk-update")
    def bulk_update(self, request):
        data = request.data

        if not isinstance(data, list):
            return Response({"error": "Expected a list of objects"}, status=status.HTTP_400_BAD_REQUEST)

        updated_objects = []
        with transaction.atomic():
            for item in data:
                try:
                    obj = Book.objects.get(id=item["id"])
                except Book.DoesNotExist:
                    continue

                serializer = self.get_serializer(obj, data=item, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                updated_objects.append(serializer.data)

        return Response(updated_objects, status=status.HTTP_200_OK)


class AddBookCopiesAPIView(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = AddBookCopiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = BookService.add_book_copies(serializer.validated_data)
        return Response(result, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def delete(self, request):
        serializer = DeleteBookCopySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = BookService.delete_book_copies(serializer.validated_data)
        return Response({"message": message}, status=200)


class BookCopyViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

    filterset_fields = ['created_at', 'status', 'barcode']
    search_fields = ['created_at', 'status', 'barcode']
    ordering_fields = ['created_at', 'status', 'barcode']

    @action(detail=False, methods=["patch"], url_path="bulk-update")
    def bulk_update(self, request):
        data = request.data

        if not isinstance(data, list):
            return Response({"error": "Expected a list of objects"}, status=status.HTTP_400_BAD_REQUEST)

        updated_objects = []
        with transaction.atomic():
            for item in data:
                try:
                    obj = BookCopy.objects.get(id=item["id"])
                except BookCopy.DoesNotExist:
                    continue

                serializer = self.get_serializer(obj, data=item, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                updated_objects.append(serializer.data)

        return Response(updated_objects, status=status.HTTP_200_OK)

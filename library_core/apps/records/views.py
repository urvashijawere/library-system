from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.db import transaction
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import IssueRecord
from .services import IssueService
from apps.books.models import BookCopy
from .serializers import IssueRecordSerializer, IssueSerializer, ReturnRecordSerializer


class IssueRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = IssueRecord.objects.all()
    serializer_class = IssueSerializer  # for create only

    filterset_fields = ['issued_at', 'due_date', 'returned_at', 'status']
    search_fields = ['issued_at', 'due_date', 'returned_at', 'status']
    ordering_fields = ['issued_at', 'due_date', 'returned_at', 'status']

    @action(detail=False, methods=["post"], url_path="issue")
    def issue(self, request):
        serializer = IssueRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = IssueService.issue_book(serializer.validated_data)

        return Response(result, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"], url_path="return")
    def return_book(self, request):
        serializer = ReturnRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = IssueService.return_book(serializer.validated_data)
        return Response(result, status=status.HTTP_200_OK)

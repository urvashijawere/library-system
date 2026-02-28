from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import IssueRecord
# from .services import borrow_book
from .serializers import IssueRecordSerializer


# @permission_required("records.can_borrow_book")
# def borrow_view(request, barcode):
#     book_copy = get_object_or_404(BookCopy, barcode=barcode)
#     member_profile = request.user.member_profile
#
#     record = borrow_book(member_profile, book_copy)
#
#     return JsonResponse({"status": "Borrowed", "record_id": record.id})


class IssueRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    queryset = IssueRecord.objects.all()
    serializer_class = IssueRecordSerializer

    # Exact filtering
    filterset_fields = ['issued_at', 'due_date', 'returned_at', 'member', 'status']

    # Search (partial match)
    search_fields = ['issued_at', 'due_date', 'returned_at']

    # Ordering
    ordering_fields = ['issued_at', 'due_date', 'returned_at']
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from apps.books.models import BookCopy
from .services import borrow_book


@permission_required("records.can_borrow_book")
def borrow_view(request, barcode):
    book_copy = get_object_or_404(BookCopy, barcode=barcode)
    member_profile = request.user.member_profile

    record = borrow_book(member_profile, book_copy)

    return JsonResponse({"status": "Borrowed", "record_id": record.id})
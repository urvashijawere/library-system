from datetime import date, timedelta
# from books.models import BookCopy
from .models import IssueRecord


# def borrow_book(member_profile, book_copy):
#     if not book_copy.status == BookCopy.status.AVAILABLE:
#         raise Exception("Book not available")
#
#     book_copy.status = BookCopy.status.ISSUED
#     book_copy.save()
#
#     return IssueRecord.objects.create(
#         member=member_profile,
#         book_copy=book_copy,
#         due_date=date.today() + timedelta(days=14)
#     )
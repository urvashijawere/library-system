from rest_framework.views import APIView
from rest_framework.response import Response
from apps.books.models import Book
from apps.users.models import MemberProfile
from apps.records.models import IssueRecord


class DashboardView(APIView):

    def get(self, request):
        data = {
            "total_books": Book.objects.count(),
            "active_members": MemberProfile.objects.count(),
            "books_issued": IssueRecord.objects.filter(status="ACTIVE").count(),
        }
        return Response(data)
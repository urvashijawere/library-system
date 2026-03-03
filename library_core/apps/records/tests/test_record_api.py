from datetime import datetime

from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch

from apps.books.models import Book, BookCopy
from apps.users.models import MemberProfile, User


class IssueAPITestCase(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            isbn="123",
            title="Test Book",
            author="Author"
        )
        self.copy = BookCopy.objects.create(
            book=self.book,
            status="AVAILABLE"
        )
        self.user = User.objects.create(
            username="Monica",
            email="monica.smith@example.com",
            password="pass123"
        )
        self.member = MemberProfile.objects.create(
            user=self.user,
            membership_id="M1"
        )

    def test_issue_book_api(self):
        response = self.client.post(
            "/api/v1/records/issue/",
            {
                "book_copy_id": self.copy.id,
                "member_id": self.member.id,
                "due_date": timezone.now()
            }
        )
        expected_result = {'message': 'Book issued successfully', 'record_id': 2}
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected_result)

        # Reissue same book
        response = self.client.post(
            "/api/v1/records/issue/",
            {
                "book_copy_id": self.copy.id,
                "member_id": self.member.id,
                "due_date": timezone.now()
            }
        )
        expected_response_json = {
            "non_field_errors": [
                "Book copy is not available"
            ]
        }
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), expected_response_json)

    @patch("apps.records.services.timezone.now")
    def test_get_issue_book_api(self, mock_now):
        mock_now.return_value = timezone.make_aware(
            datetime(2026, 1, 1, 10, 0, 0)
        )
        #issue book
        response = self.client.post(
            "/api/v1/records/issue/",
            {
                "book_copy_id": self.copy.id,
                "member_id": self.member.id,
                "due_date": timezone.now()
            }
        )
        self.assertEqual(response.status_code, 201)

        # check records
        expected_response_json = [{'id': 1,
                                   'due_date': '2026-01-01T10:00:00Z',
                                   'issued_at': '2026-01-01T10:00:00Z',
                                   'returned_at': None, 'status': 'ACTIVE',
                                   'fine_amount': '0.00',
                                   'book_copy': self.copy.id,
                                   'member': self.member.id}]

        response = self.client.get("/api/v1/records/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response_json)

    @patch("apps.records.services.timezone.now")
    def test_return_book_api(self, mock_now):
        mock_now.return_value = timezone.make_aware(
            datetime(2026, 1, 1, 10, 0, 0)
        )
        #issue book
        response = self.client.post(
            "/api/v1/records/issue/",
            {
                "book_copy_id": self.copy.id,
                "member_id": self.member.id,
                "due_date": timezone.now()
            }
        )
        self.assertEqual(response.status_code, 201)

        # return book
        response = self.client.post(
            "/api/v1/records/return/",
            {
                "book_copy_id": self.copy.id,
                "member_id": self.member.id
            }
        )
        self.assertEqual(response.status_code, 200)

        # check records
        expected_response_json = [{'id': 3,
                                   'due_date': '2026-01-01T10:00:00Z',
                                   'issued_at': '2026-01-01T10:00:00Z',
                                   'returned_at': '2026-01-01T10:00:00Z', 'status': 'RETURNED',
                                   'fine_amount': '0.00',
                                   'book_copy': self.copy.id,
                                   'member': self.member.id}]

        response = self.client.get("/api/v1/records/")
        self.assertEqual(response.status_code, 200)
        resp = response.json()
        self.assertEqual(resp[0]['status'], 'RETURNED')
        self.assertEqual(resp[0]['returned_at'], '2026-01-01T10:00:00Z')
        self.assertEqual(resp, expected_response_json)

    def test_return_book_api_failure(self):
        with self.assertRaises(Exception):
            self.client.post(
                "/api/v1/records/return/",
                {
                    "book_copy_id": self.copy.id,
                    "member_id": self.member.id
                }
            )

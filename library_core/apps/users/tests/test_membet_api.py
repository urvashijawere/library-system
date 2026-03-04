from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.users.models import MemberProfile, User


class MemberViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.member_url = "/api/v1/users/members/"  # adjust if needed

        self.user = User.objects.create_user(
            username="member1",
            password="pass123"
        )

        self.member = MemberProfile.objects.create(
            user=self.user,
            membership_id="M001"
        )

    def test_create_member(self):
        data = {
            "username":"Alex",
            "password":"12345678",
            "membership_id": "M002",
            "id_proof_type": "Adhaaar",
            "id_proof_number": "qwuytduqw1233"
        }

        response = self.client.post(self.member_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MemberProfile.objects.count(), 2)

    def test_list_members(self):
        response = self.client.get(self.member_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_member(self):
        url = f"{self.member_url}{self.member.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["membership_id"], "M001")

    def test_update_member(self):
        url = f"{self.member_url}{self.member.id}/"
        data = {"membership_id": "M999"}

        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.member.refresh_from_db()
        self.assertEqual(self.member.membership_id, "M999")

    def test_delete_member(self):
        url = f"{self.member_url}{self.member.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MemberProfile.objects.count(), 0)
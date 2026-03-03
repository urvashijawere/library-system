from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.users.models import MemberProfile, User


class UserViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_url = "/api/v1/users/"  # adjust if needed

        self.user = User.objects.create_user(
            username="john",
            password="pass123",
            email="john@test.com"
        )

    def test_create_user(self):
        data = {
            "username": "alice",
            "password": "pass123",
            "email": "alice@test.com"
        }

        response = self.client.post(self.user_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_list_users(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_user(self):
        url = f"{self.user_url}{self.user.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "john")

    def test_update_user(self):
        url = f"{self.user_url}{self.user.id}/"
        data = {"email": "updated@test.com"}

        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, "updated@test.com")

    def test_delete_user(self):
        url = f"{self.user_url}{self.user.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    
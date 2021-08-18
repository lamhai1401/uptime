"""
User model test
"""
from django.test import TestCase

from .models import User

# Create your tests here.


class TestUser(TestCase):
    """
    Testing user api
    """

    @classmethod
    def setUp(cls):  # Create a user
        testuser1 = User.objects.create_user(
            email="lamhai@gmail.com", password="abc123"
        )
        testuser1.save()

    def test_login(self):
        """
        Testing user login
        """
        response = self.client.post(
            "/rest-auth/login/",
            {"email": "lamhai@gmail.com", "password": "abc123"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("key", response.json(), "Not contain key")

    def test_logout(self):
        """
        Testing user logout
        """
        response = self.client.post(
            "/rest-auth/login/",
            {"email": "lamhai@gmail.com", "password": "abc123"},
            format="json",
        )

        headers = {"HTTP_AUTHORIZATION": f"Token {response.json()['key']}"}
        response = self.client.post(
            "/rest-auth/logout/",
            **headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_auth(self):
        """
        Testing user auth after login
        """
        response = self.client.post(
            "/rest-auth/login/",
            {"email": "lamhai@gmail.com", "password": "abc123"},
            format="json",
        )

        headers = {"HTTP_AUTHORIZATION": f"Token {response.json()['key']}"}
        response = self.client.get(
            "/test_auth/",
            **headers,
        )
        self.assertEqual(response.status_code, 200)

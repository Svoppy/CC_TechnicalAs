from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User

class UserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        payload = {"name":"Dias", "email": "kazihanovdias@gmail.com","age":20}
        res = self.client.post("/api/v1/users/", payload, format="json")
        self.assertEqual(res.status_code,201)
        self.assertTrue(User.objects.filter(email="kazihanovdias@gmail.com").exists())
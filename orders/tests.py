from django.test import TestCase
from rest_framework.test import APIClient
from users.models import User

class OrderApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name="Anuar", email="duisenov@gmail.com", age = 21)

    def test_create_order_ok(self):
        payload = {"title": "T", "description": "", "user": self.user.id}
        res = self.client.post("/api/v1/orders", payload,format = "json")
        self.assertEqual(res.status_code, 201)

    def test_create_order_user_missing(self):
        payload = {"title": "T","description": "", "user": 9999}
        res = self.client.post("/api/v1/orders/", payload, format="json")
        self.assertEqual(res.status_code, 400)
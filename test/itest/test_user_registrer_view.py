import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.test.client import JSON_CONTENT_TYPE_RE


class TestUserRegisterRestView(APITestCase):
    def setUp(self) -> None:
        pass

    def test_user_register(self):
        body = json.dumps({
            'user': {
                'username': 'Test',
                'first_name': 'Te',
                'last_name': 'St',
                'email': 'te@st.com',
                'password': '1'
            },
            'site': {
                'name': 'Some'
            }
        })
        response = self.client.post('/api/v1/user/register/', data=body, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        users = User.objects.filter(username='Test')
        self.assertEqual(1, users.count())
        response = self.client.post('/api/v1/user/register/', data=body, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

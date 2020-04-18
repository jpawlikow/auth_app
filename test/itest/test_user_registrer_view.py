import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserRegisterRestView(APITestCase):
    def setUp(self) -> None:
        self.body = json.dumps({
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

    def test_user_register_status_code(self):
        response = self.client.post('/api/v1/user/register/', data=self.body, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_register_created_object(self):
        self.client.post('/api/v1/user/register/', data=self.body, content_type='application/json')
        users = User.objects.filter(username='Test')
        self.assertEqual(1, users.count())

    def test_user_register_two_same_requests(self):
        self.client.post('/api/v1/user/register/', data=self.body, content_type='application/json')
        response = self.client.post('/api/v1/user/register/', data=self.body, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_register_bad_request_content(self):
        response = self.client.post('/api/v1/user/register/', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

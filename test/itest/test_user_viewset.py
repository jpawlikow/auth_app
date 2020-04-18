from account_app.testing.factories import UserFactory
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserViewSet(APITestCase):
    def setUp(self) -> None:
        user = UserFactory(username='User', password='Test')
        UserFactory(username='User2', password='Test')
        response = self.client.post('/auth/token/', {'username': user.username, 'password': 'Test'})
        access_token = response.data['access']
        self.auth_headers = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)}

    def test_request_without_authorization(self):
        response = self.client.get('/api/v1/user/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_with_authorization(self):
        response = self.client.get('/api/v1/user/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list(self):
        response = self.client.get('/api/v1/user/', **self.auth_headers)
        self.assertEqual(len(response.data), 2)

    def test_user_list_content(self):
        response = self.client.get('/api/v1/user/', **self.auth_headers)
        for item in response.data:
            self.assertIn(item['username'], ['User', 'User2'])

    def test_user_by_id(self):
        response = self.client.get('/api/v1/user/1/', **self.auth_headers)
        self.assertEqual(response.data['id'], 1)

    def test_user_by_wrong_id(self):
        response = self.client.get('/api/v1/user/3/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

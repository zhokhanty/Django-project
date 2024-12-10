from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserAPITests(APITestCase):
    def test_register_api(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password1': 'ComplexPassword123!',
            'password2': 'ComplexPassword123!',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

    def test_login_api(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Profile
from scores.models import Team


class UserViewsTests(TestCase):
    register_url = reverse('register')
    login_url = reverse('login')
    profile_url = reverse('profile')
    logout_url = reverse('logout')

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Check if the user already has a profile, and create it only if necessary
        if not hasattr(self.user, 'profile'):
            self.profile = Profile.objects.create(user=self.user)
        else:
            self.profile = self.user.profile

    def test_register_view(self):
        # Ensure the registration form is rendered correctly
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

        # Simulate successful registration and expect a redirect to the login page
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'ComplexPassword123!',
            'password2': 'ComplexPassword123!',
        })
        if response.context and 'form' in response.context:
            print(response.context['form'].errors)  # Отладка ошибок формы

        self.assertRedirects(response, self.login_url)  # Редирект после регистрации
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())
    def test_profile_view(self):
        # Ensure the user is logged in before accessing the profile
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_logout_view(self):
        # Логинимся перед выходом
        self.client.login(username='testuser', password='testpassword')

        # Проверка логаута
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, reverse('sport_list'))  # После логаута редирект на список спорта
        self.assertNotIn('_auth_user_id', self.client.session)  # Проверка, что сессия пользователя была удалена

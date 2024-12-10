from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Profile

class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')

    def test_profile_creation(self):
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.user.username, 'testuser')
        self.assertIsNotNone(profile.created_at)

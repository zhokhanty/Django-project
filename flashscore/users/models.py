from django.contrib.auth.models import User
from django.db import models
from scores.models import Team
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('journalist', 'Journalist')
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f'{self.user.username} Profile'
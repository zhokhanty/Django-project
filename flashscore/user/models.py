from django.db import models

class Profile:
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.user_name
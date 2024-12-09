from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    content = models.TextField(verbose_name="content")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="author")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date of created")

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
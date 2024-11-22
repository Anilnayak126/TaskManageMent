# models.py

from django.db import models
from django.contrib.auth.models import User
import uuid

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class OAuthSettings(models.Model):
    google_client_id = models.CharField(max_length=255)
    google_client_secret = models.CharField(max_length=255)

    def __str__(self):
        return f"Google OAuth Settings"

class Invitation(models.Model):
    email = models.EmailField(unique=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.email

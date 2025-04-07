from django.db import models
from django.contrib.auth.models import User
import uuid
import base64


def generate_short_key():
    uid = uuid.uuid4()
    key = base64.urlsafe_b64encode(uid.bytes).decode('utf-8').rstrip('=\n')[:6]
    return key

class Link(models.Model):
    original_url = models.URLField(unique=True)
    key = models.CharField(max_length=6, unique=True, default=generate_short_key)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return f"{self.original_url} -> {self.shortened_url}"

    def __str__(self):
        return f"{self.key} -> {self.original_url}"
    
class LinkClick(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='clicks')
    clicked_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Click on {self.link.key} at {self.clicked_at}"
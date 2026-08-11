import string
import random
from django.conf import settings
from django.db import models


def generate_short_code():
    characters = string.ascii_letters + string.digits   # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=6))


class Link(models.Model):
    original_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='links',
        null=True,
        blank=True
    )
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"



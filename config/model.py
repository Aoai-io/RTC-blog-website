from django.db import models
from django.urls import reverse


class SubscribeEmail(models.Model):
    """Model definition for SubscribeEmail."""

    # TODO: Define fields here

    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        """Meta definition for SubscribeEmail."""

        verbose_name = "SubscribeEmail"
        verbose_name_plural = "SubscribeEmails"

    def __str__(self):
        """Unicode representation of SubscribeEmail."""
        return f"{self.email}"  # TODO

    def get_absolute_url(self):
        return reverse("home")

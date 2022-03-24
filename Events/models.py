from django.db import models
from django.utils.translation import gettext_lazy as _
from profiles.models import Profile
import uuid

# Create your models here.

province = (
    ("Al Anbar", "Al Anbar"),
    ("Babylon", "Babylon"),
    ("Baghdad", "Baghdad"),
    ("Basra", "Basra"),
    ("Dhi Qar", "Dhi Qar"),
    ("Al-Qādisiyyah", "Al-Qādisiyyah"),
    ("Diyala", "Diyala"),
    ("Duhok", "Duhok"),
    ("Erbil", "Erbil"),
    ("Halabja", "Halabja"),
    ("Karbala", "Karbala"),
    ("Kirkuk", "Kirkuk"),
    ("Maysan", "Maysan"),
    ("Muthanna", "Muthanna"),
    ("Najaf", "Najaf"),
    ("Nineveh", "Nineveh"),
    ("Saladin", "Saladin"),
    ("Sulaymaniyah", "Sulaymaniyah"),
    ("Wasit", "Wasit"),
)


class Event(models.Model):
    """Model definition for Event."""

    # TODO: Define fields here
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=500)
    cover = models.ImageField(upload_to="events/", null=True)
    description = models.TextField(_("Description"))
    date = models.DateField(_("Date"))
    from_date_time = models.DateTimeField(_("From Date Time"))
    to_date_time = models.DateTimeField(_("To Date Time"))
    city = models.CharField(_("City"), choices=province, max_length=70)
    address = models.CharField(_("Address"), max_length=600)
    total_slot = models.IntegerField(_("Total Slot"))
    speakers = models.ManyToManyField(Profile, related_name="events")

    created_at = models.DateTimeField(_("Created At"),auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(_("Updated At"),auto_now=True, null=True, blank=True)

    class Meta:
        """Meta definition for Event."""

        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        """Unicode representation of Event."""
        return self.title

    def get_absolute_url(self):
        """Return absolute url for Event."""
        return "home"

    # TODO: Define custom methods here

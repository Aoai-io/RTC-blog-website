from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):

    image = models.ImageField(upload_to="editors_profile/", null=True, blank=True)
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

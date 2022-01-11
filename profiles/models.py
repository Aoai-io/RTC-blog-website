from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Profile(models.Model):

    image = models.ImageField( upload_to='editors_profile/', null=True, blank=True)
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE)

    
from django.db import models

# Create your models here.


class OurCompany(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title


class Support(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title

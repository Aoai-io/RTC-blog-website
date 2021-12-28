from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=CASCADE)
    cover = models.ImageField(upload_to='articles/', null=True, blank=True)
    body = models.TextField()


    def __str__(self) -> str:
        return self.title[:50]

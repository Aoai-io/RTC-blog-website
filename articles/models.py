from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.db.models.fields import DateField
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.user", on_delete=CASCADE)
    cover = models.ImageField(upload_to="articles/", null=True, blank=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.title[:50]


class Comment(models.Model):
    # TODO: make a review text field
    # TODO: make a rating field
    # TODO: make a refrance to user that write comment
    # TODO: make a refrance to the article that have the comment
    pass

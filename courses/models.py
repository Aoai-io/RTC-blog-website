from django.db import models
from django.db.models.deletion import CASCADE
from django_quill.fields import QuillField

# from django.contrib.auth.models import User
from instructors.models import Instructor

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title).title()


class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return str(self.title).title()


language = (
    ("Arabic", "Arabic"),
    ("English", "English"),
)

skill_level = (
    ("Beginner", "Beginner"),
    ("Advance", "Advance"),
)

certificate = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class Course(models.Model):
    title = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor, on_delete=CASCADE)
    cover = models.ImageField(upload_to="courses/", blank=True, null=True)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )
    old_price = models.PositiveBigIntegerField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    body = QuillField()
    duration = models.DurationField(
        null=True, blank=True, help_text="Input Duration In Seconds"
    )
    lectures = models.PositiveSmallIntegerField(null=True, blank=True)
    language = models.CharField(
        max_length=50, choices=language, default=1, null=True, blank=True
    )
    skill_level = models.CharField(
        max_length=50, choices=skill_level, default=1, null=True, blank=True
    )
    certificate = models.CharField(
        max_length=50, choices=certificate, default=1, null=True, blank=True
    )

    deadline = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )

    # TODO add to course requirements field
    # TODO add to course (What you'll learn) field

    # TODO add to courses model this fields
    # ? Duration -> O.K
    # ? Lectures -> O.K
    # ? Language -> O.K
    # ? Skill level -> O.K
    # ? Deadline -> O.K
    # ? Certificate -> O.K
    # ? Enrolled

    def __str__(self):
        return str(self.title[:50]).title


class Review(models.Model):
    # TODO: make a review text field
    # TODO: make a rating field

    # TODO: make a refrance to user that write the review
    # TODO: make a refrance to the course that have the review
    pass

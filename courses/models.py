# import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from instructors.models import Instructor
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title).title()


class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='sub_category')

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
gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)
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


class Course(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor, on_delete=CASCADE, related_name='courses')
    cover = models.ImageField(upload_to="courses/", blank=True, null=True)
    sub_category = models.ForeignKey(
        SubCategory, related_name='course',on_delete=models.CASCADE, null=True, blank=True
    )
    old_price = models.PositiveBigIntegerField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    body = RichTextField(blank=True, null=True)
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

    def __str__(self) -> str:
        return self.title[:50]


class Review(models.Model):
    # TODO: make a review text field
    # TODO: make a rating field

    # TODO: make a refrance to user that write the review
    # TODO: make a refrance to the course that have the review

    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    review_title = models.TextField("Review Title", null=True, blank=True)
    review_content = models.TextField("Review Content", null=True, blank=True)

    # ? 5 star - 252
    # ? 4 star - 124
    # ? 3 star - 40
    # ? 2 star - 29
    # ? 1 star - 33

    # ? (5*252 + 4*124 + 3*40 + 2*29 + 1*33) / (252+124+40+29+33) = 4.11 and change

    def __str__(self):
        return self.review_title


class DataCollector(models.Model):
    """Model definition for DataCollector."""

    gender = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    # TODO: Define fields here
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(blank=True, null=True, max_length=15)

    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    gender = models.CharField(
        max_length=50,
        choices=gender,
    )

    street_address = models.CharField(max_length=250, blank=True, null=True)
    province = models.CharField(max_length=50, choices=province)
    city = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        """Meta definition for DataCollector."""

        verbose_name = "DataCollector"
        verbose_name_plural = "DataCollectors"

    def __str__(self):
        """Unicode representation of DataCollector."""
        return str(self.first_name + " " + self.last_name)

    def get_absolute_url(self):
        return reverse("home")

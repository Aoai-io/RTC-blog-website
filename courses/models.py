
from django.db import models
from django.db.models.deletion import CASCADE
from django_quill.fields import QuillField
from instructors.models import Instructor
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# from django.contrib.auth.models import User

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

    # TODO: Define fields here
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(blank=True, null=True, region="IQ")

    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    gender = models.CharField(
        max_length=50,
        choices=gender,
    )

    street_address = models.CharField(max_length=250,  blank=True, null=True)
    province = models.CharField(max_length=50, choices=province)
    city = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        """Meta definition for DataCollector."""

        verbose_name = "DataCollector"
        verbose_name_plural = "DataCollectors"

    def __str__(self):
        """Unicode representation of DataCollector."""
        return str(self.first_name + " " + self.last_name)

    def get_absolute_url(self):
        return reverse('home')
    

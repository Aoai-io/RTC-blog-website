from django.db import models
from django.db.models.deletion import CASCADE
# from django.contrib.auth.models import User
from instructors.models import Instructor

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor,on_delete=CASCADE)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.PositiveBigIntegerField()
    body = models.TextField()

    def __str__(self):
        return self.title[:50]
    


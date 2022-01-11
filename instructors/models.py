from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField( upload_to='instructors/', null=True, blank=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('auth.user', on_delete=CASCADE)
    bio = models.TextField()  


    def __str__(self):
        return self.name
    
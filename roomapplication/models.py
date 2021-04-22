from django.db import models
from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField


# Create your models here.


class Room(models.Model):
    location = models.CharField(max_length=100, blank=False, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.location


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(0)])



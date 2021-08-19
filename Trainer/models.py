from django.db import models
# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=12, blank=True, null = True)
    last_name = models.CharField(max_length=12, blank=True, null = True)
    age = models.PositiveSmallIntegerField(blank=True, null = True)
    gender = models.CharField(max_length=12, blank=True, null = True)
    bio = models.TextField(blank=True, null = True)
    courses = models.CharField(max_length=14, blank=True, null = True)
    email_address = models.EmailField(blank=True, null = True)
    phone_number = models.CharField(max_length=15,blank=True, null = True)
    lesson_duration = models.PositiveSmallIntegerField(blank=True, null = True)
    
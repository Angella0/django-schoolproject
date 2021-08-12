from django.db import models


# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    Age = models.PositiveSmallIntegerField()
    Gender = models.CharField(max_length=12)
    Bio = models.TextField()
    Courses = models.CharField(max_length=14)
    Email_Address = models.EmailField()
    phone_number = models.CharField(max_length=12)
    Salary = models.PositiveBigIntegerField()
    Lesson_Duration = models.PositiveSmallIntegerField()
   
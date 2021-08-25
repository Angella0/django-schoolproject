from django.db import models

# Create your models here.
class CoursesForm(models.Model):
    name = models.CharField(max_length=18, null = True)
    course_code = models.CharField(max_length=12, null = True)
    syllabus=models.CharField(max_length=15, null = True)
    course_trainer=models.CharField(max_length=15, null = True)
    # course_schedule=models.FileField(max_length=30, null = True)
    course_duration=models.CharField(max_length=15, null=True)
    
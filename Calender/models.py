from django.db import models

# Create your models here.
class Calender(models.Model):
    event_name = models.CharField(max_length=12, null = True)
    event_date = models.DateField(null = True)
    event_planner=models.CharField( max_length=15, null=True)
    event_participation=models.DateField( null = True)
    event_duration=models.FileField(max_length=30, null = True)
    course_duration=models.CharField(max_length=15, null=True)
    
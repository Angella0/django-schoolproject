from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    Email_address = models.EmailField()
    Student_id=models.CharField(max_length=15)
    Date_of_enrollment=models.DateField()
    County=models.CharField(max_length=12)
    Medical_report=models.FileField()
    Course_name=models.CharField(max_length=12)
    Roll_number=models.CharField(max_length=15)
    GENDER_CHOICES=(
        (u'M',u'Male'),
        (u'F',u'Feamle'),
        (u'O',u'Other')
    )
    LANGUAGE_CHOICES = (
        (u'L', u'Luganda'),
        (u'E', u'English'),
        (u'K', u'Kiswahili')
    )
    languages = models.CharField(max_length=6, choices=LANGUAGE_CHOICES)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)



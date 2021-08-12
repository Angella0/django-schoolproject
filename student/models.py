from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    
    Roll_number=models.CharField(max_length=15)
    Student_id=models.CharField(max_length=15)
    Course_name=models.CharField(max_length=30)
    # City_Name=models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    Email_address = models.EmailField()
    Date_of_enrollment=models.DateField()
    Medical_report=models.FileField()
    # image = models.ImageField(upload_to='images/')


    GENDER_CHOICES=(
        
        (u'F',u'Female'),
    
    )
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)

    LANGUAGE_CHOICES = (
        (u'L', u'Luganda'),
        (u'E', u'English'),
        (u'K', u'Kiswahili'),
        (u'K', u'Kinyarwanda')
    )
    languages  = models.CharField(max_length=6, choices=LANGUAGE_CHOICES)



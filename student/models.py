from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=12, null = True)
    last_name = models.CharField(max_length=12, null = True)
    roll_number=models.PositiveSmallIntegerField( null = True)
    student_id=models.CharField(max_length=15, null = True)
    course_name=models.CharField(max_length=30, null = True)
    city_name=models.CharField(max_length=15, null=True)
    age = models.PositiveSmallIntegerField( null = True)
    date_of_birth = models.DateField(max_length=20, null = True)
    email_address = models.EmailField( null = True)
    date_of_enrollment=models.DateField( null = True)
    medical_report=models.FileField(upload_to='documents/', null = True)
    # image = models.ImageField(upload_to='images/')


    GENDER_CHOICES=(
        
        (u'F',u'Female'),
        (u'M',u'Male')
    
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES, null=True)

    LANGUAGE_CHOICES = (
        (u'L', u'Luganda'),
        (u'E', u'English'),
        (u'K', u'Kiswahili'),
        (u'K', u'Kinyarwanda')
    )
    languages  = models.CharField(max_length=6, choices=LANGUAGE_CHOICES, null=True)



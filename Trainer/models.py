from django.db import models
# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=12, blank=True, null = True)
    last_name = models.CharField(max_length=12, blank=True, null = True)
    age = models.PositiveSmallIntegerField(blank=True, null = True)
    gender = models.CharField(max_length=12, blank=True, null = True)
    image = models.ImageField(blank=True, upload_to='images/', null = True)
    bio = models.TextField(blank=True, null = True)
    cv = models.FileField(upload_to='documents/', null = True)
    email_address = models.EmailField(blank=True, null = True)
    phone_number = models.CharField(max_length=15,blank=True, null = True)
    lesson_duration = models.PositiveSmallIntegerField(blank=True, null = True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    
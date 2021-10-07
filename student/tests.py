from django import urls
from django.conf.urls import url
from django.http import request
from django.test import TestCase
from django.urls.base import reverse
from .models import Student
import datetime

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student = Student(
        first_name="Angella",
        last_name = "Nambooze", 
        age =22, 
        roll_number = 49, 
        student_id = "70",
        date_of_birth = "1/6/1999",
        email_address = "angellasimbwa@gmail.com",
        city_name = "Entebbe")
    
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())
    
    def test_student_year_of_birth(self):
        current_year = datetime.datetime.now().year
        year = current_year-self.student.age
        self.assertEqual(year, self.student.year_of_birth())

    def tesst_register_student_view(self):
        url = reverse("register_student")
        data = {"first_name": self.student.first_name,
        "last_name": self.student.last_name,
        "age": self.student.age,
        "roll_number": self.student.roll_number,
        "student_id": self.student.student_id,
        "date_of_birth": self.student.date_of_birth,
        "email_address": self.student.email_address,
        "city_name": self.student.city_name}
        request = self.client.post(url,data)
        self.assertEqual(request.status_code,200)
        

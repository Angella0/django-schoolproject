from django.db.models import fields
from rest_framework import serializers
from student.models import Student
from Trainer.models import Trainer
from cal.models import Event
from Courses.models import CoursesForm

class  StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "age", "roll_number")

class TrainerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ("first_name", "last_name", "age")
class CalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "description", "start_time", "end_time")

class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoursesForm
        fields = ("name", "course_code", "syllabus")



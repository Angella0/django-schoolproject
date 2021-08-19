# Generated by Django 3.2.4 on 2021-08-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210813_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='city_Name',
            new_name='city_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_enrollment',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='medical_report',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

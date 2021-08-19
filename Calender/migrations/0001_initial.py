# Generated by Django 3.2.4 on 2021-08-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=12, null=True)),
                ('event_date', models.DateField(null=True)),
                ('event_planner', models.CharField(max_length=15, null=True)),
                ('event_participation', models.DateField(null=True)),
                ('event_duration', models.FileField(max_length=30, null=True, upload_to='')),
                ('course_duration', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
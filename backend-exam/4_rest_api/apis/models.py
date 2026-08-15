from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

class Classroom(models.Model):
    year = models.IntegerField()
    section = models.CharField(max_length=10)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name='classrooms'
        )
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='students',
    )
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classroom = models.ManyToManyField(
        Classroom,
        related_name='teachers',
    )
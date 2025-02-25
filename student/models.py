from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    adm_number = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    courses = models.ManyToManyField("Course", related_name="students", blank=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name    

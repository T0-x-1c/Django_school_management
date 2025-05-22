from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SchoolClass(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

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
    
class Schedule(models.Model):
    DAYS = (
        ('Monday', 'Понеділок'),
        ('Tuesday', 'Вівторок' ),
        ('Wednesday', 'Середа'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятния'),
        ('Saturday', 'Субота'),
        ('Sunday', 'Неділя')
            )   


    date = models.CharField(max_length=20, choices=DAYS)
    start_time = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    schoolclass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'день: {self.date}, година:{self.start_time}, предмет:{self.subject}'
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ImageField(max_length=20)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'оцінка:{self.grade}, предмет:{self.subject}, студент:{self.student}, дата получення:{self.date()}'





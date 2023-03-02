from django.db import models

# Create your models here.
class Student(models.Model):
    studentID = models.CharField(max_length=11, primary_key=True)
    studentName = models.TextField()
    password = models.TextField(default = 'NULL')

class Course(models.Model):
    courseCode = models.CharField(max_length=3, primary_key=True)
    courseName = models.TextField()

class Subject(models.Model):
    courseCode = models.ForeignKey(Course,on_delete=models.CASCADE)
    subjectCode = models.CharField(max_length=7, primary_key=True)
    subjectName = models.TextField()    
    credithours = models.IntegerField()
    lecturerName = models.TextField()

class Assignment(models.Model):
    subjectCode = models.ForeignKey(Subject,on_delete=models.CASCADE)
    assignName = models.TextField()
    dateOut = models.DateField()
    dateIn = models.DateField()
    submit = models.TextField(default = 'UNSUBMITED')
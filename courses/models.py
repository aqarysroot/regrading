from django.db import models
from teachers.models import Teacher
from students.models import Student
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы' 


class Course(models.Model):
    name = models.CharField(max_length=50)
    duration_hours = models.IntegerField()
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    teacher = models.ForeignKey("teachers.Teacher", on_delete=models.CASCADE)
    teaching_days = models.JSONField(
        default={
            'Monday': True,
            'Tuesday': True,
            'Wednesday': True,
            'Thursday': True,
            'Friday': True,
            'Saturday': True,
            'Sunday': True,
        }
    )

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    enrollment_timeout = models.IntegerField()
    everyday_at = models.DateField()

    def __str__(self):
        return f'Студент {self.student.account.username} | Предмет: {self.subject.name}'


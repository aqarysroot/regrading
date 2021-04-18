from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    GENDER = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]

    name = models.CharField(max_length=80)
    gender = models.CharField(max_length=80, blank=True, null=True, choices=GENDER)
    account = models.ForeignKey(User, models.DO_NOTHING, db_column='account', blank=True, null=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты' 

    def __str__(self):
        return f'Студент {self.account.username}'
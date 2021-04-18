from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    account = models.ForeignKey(User, models.DO_NOTHING, db_column='account', blank=True, null=True)
    teaching_experience = models.IntegerField()

    class Meta:
        verbose_name = 'Препод'
        verbose_name_plural = 'Преподы' 
        
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Teacher
from .serailizers import TeacherSerializer
# Create your views here.

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
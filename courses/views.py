from django.shortcuts import render
from rest_framework import viewsets
from .models import Subject, Course, Enrollment
from .serializers import SubjectSerializer, CourseSerializer, EnrollmentSerializer
# Create your views here.

class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentView(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
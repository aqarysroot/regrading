from .models import Subject, Course, Enrollment
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']

class CourseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teaching_days = serializers.JSONField()
    class Meta:
        model = Course
        fields = 'name','subject', 'teacher', 'duration_hours', 'teaching_days'

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    
    class Meta:
        model = Enrollment
        fields = ('course', 'student', 'enrollment_timeout')
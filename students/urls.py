from django.urls import path
from .views import StudentView

urlpatterns = [
    path('',StudentView.as_view({'get':'list'}),
         name='student'),
]
from rest_framework import viewsets
from .models import Teacher, Student  # Імпортуємо моделі, якщо вони існують
from .serializers import TeacherSerializer, StudentSerializer  # Імпортуємо серіалізатори

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


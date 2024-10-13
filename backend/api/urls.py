
from .views import TeacherViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

# Створюємо роутер для автоматичної маршрутизації
router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = router.urls

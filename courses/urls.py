from django.urls import path
from .views import CourseDetailView

urlpatterns = [
    path('course/<int:pk>/',CourseDetailView.as_view(), name='course_detail' ),
]

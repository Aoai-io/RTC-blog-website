from django.urls import path
from .views import InstructorDetailView

urlpatterns = [
    path('instructor/<int:pk>/profile', InstructorDetailView.as_view(), name='instructor.show'),
]

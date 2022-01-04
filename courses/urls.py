from django.urls import path
from .views import CourseDetailView, CourseListView, DataCollectorCreateView

urlpatterns = [
    path("", CourseListView.as_view(), name="courses_list"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path(
        route="course/register/",
        view=DataCollectorCreateView.as_view(),
        name="course_register",
    ),
]

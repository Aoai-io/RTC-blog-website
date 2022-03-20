from django.urls import path
from .views import CourseDetailView, CourseListView, DataCollectorCreateView, create, SearchResultListView, CourseSearchListView

urlpatterns = [
    path("", CourseListView.as_view(), name="courses_list"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path(
        route="course/register/",
        view=DataCollectorCreateView.as_view(),
        name="course_register",
    ),
    path("review/create/", create, name="review_create"),
    path("course/search/", SearchResultListView.as_view(), name="search_filter"),
    path("course/searchList/", CourseSearchListView.as_view(), name="search_list"),
]

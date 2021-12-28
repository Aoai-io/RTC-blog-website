from django.shortcuts import render
from django.views.generic import DetailView
from .models import Course
# Create your views here.




class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Instructor

# Create your views here.


class InstructorDetailView(DetailView):
    model = Instructor
    template_name = "instructors/show.html"




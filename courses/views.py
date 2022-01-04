from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Course, DataCollector

# Create your views here.


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"


class CourseListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"


class DataCollectorCreateView(SuccessMessageMixin, CreateView):
    model = DataCollector
    template_name = "courses/course_user_form.html"
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "date_of_birth",
        "gender",
        "street_address",
        "province",
        "city",
        "company",
    ]
    success_message = "Thank You For Using Our Service Form Submitted Successfully"


# def course_register(request):
#     return render(request, '')

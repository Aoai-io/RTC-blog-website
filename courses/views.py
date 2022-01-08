from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView
from .models import Course, DataCollector, Review
from .forms import DataCollectorForm
from .forms import ReviewForm

# Create your views here.



class DataCollectorFormView(FormView):
    model = DataCollector
    template_name = "courses/course_user_form.html"
    form_class = DataCollectorForm
    success_url = '/thanks/'


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"


class CourseListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"


class DataCollectorCreateView(SuccessMessageMixin, CreateView):
    model = DataCollector
    form_class = DataCollectorForm
    template_name = "courses/course_user_form.html"
    success_message = "Thank You For Using Our Service Form Submitted Successfully"


# def course_register(request):
#     return render(request, '')





def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ReviewForm()

    return render(request,'courses/course_detail.html',{'form': form})
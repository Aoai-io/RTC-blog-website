from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView
from .models import Course, DataCollector, Category
from .forms import DataCollectorForm
from .forms import ReviewForm

# Create your views here.


class DataCollectorFormView(FormView):
    model = DataCollector
    template_name = "courses/course_user_form.html"
    form_class = DataCollectorForm
    success_url = "/thanks/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CourseListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CourseSearchListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q == "" or q == None:
            pass
        else:
            return Course.objects.filter(
                Q(title__icontains=q)
                | Q(instructor__name__icontains=q)
                | Q(sub_category__title__icontains=q)
                | Q(sub_category__category__title__icontains=q)
            )
            # return Course.objects.filter(title__icontains=q)


class DataCollectorCreateView(SuccessMessageMixin, CreateView):
    model = DataCollector
    form_class = DataCollectorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    template_name = "courses/course_user_form.html"
    success_message = "Thank You For Using Our Service Form Submitted Successfully"


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = ReviewForm()

    return render(request, "courses/course_detail.html", {"form": form})


class SearchResultListView(ListView):
    model = Course
    template_name = "courses/search_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q == "" or q == None:
            pass
        else:
            return Course.objects.filter(Q(sub_category__title__icontains=q)|Q(sub_category__category__title__icontains=q))

from django.shortcuts import redirect, render
from articles.models import Article
from courses.models import Category, Course, SubCategory
from instructors.models import Instructor
from django.http import HttpResponse
from django.core.mail import send_mail

import os
import environ

env = environ.Env()
environ.Env.read_env(".env")


# Create your views here.

categories = None


def HomePageView(request):
    articles = Article.objects.all()
    courses = Course.objects.all()[:4]
    instructors = Instructor.objects.all()

    global categories
    categories = Category.objects.all()

    global sub_categories
    sub_categories = SubCategory.objects.all()

    context = {
        "articles": articles,
        "courses": courses,
        "instructors": instructors,
        "categories": categories,
        "sub_categories": sub_categories,
    }
    return render(request, "home.html", context=context)


def Deploy(request):
    os.system("touch tmp.deploy.txt")
    os.system("./serve.sh > tmp.deploy.txt 2>&1 &")
    return HttpResponse("<h1>deployed</h1>")

def send_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'support@aoai.io',
        [request.POST.get('email')],
        fail_silently=False,
    )
    return redirect('/')

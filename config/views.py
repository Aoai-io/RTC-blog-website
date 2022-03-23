from django.shortcuts import redirect, render
from articles.models import Article
from courses.models import Category, Course, SubCategory
from instructors.models import Instructor
from django.http import HttpResponse
from django.core.mail import send_mail
from .model import SubscribeEmail

import os
# Create your views here.

categories = None

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


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


def privacy_policy(request):
    categories = Category.objects.all()


    context = {
        "categories": categories,
    }
    return render(request, "privacy_policy.html", context=context)


def Deploy(request):
    os.system("touch tmp.deploy.txt")
    os.system("./serve.sh > tmp.deploy.txt 2>&1 &")
    return HttpResponse("<h1>deployed</h1>")


def send_email(request):
    obj, created = SubscribeEmail.objects.get_or_create(email=request.POST.get("email"))
    obj.value = request.POST.get("email")
    obj.save()

    send_mail(
        f"Hi there {request.POST.get('email')}",
        """
        Welcome to my newsletter! I’m so glad you’re interested in learning more from me. I can’t wait to start sharing latest RTCpro Content with you.

        Talk soon friend, 

        Osama Muhammed

        """,
        from_email="support@aoai.io",
        recipient_list=[request.POST.get("email")],
        fail_silently=False,
    )
    return redirect("/")

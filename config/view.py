from django.shortcuts import render
from articles.models import Article
from courses.models import Category, Course, SubCategory
from instructors.models import Instructor
from django.http import HttpResponse
import datetime
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

    # file_object = open("tmp.deploy.txt", "a")
    # file_object.write(f"{datetime.datetime.now()}\n")
    # file_object.write("###################################################\n")
    # file_object.close()
    os.system("./server.sh > tmp.deploy.txt 2>&1 &")

    # os.system(env("DEFAULT_GIT_QUERY") + " >> tmp.deploy.txt 2>&1 &")

    # os.system("source ../venv/bin/activate >> tmp.deploy.txt 2>&1 &")

    # os.system("pip install -r requirements.txt >> tmp.deploy.txt 2>&1 &")

    # os.system("python manage.py migrate >> tmp.deploy.txt 2>&1 &")

    # os.system("echo Omar@wolf.9803 | sudo -S systemctl restart gunicorn.service 2>&1 &")
    # os.system("echo Omar@wolf.9803 | sudo -S systemctl restart nginx.service 2>&1 &")

    # os.system(
    #     "cp /home/osama/RTC-blog-website/tmp.deploy.txt /home/osama/logs/deploy.txt 2>&1 &"
    # )
    # os.system("rm tmp.deploy.txt 2>&1 &")
    return HttpResponse("<h1>deployed</h1>")

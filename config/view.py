from django.shortcuts import render
from articles.models import Article
from courses.models import Category, Course
from instructors.models import Instructor
from django.http import HttpResponse
import datetime
import os
import environ

env = environ.Env()
environ.Env.read_env('.env')


# Create your views here.

categories = None


def HomePageView(request):

    articles = Article.objects.all()
    courses = Course.objects.all()[:4]
    instructors = Instructor.objects.all()

    global categories
    categories = Category.objects.all()

    context = {
    'articles': articles,
    'courses': courses,
    'instructors': instructors,
    'categories': categories,
}
    return render(request, 'home.html', context=context)

def Deploy(request):
    
    os.system('touch tmp.deploy.txt')

    file_object = open('tmp.deploy.txt', 'a')
    file_object.write(f'{datetime.datetime.now()}')
    file_object.write('\n')
    file_object.write('###################################################')
    file_object.write('\n')
    file_object.close()

    os.system(env('DEFAULT_GIT_QUERY') + ' >> tmp.deploy.txt')

    file_object = open('tmp.deploy.txt', 'a')
    file_object.write('\n')
    file_object.write('###################################################')
    file_object.write('\n')
    file_object.close()

    os.system('source ../venv/bin/activate >> tmp.deploy.txt')

    file_object = open('tmp.deploy.txt', 'a')
    file_object.write('\n')
    file_object.write('###################################################')
    file_object.write('\n')
    file_object.close()

    os.system('pip install -r requirements.txt >> tmp.deploy.txt')

    file_object = open('tmp.deploy.txt', 'a')
    file_object.write('\n')
    file_object.write('###################################################')
    file_object.write('\n')
    file_object.close()

    # os.system('python manage.py migrate >> tmp.deploy.txt')
    
    file_object = open('tmp.deploy.txt', 'a')
    file_object.write('\n')
    file_object.write('###################################################')
    file_object.write('\n')
    file_object.close()


    os.system('cp /home/osama/RTC-blog-website/tmp.deploy.txt /home/osama/logs/deploy.txt')
    os.system('rm tmp.deploy.txt')
    return HttpResponse("<h1>Deploy Successful</h1>")

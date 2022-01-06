from django.shortcuts import render
from articles.models import Article
from courses.models import Category, Course
from instructors.models import Instructor

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
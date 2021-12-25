from django.shortcuts import render
from articles.models import Article
from courses.models import Course
from instructors.models import Instructor

# Create your views here.


def HomePageView(request):

    articles = Article.objects.all()
    courses = Course.objects.all()
    instructors = Instructor.objects.all()

    context = {
    'articles': articles,
    'courses': courses,
    'instructors': instructors,
}
    return render(request, 'home.html', context=context)
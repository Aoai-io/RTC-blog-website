from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
from courses.models import Category
from django.views.generic import DetailView

# Create your views here.


def index(request):

    articles = Article.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(articles, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # ? context data for binding
    context = {
        "categories": categories,
        'page_obj': page_obj,

    }


    return render(request, "articles/articles_list.html", context=context)






class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"


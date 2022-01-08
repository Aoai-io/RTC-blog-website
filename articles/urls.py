from django.urls import path
from .views import index, ArticleDetailView
urlpatterns = [
    path('', index, name='articles_list'),
    path('article/<uuid:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]

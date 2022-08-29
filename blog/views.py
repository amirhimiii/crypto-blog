from django.shortcuts import render
from django.views import generic
from .models import Article


class ArticleHomeView(generic.ListView):
    model = Article
    template_name = "blog/article_home.html"
    # context_object_name  = 'article'


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "blog/article_detail.html"



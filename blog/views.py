from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article, Category
from .models import User

class ArticleHomeView(generic.ListView):
    model = Article
    template_name = "blog/article_home.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context["article"] =Article.objects.article_published()
        return context
    
    

class ArticleDetailView(generic.DetailView):
    template_name = "blog/article_detail.html"

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article , slug=slug)



class CategoryListView(generic.ListView):
    model = Category
    template_name = "blog/category_list.html"

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        context['categories'] = get_object_or_404(Category.objects.category_status(),slug=slug)
        return context 

    # def get_queryset(self):
    #     global category
    #     slug = self.kwargs.get('slug')
    #     category =  get_object_or_404(Category.objects.category_status(),slug=slug)
    #     return category.articles.category_status()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = category
    #     return context 


class AuthorListView(generic.ListView):
    # model = Article
    template_name = "blog/user_list.html"
    context_object_name = 'article'
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username=username)
        return author.articles.article_published

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = author
        return context
    
        
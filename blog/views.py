from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article, Category, Comment
from .models import User
from profiles.mixins import AuthorAccessMixin
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count , Q
from datetime import datetime, timedelta




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
        article =  get_object_or_404(Article, slug=slug)
    
        ip_address =self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm 
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
        return context
    


    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
    
        slug = self.kwargs.get('slug')#1 gereftan id
        article =get_object_or_404(Article, slug=slug)#2 badesh dadn id be get_obj
        obj.comment = article 

        return super().form_valid(form)

    


class ArticlePreview(AuthorAccessMixin, generic.DetailView):
    template_name =  "blog/article_preview.html"

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
    



class SearchView(generic.ListView):
    # model = Article
    template_name = "blog/search_list.html"
    context_object_name = 'article'
    
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q (description__icontains=search)) |Q(title__icontains=search)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get('q')
        return context
    
        
        
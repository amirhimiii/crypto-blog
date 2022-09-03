from django.shortcuts import render
from django.views import generic
from blog.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldMixin, FormValidMixin, AuthorAccessMixin


class ProfileListView(LoginRequiredMixin, generic.ListView):
    queryset = Article.objects.all()
    template_name = "profile/profile_view.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(user=self.request.user)


    
class ArticleCreateView(LoginRequiredMixin,FormValidMixin ,FieldMixin, generic.CreateView):
    model =Article
    template_name = "profile/article_create.html"


    
class ArticleUpdateView(AuthorAccessMixin, FormValidMixin ,FieldMixin, generic.UpdateView):
    model =Article
    template_name = "profile/article_create.html"



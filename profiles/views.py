from django.shortcuts import render
from django.views import generic
from blog.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileListView(LoginRequiredMixin, generic.ListView):
    queryset = Article.objects.all()
    template_name = "profile/profile_view.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(user=self.request.user)


    
# class ArticleCreateView(generic.CreateView):
#     model = Article
#     template_name = "profile/article_create.html"


#CRUD
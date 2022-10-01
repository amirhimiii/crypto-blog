from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldMixin, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin, AuthorsAccessMixin
from blog.models import User
from profiles.forms import ProfileUserForm

class ProfileListView(AuthorsAccessMixin, generic.ListView):
    queryset = Article.objects.all()
    template_name = "profile/profile_view.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(user=self.request.user)


    
class ArticleCreateView(AuthorsAccessMixin,FormValidMixin ,FieldMixin, generic.CreateView):
    model =Article
    template_name = "profile/article_create.html"


    
class ArticleUpdateView(AuthorAccessMixin, FormValidMixin ,FieldMixin, generic.UpdateView):
    model =Article
    template_name = "profile/article_create.html"


    
class ArticleDeleteView(SuperUserAccessMixin, generic.DeleteView):
    model =Article
    template_name = "profile/article_delete.html"
    success_url = reverse_lazy('blog:home')


class Profile(LoginRequiredMixin ,generic.UpdateView):
    template_name = 'profile/profile.html'
    form_class = ProfileUserForm
    success_url = reverse_lazy('profile:profile')

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user
        })
        return kwargs
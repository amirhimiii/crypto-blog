from django.http import Http404
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404, redirect
from blog.models import Article

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if  self.request.user.is_superuser:
            self.fields = ('user','slug','title',
                'description','thumbnail','publish','is_special',
                'status','category')
        elif self.request.user.is_author:
            self.fields = ('slug','title',
                'description','thumbnail','publish','is_special',
                'category')
        else:
            raise  Http404('you cant see this page')
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.status = 'D'
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.user == request.user and article.status in ['D','B'] or\
        request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404(' You cant see this page')

class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('profile:profile')
        else:
            return redirect('account_login')



class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404(' You cant see this page')
            
            
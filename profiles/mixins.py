from django.http import Http404
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if  self.request.user.is_superuser:
            self.fields = ('user','slug','title',
                'description','thumbnail','publish',
                'status','category')
        elif self.request.user.is_author:
            self.fields = ('slug','title',
                'description','thumbnail','publish',
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
        if article.user == request.user and article.status =='D' or\
        request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404(' You cant see this page')
            
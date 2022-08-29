from django.contrib import admin
from .models import Article
from django.utils.translation import gettext_lazy as _



# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','publish','status']
    list_filter = ['status','publish']
    search_fields = ['title','description']
    prepopulated_fields = {"slug": ("title",)}
    ordering =['-publish','-status',]
    


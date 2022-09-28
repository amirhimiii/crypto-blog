from django import template
from blog.models import Category, Article
from django.db.models import Count , Q
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType




register = template.Library()


@register.inclusion_tag("blog/category_navbar.html")
def category_navbar():
    return {
        'category': Category.objects.filter(status=True)
    }



@register.inclusion_tag("blog/popular_articles.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        'popular_articles': Article.objects.article_published().annotate(
            count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count','-publish')[:3],
        
        'title': 'مقالات پربازدید ماه'
        }




@register.inclusion_tag("blog/popular_articles.html")
def hot_articles():
    return {
        'popular_articles': Article.objects.article_published().annotate(
            count=Count('comments', filter=Q(comments__posted__gt=last_month) and Q(comments__datetime_created=last_month))).order_by('-count','-publish'),
        
        'title': 'مقالات داغ ماه'
        }
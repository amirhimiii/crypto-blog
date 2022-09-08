from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.contrib.auth import get_user_model

from django.utils.translation import ngettext



class ArticleFilterManager(models.Manager):
    def article_published(self):
        return self.filter(status='P')


class CategoryManager(models.Manager):
    def category_status(self):
        return self.filter(status=True)



class Category(models.Model):
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, default= None, blank=True, null=True, related_name='children',verbose_name= _('main category'))
    title = models.CharField(max_length=50, verbose_name= _('category title'))
    status = models.BooleanField(default=True,verbose_name= _('category status'))
    slug = models.SlugField() # baray neshon dadn urlsh balay safhe mitone monaseb bashe

    objects = CategoryManager()

    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title




class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()



User = get_user_model()
class Article(models.Model):
    STATUS_CHOICES = (
        ('D','Draft'),
        ('P','Published'),
        ('I','Investigation'),
        ('B','Back')
    )
    user = models.ForeignKey(User, verbose_name=_("user") ,on_delete=models.CASCADE, related_name = 'articles')
    hits = models.ManyToManyField(IPAddress, through="ArticleHit" ,blank=True, related_name='hits', verbose_name=('views'))
    is_special = models.BooleanField(default=False,verbose_name= _('special article?'))    
    title = models.CharField(max_length=50, verbose_name= _('title'))
    slug = models.SlugField()
    description = models.TextField( verbose_name= _('description'))
    thumbnail = models.ImageField(upload_to='thumbnail/', blank = False, verbose_name= _('thumbnail'))
    publish = models.DateTimeField(default= timezone.now, verbose_name= _('published date:'))
    created = models.DateField(auto_now_add=timezone.now,  verbose_name= _('created:'))
    updated = models.DateField(auto_now=timezone.now, verbose_name= _('updated article:'))
    status = models.CharField(choices=STATUS_CHOICES ,max_length=1, verbose_name= _('status'))
    category = models.ManyToManyField(Category, verbose_name=_("category") ,related_name='articles_category')


    objects = ArticleFilterManager()# The Dahl-specific manager.


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"slug": self.slug})
    

    def category_published(self):
        return self.category.filter(status=True)

    def thumbnail_image(self):
        return format_html("<img width='90' height='60'  src='{}'>".format(self.thumbnail.url))
    thumbnail_image.short_description =_('article image')


    def category_to_str(self):
        return ", ".join([category.title for category in self.category.category_status()])
    category_to_str.short_description='category'


class Comment(models.Model):
    title = models.CharField(max_length=50)
    text  = models.TextField()
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    comment = models.ForeignKey(Article, verbose_name=_("comment"), on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now=timezone.now)

    def get_absolute_url(self):
        return reverse("blog:home")




class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

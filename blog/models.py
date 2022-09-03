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



User = get_user_model()
class Article(models.Model):
    STATUS_CHOICES = (
        ('D','Draft'),
        ('P','Published')
    )
    user = models.ForeignKey(User, verbose_name=_("user") ,on_delete=models.CASCADE, related_name = 'articles')
    title = models.CharField(max_length=50, verbose_name= _('title'))
    slug = models.SlugField()
    description = models.TextField( verbose_name= _('description'))
    thumbnail = models.ImageField(upload_to='thumbnail/', blank = True, verbose_name= _('thumbnail'))
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

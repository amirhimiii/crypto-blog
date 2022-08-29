from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _




# class Category(models.Model):
#     title = models.CharField(max_length=50)
#     status = models.BooleanField(default=True)
#     slug = models.SlugField() # baray neshon dadn urlsh balay safhe mitone monaseb bashe


#     class Meta:
#         verbose_name = _("Category")
#         verbose_name_plural = _("Categorys")

#     def __str__(self):
#         return self.title






class Article(models.Model):
    STATUS_CHOICES = (
        ('D','Draft'),
        ('P','Published')
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/', blank = True)
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateField(auto_now_add=False)
    updated = models.DateField(auto_now=False)
    status = models.CharField(choices=STATUS_CHOICES ,max_length=1)
    # category = models.ManyToManyField(Category, verbose_name=_("category"))




    class Meta:
        verbose_name = ("article")
        verbose_name_plural = ("articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"slug": self.slug})
    



from django.db import models
from django.utils import timezone





class Article(models.Model):
    STATUS_CHOICES = (
        ('D','Draft'),
        ('P','Published')
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=None, blank = True)
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateField(auto_now_add=False)
    updated = models.DateField(auto_now=False)
    status = models.CharField(choices=STATUS_CHOICES ,max_length=1)



    class Meta:
        verbose_name = ("article")
        verbose_name_plural = ("articles")

    def __str__(self):
        return self.title



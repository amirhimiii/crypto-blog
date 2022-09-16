from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Contact(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    text = models.TextField()

    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.first_name


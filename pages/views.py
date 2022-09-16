from django.shortcuts import render
from .models import Contact
from django.views import generic
from .forms import ContactForm
from django.urls import reverse_lazy



class ContactView(generic.CreateView):
    form_class = ContactForm
    template_name = "pages/contact_us.html"
    success_url = reverse_lazy('blog:home')

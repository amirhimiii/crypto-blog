from django.contrib import admin

# Register your models here.
from .models import CustomUser



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','is_staff']
    list_filter = ['is_staff','is_superuser','is_active']
    search_fields = ['first_name']
    
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# UserAdmin.fieldsets += (
#     ('special_field', {'fields': ('is_author', 'special_user')}),
# )

# admin.site.register()
UserAdmin.fieldsets [2][1]['fields']= (
'is_author', 'special_user')

# UserAdmin.list_display += ('is_author', 'is_special_user')

# UserAdmin.fieldsets [2][1]['fields']= (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     'is_author',
#                     'special_user'
#                     "groups",
#                     "user_permissions",)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','is_staff','is_author', 'is_special_user']
    list_filter = ['is_staff','is_superuser','is_active']
    search_fields = ['first_name']

    
from django.contrib import admin
from .models import Article, Category
from django.utils.translation import gettext_lazy as _


# @admin.action(description='Mark selected stories as published')
# def make_published(modeladmin, request, queryset):
#     queryset.update(status='P')


# @admin.action(description='Mark selected stories as drafted')
# def make_drafted(modeladmin, request, queryset):
#     queryset.update(status='D')


# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','thumbnail_image','publish','status','category_to_str']
    list_filter = ['status','publish']
    search_fields = ['title','description']
    prepopulated_fields = {"slug": ("title",)}
    ordering =['-publish','-status',]
    list_display_links  = ['category_to_str','title']



    def make_published(self, request, queryset):
        updated = queryset.update(status='P')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description =_( 'published marked articles')

    
    def make_drafted(self, request, queryset):
        updated = queryset.update(status='D')
        self.message_user(request, ngettext(
            '%d story was successfully marked as drafted.',
            '%d stories were successfully marked as drafted.',
            updated,
        ) % updated, messages.SUCCESS)

    actions =[make_published, make_drafted]
    make_drafted.short_description = _('drafted marked articles')




    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category_published()])
    category_to_str.short_description='category'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','slug','status']
    list_filter = ['status']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}
    ordering =['-status']


    
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description =_( 'published marked catgory')

    
    def make_drafted(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
            '%d story was successfully marked as drafted.',
            '%d stories were successfully marked as drafted.',
            updated,
        ) % updated, messages.SUCCESS)
    make_drafted.short_description =_('drafted marked catgory')

    actions =[make_published, make_drafted]



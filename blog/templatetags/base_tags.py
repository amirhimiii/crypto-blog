from django import template
from blog.models import Category
register = template.Library()

# @register.inclusion_tag("blog/category_navbar.html", takes_context=True)
# def ".html"(context):
#     request = context.get("request")
    
#     return {
#         "request": request,
        
#     }



@register.inclusion_tag("blog/category_navbar.html")
def category_navbar():
    return {
        'category': Category.objects.filter(status=True)
    }
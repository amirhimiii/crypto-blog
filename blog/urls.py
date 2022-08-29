from django.urls import path
from .views import ArticleHomeView, ArticleDetailView

app_name = 'blog'

urlpatterns = [
    path('blog/', ArticleHomeView.as_view(), name='article-list'),
    path('detail/<slug:slug>/',ArticleDetailView.as_view(),name='article-detail')
]

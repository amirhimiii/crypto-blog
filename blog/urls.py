from django.urls import path
from .views import ArticleHomeView, ArticleDetailView, CategoryListView

app_name = 'blog'

urlpatterns = [
    path('', ArticleHomeView.as_view(), name='article-list'),
    path('detail/<slug:slug>/',ArticleDetailView.as_view(),name='article-detail'),
    path('category/<slug:slug>/',CategoryListView.as_view(),name='category'),

]

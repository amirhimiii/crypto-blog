from django.urls import path
from .views import (
    ArticleHomeView,
    ArticleDetailView,
    CategoryListView,
    AuthorListView,
    ArticlePreview,
    CommentCreateView,
    SearchView
)

app_name = 'blog'

urlpatterns = [
    path('', ArticleHomeView.as_view(), name='home'),
    path('detail/<slug:slug>/',ArticleDetailView.as_view(),name='article-detail'),
    path('preview/<slug:slug>/',ArticlePreview.as_view(),name='article-preview'),
    path('category/<slug:slug>/',CategoryListView.as_view(),name='category'),
    path('user_list/<slug:username>/',AuthorListView.as_view(),name='author-list'),
    path('comment/<slug:slug>/',CommentCreateView.as_view(),name='comment-create'),
    path('search/<int:page>/',SearchView.as_view(),name='search'),
    path('search/',SearchView.as_view(),name='search'),
]

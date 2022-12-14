from django.urls import path
from .views import (
ProfileListView,
ArticleCreateView,
ArticleUpdateView,
ArticleDeleteView,
Profile
)

app_name = 'profile'

urlpatterns = [
    path('', ProfileListView.as_view(), name = 'article-list'),
    path('create/', ArticleCreateView.as_view(), name = 'article-create'),
    path('update/<slug:slug>/',ArticleUpdateView.as_view(), name = 'article-update' ),
    path('delete/<slug:slug>/',ArticleDeleteView.as_view(),name='article-delete'),
    path('profile/',Profile.as_view(),name='profile'),

]
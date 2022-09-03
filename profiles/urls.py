from django.urls import path
from .views import (
ProfileListView,
ArticleCreateView,
ArticleUpdateView

)

app_name = 'profile'

urlpatterns = [
    path('', ProfileListView.as_view(), name = 'article-list'),
    path('create/', ArticleCreateView.as_view(), name = 'article-list'),
    path('update/<slug:slug>/',ArticleUpdateView.as_view(), name = 'article-update' )

    
    # path('product/delete/<slug:slug>/',ProductDeleteView.as_view(),name='product-delete'),
    # path('product/create/',ProductCreateView.as_view(),name='product-create'),
    # path('product/update/<slug:slug>/',ProductUpdateView.as_view(),name='product-update'),
    # path('profile/',Profile.as_view(),name='profile'),

]
from django.urls import path
from .views import (
    Create_View,
    Detail_View,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'blog' # namespace
urlpatterns = [
    # path('create/', Create_View),
    # path('<int:my_id>/', Detail_View),
    path('',ArticleListView.as_view(),name='article-list'),
    path('<int:id>/',ArticleDetailView.as_view(),name = 'article-detail'),
    path('create/', ArticleCreateView.as_view()),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name = 'article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name = 'article-delete')
]
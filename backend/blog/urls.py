from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, BlogPostCategoriesView
                    

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    #path('update', BlogWriteupView.as_view()),
    path('categories', BlogPostCategoriesView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
]
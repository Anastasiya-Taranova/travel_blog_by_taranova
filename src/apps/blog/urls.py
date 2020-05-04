from django.urls import path

from apps.blog import views
from apps.blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", views.AllBlogPostView.as_view(), name="blog"),
    path("post/<int:pk>", views.BlogPostView.as_view(), name="post"),
]

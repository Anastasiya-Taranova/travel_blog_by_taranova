from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from apps.blog.models import BlogPost


class AllBlogPostView(LoginRequiredMixin, ListView, ):
    template_name = "blog/index.html"
    model = BlogPost


class BlogPostView(LoginRequiredMixin, DetailView):
    template_name = "blog/post.html"
    model = BlogPost

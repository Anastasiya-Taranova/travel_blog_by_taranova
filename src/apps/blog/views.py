from django.views.generic import ListView, DetailView
from apps.blog.models import BlogPost


class AllBlogPostView(ListView):
    template_name = "blog/index.html"
    model = BlogPost


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = BlogPost



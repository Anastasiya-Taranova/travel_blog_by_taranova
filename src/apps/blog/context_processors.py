from apps.blog.models import Post
from apps.blog.models import Random


def random_photos(request):
    return {
        "random_photos": Random.objects.order_by("?")[:4],
    }


def blog(request):
    return {
        "posts": Post.objects.order_by("?"),
    }

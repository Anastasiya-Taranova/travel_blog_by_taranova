from apps.blog.models import Post, Random
from apps.blog.views import PhotosView


def random_photos(request):
    return {
        'photos': PhotosView(),
    }


def blog(request):
    return {
        'posts': Post.objects.order_by('?'),
    }

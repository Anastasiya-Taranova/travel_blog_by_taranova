from random import choices

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from apps.blog.forms import CommentForm
from apps.blog.models import Post


class AllBlogPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx["form"] = CommentForm(
                initial={"post": self.object, "author": self.request.user}
            )

        return ctx


class CommentView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    http_method_names = ["post"]

    def get_success_url(self):
        url = reverse_lazy("blog:post", kwargs={"pk": self.kwargs["pk"]})

        return url


# class ImageView(TemplateView):
#     template_name = "blog/posts.html"
#
#     def get_context_data(self, **kwargs):
#         images_urls = [
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/69602699_487992365118265_4417764748370499537_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=LXNTl_k2Ol4AX_0IM9O&oh=fcb6c9f2a0029141c319afd864ac23bc&oe=5F7C6D11",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/71562959_957703444570255_8539066205975295133_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=107&_nc_ohc=taU8uHXUgPMAX_yBI9H&oh=79a9cfb0976799dce5de024655189828&oe=5F7B299D",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/69751747_2254864897956512_7321464936466138595_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=108&_nc_ohc=KvUymq8PNY4AX-NbBHK&oh=e4458e9bbc2851df0c5834a20c3233c5&oe=5F7D4614",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/68686929_382021066063412_7971678111364146195_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=108&_nc_ohc=hCaz3OdZbQwAX_tORB7&oh=587cbd465ff4912965113a68a9240d76&oe=5F7BA2BB",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/65723662_634309233743393_2017934153174321352_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=105&_nc_ohc=pZpST2wY1h8AX_vXhLT&oh=3d6d10b0fa1c5d67d091b612d0a7efab&oe=5F7E768C",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/56686084_458782517997299_6977927057441795925_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=111&_nc_ohc=Y6__=111&_nc_ohc=Y6__rnIsbWUAX89iCh5&oh=9467f33fe12967db3ef7f1ab48849056&oe=5F7ADB01",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/54447034_1372961066162474_7490785363625199271_n.jpg?_nc_ht=scontent-waw1-1.cdnirnIsbWUAX89iCh5&oh=9467f33fe12967db3ef7f1ab48849056&oe=5F7ADB01",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/54447034_1372961066162474_7490785363625199271_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=102&_nc_ohc=YyYtygE60rwAX-BTuwn&oh=ccb7cac94358fcf436c1bfc832e805ce&oe=5F7E436A",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/40676533_2265170153510799_2757346925619108858_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=ivl4D39svEEAX-qJW2Q&oh=b09dd9a75dbba80b9bac7e06f336df2e&oe=5F7B7207",
#                 "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/e35/39995668_321224858627367_6723593756529917952_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=Fvt_9SHyzm4AX86gz2F&oh=e9e1112432624805ee375b2be7c5e489&oe=5F7C1B37",
#         ]
#         random_4_images = choices(images_urls, k=4)
#         ctx = super().get_context_data(**kwargs)
#         ctx.update({
#             "random_4_images": random_4_images,
#         })
#
#         return ctx

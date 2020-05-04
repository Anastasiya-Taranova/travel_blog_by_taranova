from django.contrib.auth import get_user_model
from django.db import models as m
from django.urls import reverse_lazy

User = get_user_model()


class BlogPost(m.Model):
    author = m.ForeignKey(User, on_delete=m.SET_NULL, null=True, blank=True)
    title = m.TextField(null=True, blank=True)
    content = m.TextField(null=True, blank=True)

    def get_absolute_url(self):  # возращает путь к этому объекту
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})

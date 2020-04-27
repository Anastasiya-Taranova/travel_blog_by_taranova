from django.db import models as m
from django.urls import reverse_lazy


class BlogPost(m.Model):
    title = m.TextField(null=True, blank=True)
    content = m.TextField(null=True, blank=True)

    def get_absolute_url(self):  # возращает путь к этому объекту
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})

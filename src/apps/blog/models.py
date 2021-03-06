import uuid

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


class Post(models.Model):
    title = models.TextField(null=True, blank=True)
    precontent = models.TextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    nr_likes = models.IntegerField(null=True, blank=True)
    nr_dislikes = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})

    def upvote(self):
        if self.nr_likes is None:
            self.nr_likes = 0

        self.nr_likes += 1
        self.save()

    def downvote(self):
        if self.nr_dislikes is None:
            self.nr_dislikes = 0

        self.nr_dislikes += 1
        self.save()

    class Meta:
        verbose_name_plural = "Посты"

    def __str__(self):
        return str(f"Пост: " + " " + self.title)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    nr_likes = models.IntegerField(null=True, blank=True)
    nr_dislikes = models.IntegerField(null=True, blank=True)

    message = models.TextField()

    def upvote(self):
        if self.nr_likes is None:
            self.nr_likes = 0

        self.nr_likes += 1
        self.save()

    def downvote(self):
        if self.nr_dislikes is None:
            self.nr_dislikes = 0

        self.nr_dislikes += 1
        self.save()

    class Meta:
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return str(f"Комментарий: " + " " + self.message)


class Photo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    original = models.FileField(storage=S3Boto3Storage())

    class Meta:
        verbose_name_plural = "Фотографии"


class Random(models.Model):
    url = models.URLField()

    class Meta:
        verbose_name_plural = "Фотографии на главную страницу"

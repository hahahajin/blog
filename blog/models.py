from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'categories'

class Blog(models.Model):
    title = models.CharField(max_length=30)
    writer = models.CharField(max_length=10)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models. ImageField(upload_to = "blog/", blank = True, null = True)
   

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now) #장고에서 기본으로 제공됨
    # 들어갈 내용들 : 댓글 작성자, 댓글 내용, 댓글 작성 시간

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text


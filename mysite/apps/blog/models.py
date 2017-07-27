from django.db import models
from django.utils.safestring import mark_safe
from markdown_deux import markdown


class Post(models.Model):
    slug = models.SlugField(db_index=True, unique=True, max_length=255, editable=False)  # Hide from admin
    title = models.TextField(db_index=True, max_length=255,)
    body = models.TextField()
    read_time = models.PositiveSmallIntegerField(editable=False)  # Hide from admin

    tags = models.ManyToManyField(
        'blog.Tag', related_name='posts', blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_markdown(self):
        content = self.body
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

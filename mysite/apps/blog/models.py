from django.db import models


class Post(models.Model):
    slug = models.SlugField(db_index=True, unique=True, max_length=255)
    title = models.TextField(db_index=True, max_length=255,)
    body = models.TextField()
    read_time = models.PositiveSmallIntegerField()

    tags = models.ManyToManyField(
        'blog.Tag', related_name='posts'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

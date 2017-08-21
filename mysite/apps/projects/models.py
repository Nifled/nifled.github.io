from django.db import models

from mysite.apps.blog.models import Tag


class Project(models.Model):
    name = models.CharField(max_length=255)
    imageUrl = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        'blog.Tag', related_name='projects', blank=True
    )

    def __str__(self):
        return self.name

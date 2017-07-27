from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Post
from .utils import get_read_time


@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    MAXIMUM_SLUG_LENGTH = 255

    # Creating the slug
    if instance and not instance.slug:
        slug = slugify(instance.title)

        if len(slug) > MAXIMUM_SLUG_LENGTH:
            slug = slug[:MAXIMUM_SLUG_LENGTH]

        instance.slug = slug

    # Creating the estimated read time
    if instance and instance.body:
        read_time = get_read_time(instance.get_markdown)  # body field is Markdown
        instance.read_time = read_time




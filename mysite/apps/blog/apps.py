from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'mysite.apps.blog'

    def ready(self):
        import mysite.apps.blog.signals

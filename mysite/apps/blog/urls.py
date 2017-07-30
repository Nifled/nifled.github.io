from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

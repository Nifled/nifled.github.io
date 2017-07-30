from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Post, Tag
from .serializers import PostSerializer


class PostViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    lookup_field = 'slug'
    queryset = Post.objects.all()
    # TODO : Add custom permission for type IsStaffOrReadOnly
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        If tag exists in query params, filter Posts by the tag object.
        E.G. /posts?tag=dragons
        """
        queryset = self.queryset

        # TODO : Make filtering support multiple tags in query parameters
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = queryset.filter(tags__tag=tag)

        return queryset

    def create(self, request):
        context = {'request': request}

        serializer_data = request.data

        serializer = self.serializer_class(
            data=serializer_data,
            context=context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        context = {'request': request}

        serializer = self.serializer_class(
            self.get_queryset(),
            context=context,
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, slug):
        context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Post.DoesNotExist:
            raise NotFound('A post with this slug does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, slug):

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Post.DoesNotExist:
            raise NotFound('An article with this slug does not exist.')

        serializer_data = request.data
        context = {'request': request}

        serializer = self.serializer_class(
            serializer_instance,
            context=context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

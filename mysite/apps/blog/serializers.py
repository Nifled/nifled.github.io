from rest_framework import serializers

from .models import Post, Tag


class PostSerializer(serializers.HyperlinkedModelSerializer):

    slug = serializers.SlugField(required=False)
    description = serializers.CharField(required=False)

    # Show the list of tags' __str__ string in our JSON
    # response. So we can retrieve them as an array.
    tagList = serializers.StringRelatedField(many=True, required=False, source='tags')

    created_at = serializers.SerializerMethodField(method_name='get_created_at')
    updated_at = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Post
        fields = (
            'body',
            'created_at',
            'description',
            'read_time',
            'slug',
            'tagList',
            'title',
            'url',
        )

    def create(self, validated_data):
        """Create tags dynamically along with other validated data."""

        tags = validated_data.pop('tags', [])

        post = Post.objects.create(**validated_data)

        for tag in tags:
            post.tags.add(tag)

        return post

    # \
    #  Serializer methods
    # /
    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    # On Responses, we only want the Tag objects to show
    # the name field (see Tag model) as strings, in an array
    def to_representation(self, obj):
        return obj.name

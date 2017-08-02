from rest_framework import serializers

from .models import Tag


class TagRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Tag.objects.all()

    # \
    #  The to_internal_value() method is called to restore a
    #  primitive datatype into its internal python representation.
    # /
    def to_internal_value(self, data):
        """
        This method should raise a serializers.ValidationError if the data is invalid.
        
        When a serializer receives a payload with, lets say,
        ```tagList = ["python", "django", "django-rest-framework"]```
        this function will take in the data and check if the tag exists.
        If it does, it will just return the Tag object, if it doesn't exist, 
        it will create a new Tag object and return it.
        """
        tag, created = Tag.objects.get_or_create(name=data, slug=data.lower())

        return tag

    # \
    #  The .to_representation() method is called to convert the
    #  initial datatype into a primitive, serializable datatype.
    # /
    def to_representation(self, value):
        return value.name

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
        """
        tag, created = Tag.objects.get_or_create(name=data, slug=data.lower())

        return tag

    # \
    #  The .to_representation() method is called to convert the
    #  initial datatype into a primitive, serializable datatype.
    # /
    def to_representation(self, value):
        return value.name

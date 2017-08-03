from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration request.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # Use the `create_user` from custom UserManager
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # Validate that user provided an email and password and that
        # this combination matches one of the users in the database.
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # `authenticate` method is provided by Django and handles checking
        # for a user that matches email/password combination in DB.
        # `USERNAME_FIELD` is set to `email`.
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    # These values are the default provided by Django.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token',)
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """Update a User instance."""

        # Passwords should not be handled with `setattr`, unlike other fields.
        # Django provides a function that handles hashing and
        # salting passwords. That means
        # we need to remove the password field from the
        # `validated_data` dictionary before iterating over it.
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            # E.G. for our User, set the 'username' (key) to it's value from request
            # (see the UserRetrieveUpdateAPIView).
            setattr(instance, key, value)

        if password is not None:
            # `.set_password()`  handles all of the security stuff.
            instance.set_password(password)  # Set new password (if new password is provided)

        # After everything has been updated the `save` method must be
        # called on the model. `.set_password()` does not save the model.
        instance.save()

        return instance

from rest_framework import serializers

from . import models

"""
SERIALIZERS:
- Serializers allow complex data such as querysets and model instances to be 
converted to native Python datatypes that can then be easily rendered into 
JSON, XML or other content types. 
- Serializers also provide deserialization, allowing parsed data to be 
converted back into complex types, after first validating the incoming data.
- Serializers also take care of validations.
"""


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)


"""
MODEL SERIALIZER:
Often you'll want serializer classes that map closely to Django model definitions.
The ModelSerializer class provides a shortcut that lets you automatically create a 
Serializer class with fields that correspond to the Model fields.
https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
"""
class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                # 'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user."""

        # user = models.UserProfile(
        #     email=validated_data['email'],
        #     name=validated_data['name']
        # )
        # user.set_password(validated_data['password'])
        # user.save()

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        # fields = ('id', 'user_profile', 'status_text', 'created_on')
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}

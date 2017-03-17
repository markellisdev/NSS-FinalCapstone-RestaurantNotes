from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restaurant_notes.models import RestaurantNote, Customer


class RestaurantNoteSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`RestaurantNote`
    author: Mark Ellis
    """

    class Meta:
        model = RestaurantNote
        fields = ('url', 'created', 'title', 'note_text', 'restaurant_id', 'favorite_dish', )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`auth.User`
    author: Mark Ellis
    """
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'groups', )

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`auth.User`
    author: Mark Ellis
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :models:`Group`
    author: Mark Ellis
    """
    class Meta:
        model = Group
        fields = ('url', 'name')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`bangapi.Customer`
    author: Mark Ellis
    """
    class Meta:
        model = Customer
        fields = ('url', 'user', 'address', 'city', 'state_province', 'country', )

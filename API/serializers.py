from rest_framework import serializers
from tinder.models import User


class UserSerializer(serializers.ModelSerializer):
    data_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'passwords': {'write_only': True}}

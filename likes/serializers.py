from rest_framework import serializers
from tinder.models import User


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
                  )


class DisLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
        )

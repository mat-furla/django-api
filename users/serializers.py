from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from uuid import uuid4

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=True)

    class Meta:
        model = User
        fields = ('__all__')

    def create(self, validated_data):
        if validated_data.get('password') == "":
            validated_data['password'] = make_password(str(uuid4()))
        else:
            validated_data['password'] = make_password(
                validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

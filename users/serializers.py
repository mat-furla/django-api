from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254)
    first_name = serializers.CharField(max_length=254)
    last_name = serializers.CharField(max_length=254)
    birth_date = serializers.DateField()

    class Meta:
        model = User
        fields = ('__all__')

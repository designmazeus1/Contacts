from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import (
    User,
    ProfileFeedItem,
)

class HelloSerializer(serializers.Serializer):
    """Bizning API Viewni sinab ko‘rish uchun nom maydonini ketma-ketlashtiradi."""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Foydalanuvchi profilimiz ob'ektlari uchun seriyalilashtiruvchi."""

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Yangi foydalanuvchi yaratish va qaytarish."""

        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Profil tasmasi elementlari uchun serializator."""

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile','status_text','created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
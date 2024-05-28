from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "city", "avatar", "payments"]


class UserPasswordSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", "phone", "city", "avatar", "role"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

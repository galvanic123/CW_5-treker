from rest_framework import serializers

from users.models import CustomsUser


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели привычка."""

    class Meta:
        model = CustomsUser
        fields = "__all__"

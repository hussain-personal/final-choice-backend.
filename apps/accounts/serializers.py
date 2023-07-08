from rest_framework.serializers import ModelSerializer
from .models import User


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name",
                  "email", "phone_number", "password"]

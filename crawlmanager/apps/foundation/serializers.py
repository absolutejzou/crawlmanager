from marshmallow import Schema, fields
from rest_framework import serializers

from crawlmanager.apps.foundation.models import User


class UserSerializer(Schema):
    user_name = fields.Str()
    is_active = fields.Boolean()


class UserSeria(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')

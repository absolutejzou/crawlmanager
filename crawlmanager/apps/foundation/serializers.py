from marshmallow import Schema, fields


class UserSerializer(Schema):
    user_name = fields.Str()
    is_active = fields.Boolean()

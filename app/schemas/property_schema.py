# Core Library
from enum import Enum

# Third party
from marshmallow import Schema, ValidationError, fields, validate


class Status(Enum):
    PRE_VENTA = 3
    EN_VENTA = 4
    VENDIDO = 5


class StatusField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.value

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return Status(value)
        except ValueError as error:
            raise ValidationError("Invalid Status") from error


class PropertyRequest(Schema):
    status = fields.List(fields.Integer(validate=validate.OneOf([3, 4, 5])), required=False)
    city = fields.List(fields.String(), required=False)
    year = fields.List(fields.String(), required=False)


class PropertyResponse(Schema):
    address = fields.String(required=True)
    city = fields.String(required=True)
    price = fields.Integer(required=True)
    description = fields.String(required=True)
    status = fields.String(required=True)


property_request_schema = PropertyRequest()
property_response_schema = PropertyResponse(many=True)

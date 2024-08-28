# Core Library
import json

# Third party
import jsonschema
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest, HTTPException, NotFound
from werkzeug.wrappers import Request, Response

# First party
from app.repositories.property_repository import PropertyRepository
from app.schemas.property_schema import (
    property_request_schema,
    property_response_schema,
)
from app.services.property_service import PropertyService


def get_request_data(request: Request):
    if request.content_type == 'application/json':
        try:
            return request.get_json(silent=True) or {}
        except json.JSONDecodeError:
            raise BadRequest(description='Invalid JSON')
    return {}


def get_properties(request: Request):
    try:
        body_params = get_request_data(request)

        validated_data = property_request_schema.load(body_params)

        property_repo = PropertyRepository()
        property_service = PropertyService(property_repo)
        properties = property_service.get_all_with_filters(body_params=validated_data)

        if not properties:
            raise NotFound(description='Properties not found')

        result = property_response_schema.dump(properties)
        return Response(json.dumps(result, ensure_ascii=False), mimetype='application/json')
    except ValidationError as e:
        raise BadRequest(description='The input was not valid') from e

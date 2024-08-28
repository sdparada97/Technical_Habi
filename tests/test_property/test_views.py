# Third party
import pytest
from werkzeug.exceptions import BadRequest, NotFound
from werkzeug.wrappers import Request

# First party
from app.views.property import get_properties

test_cases = [
    ({"status": [3], "city": ["bogota"], "year": ["2021"]}, 200),
    pytest.param(
        {"status": ["2"], "city": ["bogota"], "year": ["2024"]},
        400,
        marks=pytest.mark.xfail(raises=BadRequest),
    ),
    pytest.param(
        {"status": [3], "city": ["derfgrg"], "year": ["5"]},
        404,
        marks=pytest.mark.xfail(raises=NotFound),
    ),
]


@pytest.mark.parametrize("body_params, expected", test_cases)
def test_get_properties(body_params, expected):
    request = Request.from_values(method='POST', json=body_params)
    if expected == 200:
        response = get_properties(request)
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        assert response.get_json()
    elif expected == 400:
        with pytest.raises(BadRequest):
            get_properties(request)
    elif expected == 404:
        with pytest.raises(NotFound):
            get_properties(request)

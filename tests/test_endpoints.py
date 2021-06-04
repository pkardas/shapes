import json

import pytest
from starlette.testclient import TestClient

from shapes import app
from tests.test_factories import DrawingFactory

# Dumping to JSON and loading to dict solves issue with Color encoding:
_valid_request = json.loads(DrawingFactory.create().json())
# Request with missing fields:
_invalid_request = {"width": 700, "height": 500}


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.parametrize(
    "payload, expected_status_code", [
        (_valid_request, 200),
        (_invalid_request, 422)
    ]
)
def test_drawings(payload, expected_status_code, client):
    response = client.post("/drawings", json=payload)

    assert response.status_code == expected_status_code

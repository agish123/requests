import pytest
import requests

def test_full_workflow():
    """Test GET with headers, params, and response parsing."""
    headers = {"Accept": "application/json"}
    params = {"id": "123"}
    response = requests.get("http://httpbin.org/get", headers=headers, params=params)
    assert response.status_code == 200
    assert response.json()["args"]["id"] == "123"
    assert response.json()["headers"]["Accept"] == "application/json"
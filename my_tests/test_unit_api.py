import pytest
import requests

def test_get_success():
    """Test successful GET request."""
    response = requests.get("http://httpbin.org/get")
    assert response.status_code == 200
    assert "json" in response.headers["Content-Type"]

def test_post_data():
    """Test POST with data."""
    data = {"key": "value"}
    response = requests.post("http://httpbin.org/post", data=data)
    assert response.status_code == 200
    assert response.json()["form"] == data

def test_get_timeout():
    """Test GET with timeout exception."""
    with pytest.raises(requests.exceptions.Timeout):
        requests.get("http://httpbin.org/delay/5", timeout=1)
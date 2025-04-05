import pytest
import requests

def test_session_headers():
    """Test Session persists headers."""
    session = requests.Session()
    session.headers["User-Agent"] = "TestAgent"
    response = session.get("http://httpbin.org/get")
    assert response.json()["headers"]["User-Agent"] == "TestAgent"

def test_session_auth():
    """Test Session with basic auth."""
    session = requests.Session()
    session.auth = ("user", "pass")
    response = session.get("http://httpbin.org/basic-auth/user/pass")
    assert response.status_code == 200
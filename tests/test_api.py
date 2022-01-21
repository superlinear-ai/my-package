"""Test My Package REST API."""

from fastapi.testclient import TestClient

from my_package.api import app

client = TestClient(app)


def test_read_root() -> None:
    """Test that reading the root is successful."""
    response = client.get("/")
    assert response.status_code == 200

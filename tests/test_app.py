import pytest
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture
def client():
    # Arrange: Set up the TestClient for each test
    return TestClient(app)

# Example in-memory data reset fixture (if needed)
@pytest.fixture(autouse=True)
def reset_data():
    # If your app uses in-memory data, reset it here
    # e.g., src.app.activities.clear() or similar
    pass

def test_get_activities(client):
    # Arrange: (Any setup if needed)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Check that at least one known activity is present
    assert "Chess Club" in data
    assert "description" in data["Chess Club"]

# Add more tests for signup and unregister endpoints following AAA pattern

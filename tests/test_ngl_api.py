import pytest
from app import app  # Import the Flask app instance from app.py

# Create a pytest fixture for setting up the Flask test client
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable testing mode in Flask
    with app.test_client() as client:
        yield client

# Test the /api/submit endpoint
def test_submit_to_ngl(client):
    # Sample data for the POST request
    data = {
        'username': 'test_user',
        'question': 'What is Flask?',
        'deviceId': '1234abcd',
        'gameSlug': 'game_example',
        'referrer': 'test_referrer'
    }

    # Send a POST request to the /api/submit endpoint
    response = client.post('/api/submit', data=data)

    # Assert the status code of the response is 200 (OK)
    assert response.status_code == 200

    # Assert the response JSON contains the 'error' key, indicating failure
    json_data = response.get_json()
    assert 'error' in json_data  # Expecting an error if something goes wrong

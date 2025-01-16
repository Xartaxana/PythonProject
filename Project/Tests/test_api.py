import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from unittest.mock import patch
from Project.Core.logger import get_logger

# Initialize the logger
logger = get_logger(__name__)
logger.info(" API logger initialized successfully!")
logger.info("This is an info message.")
logger.debug("This is a debug message.")


base_url = "https://jsonplaceholder.typicode.com/"


@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}


@pytest.mark.api
def test_get_request(headers):
    """Test to validate that the GET method fetches data as expected."""
    logger.debug("Starting log for test_get_request")
    response = requests.get(f"{base_url}/posts/1", headers=headers)
    assert response.status_code == 200
    assert "userId" in response.json()
    logger.debug("test_get_request successfully passed")


user_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "id", "body"],
}


@pytest.mark.api
def test_post_request(headers):
    """Test to validate that the POST method creates data according to schema."""
    logger.debug("Starting log for test_post_request")
    payload = {"body": "bar", "userId": 1}
    response = requests.post(f"{base_url}/posts", json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["body"] == "bar"
    post_data = response.json()
    validate(instance=post_data, schema=user_schema)
    logger.debug("test_post_request successfully passed")


@pytest.mark.api
def test_post_with_validation_error(headers):
    """Test to validate that schema validation work as expected."""
    logger.debug("Starting log for test_post_with_validation_error")
    payload = {"title": "lalala", "userId": 2}
    response = requests.post(f"{base_url}/posts", json=payload, headers=headers)
    assert response.status_code == 201
    post_data = response.json()
    try:
        validate(instance=post_data, schema=user_schema)
        logger.debug("Response was successfully validated")
    except ValidationError as e:
        logger.error("An error occurred while validating the response.")
        print(e)


@pytest.mark.api
@patch('requests.get')
def test_mocked_response_in_put_request(mock_get, headers):
    """Test to validate that the PUT method update data with new data from mocks."""
    logger.debug("Starting log for test_mocked_response_in_put_request")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"title": "Mocked Title", "body": "Mocked body", "userId": 3}
    mocked_response = requests.get(f"{base_url}/posts/1")
    # PUT mocked data in real DB
    put_response = requests.put(f"{base_url}/posts/1", json=mocked_response.json(), headers=headers)
    assert put_response.status_code == 200
    assert put_response.json()["title"] == "Mocked Title"
    assert put_response.json()["userId"] == 3
    logger.debug("test_mocked_response_in_put_request successfully passed")

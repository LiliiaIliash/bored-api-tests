import pytest
import requests

BASE_URL = "https://bored-api.appbrewery.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def session():
    with requests.Session() as s:
        yield s

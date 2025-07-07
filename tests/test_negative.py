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

@pytest.mark.parametrize("params", [
    {"participants": 0},
    {"type": "unknown"},
    {"type": "social", "participants": 999}
])
def test_invalid_filters(session, base_url, params):
    resp = session.get(f"{base_url}/filter", params=params)
    assert resp.status_code == 404
    assert resp.json().get("error") == "Activities not found for the given filter."


import pytest

@pytest.mark.parametrize("params", [
    {"participants": 0},
    {"type": "unknown"},
    {"type": "social", "participants": 999}
])
def test_invalid_filters(session, base_url, params):
    resp = session.get(f"{base_url}/filter", params=params)
    assert resp.status_code == 404
    assert resp.json().get("error") == "Activities not found for the given filter."


from jsonschema import validate
from pathlib import Path
import pytest
import json

SCHEMA = json.loads(
    (Path(__file__).parent.parent / "schemas" / "activity_schema.json").read_text()
)

@pytest.mark.parametrize("params", [
    {"type": "education"},
    {"participants": 2},
    {"participants": 1, "type": "social"},
    {"price": 0},
    {"availability": 0.1}
])
def test_filter_activity(session, base_url, params):
    resp = session.get(f"{base_url}/filter", params=params, timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list) and data, "Filter returned empty list"

    for item in data:
        validate(instance=item, schema=SCHEMA)
        if "type" in params:
            assert item["type"] == params["type"]
        if "participants" in params:
            assert item["participants"] == params["participants"]

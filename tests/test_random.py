
from jsonschema import validate
from pathlib import Path
import pytest
import json

schema_path = Path(__file__).parent.parent / "schemas" / "activity_schema.json"
schema = json.loads(schema_path.read_text())

@pytest.mark.smoke
def test_random_activity(session, base_url):
    r = session.get(f"{base_url}/random", timeout=5)
    assert r.status_code == 200
    assert r.headers["Content-Type"].startswith("application/json")
    validate(instance=r.json(), schema=schema)


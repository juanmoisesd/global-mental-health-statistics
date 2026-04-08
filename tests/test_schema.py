import json
import os

def test_schema_exists():
    assert os.path.exists("schema.json")

def test_schema_is_valid_json():
    with open("schema.json", "r") as f:
        data = json.load(f)
        assert "type" in data

#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "config" / "settings.schema.json"
DEFAULT_PROFILE_PATH = ROOT / "config" / "profiles" / "default.json"
ONBOARDING_PATH = ROOT / "config" / "onboarding.flow.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return data


def validate_required(schema: dict[str, Any], data: dict[str, Any], label: str) -> None:
    for key in schema.get("required", []):
        if key not in data:
            fail(f"{label} missing required setting: {key}")


def validate_node(schema: dict[str, Any], data: Any, path: str) -> None:
    expected_type = schema.get("type")
    if expected_type == "object":
        if not isinstance(data, dict):
            fail(f"{path} must be an object")
        validate_required(schema, data, path)
        if schema.get("additionalProperties") is False:
            allowed = set((schema.get("properties") or {}).keys())
            extra = set(data.keys()) - allowed
            if extra:
                fail(f"{path} contains unsupported settings: {sorted(extra)}")
        for key, value in data.items():
            child = (schema.get("properties") or {}).get(key)
            if isinstance(child, dict):
                validate_node(child, value, f"{path}.{key}")
        return
    if expected_type == "string" and not isinstance(data, str):
        fail(f"{path} must be a string")
    if expected_type == "boolean" and not isinstance(data, bool):
        fail(f"{path} must be a boolean")
    if "enum" in schema and data not in schema["enum"]:
        fail(f"{path} has unsupported value: {data}")
    if isinstance(data, str) and schema.get("minLength") and len(data) < int(schema["minLength"]):
        fail(f"{path} must not be empty")


def validate_onboarding(path: Path, schema: dict[str, Any]) -> None:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        fail(f"PyYAML is required to validate onboarding flow: {exc}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("onboarding flow must be a mapping")
    presets = data.get("presets")
    if not isinstance(presets, list) or len(presets) < 6:
        fail("onboarding flow must define six presets")
    mode_enum = set(schema["properties"]["research_mode"]["enum"])
    view_enum = set(schema["properties"]["output_view"]["enum"])
    seen_ids: set[str] = set()
    for item in presets:
        if not isinstance(item, dict):
            fail("each preset must be a mapping")
        for key in ["id", "label", "research_mode", "output_view"]:
            if key not in item:
                fail(f"preset missing required key: {key}")
        if item["id"] in seen_ids:
            fail(f"duplicate preset id: {item['id']}")
        seen_ids.add(str(item["id"]))
        if item["research_mode"] not in mode_enum:
            fail(f"preset {item['id']} has unsupported research_mode")
        if item["output_view"] not in view_enum:
            fail(f"preset {item['id']} has unsupported output_view")


def main() -> None:
    schema = load_json(SCHEMA_PATH)
    profile = load_json(DEFAULT_PROFILE_PATH)
    validate_required(schema, profile, "default profile")
    validate_node(schema, profile, "settings")
    validate_onboarding(ONBOARDING_PATH, schema)
    print("OK: settings validation passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Repository sanity checks for the stock research skill."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'SKILL.md',
    'README.md',
    'LICENSE',
    'requirements.txt',
    'config/settings.schema.json',
    'config/profiles/default.json',
    'references/business-model-framework.md',
    'references/evidence-indexing-framework.md',
    'references/incremental-refresh-framework.md',
    'references/opportunity-discovery-framework.md',
    'references/profit-cash-flow-quality-framework.md',
    'references/quality-calibration-loop.md',
    'references/report-style-patterns.md',
    'references/scorecard-decision-framework.md',
    'references/short-seller-risk-framework.md',
    'references/technical-analysis-framework.md',
    'references/user-intake-settings-framework.md',
    'references/valuation-framework.md',
    'scripts/validate_report_output.py',
    'scripts/validate_research_manifest.py',
    'scripts/validate_report_against_manifest.py',
]

REQUIRED_SKILL_PHRASES = [
    'source-backed public-company',
    'evidence register',
    'Do not provide personalized financial advice',
    'Separate verified facts, calculations, estimates, and interpretation',
]


def fail(message: str) -> None:
    print(f'ERROR: {message}', file=sys.stderr)
    raise SystemExit(1)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def check_required_files() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    if missing:
        fail('missing required files: ' + ', '.join(missing))


def check_skill() -> None:
    text = read('SKILL.md')
    if not text.startswith('---\n'):
        fail('SKILL.md must start with YAML frontmatter')
    for phrase in REQUIRED_SKILL_PHRASES:
        if phrase not in text:
            fail(f'SKILL.md missing required phrase: {phrase}')


def check_manifest() -> None:
    data = json.loads(read('skill_manifest.json'))
    if data.get('entrypoint') != 'SKILL.md':
        fail('skill_manifest.json entrypoint must be SKILL.md')
    for command in data.get('health_commands', []):
        parts = command.split()
        if len(parts) >= 2 and parts[1].startswith('scripts/'):
            if not (ROOT / parts[1]).exists():
                fail(f'manifest command points to missing script: {parts[1]}')


def main() -> None:
    check_required_files()
    check_skill()
    check_manifest()
    print('OK: stock research skill sanity checks passed')


if __name__ == '__main__':
    main()

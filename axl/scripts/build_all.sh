#!/usr/bin/env bash
# Rebuild every derived data file in order. Run from anywhere. Requires node deps in axl/tools (npm ci) and jsonschema.
set -euo pipefail
cd "$(dirname "$0")/../.."
python3 axl/scripts/refetch_sources.py --init
python3 axl/scripts/extract_legacy.py
python3 axl/scripts/build_sources.py && python3 axl/scripts/lineage.py
python3 axl/scripts/build_claims.py
python3 axl/scripts/apply_receipts.py
python3 axl/scripts/build_definitions.py
python3 axl/scripts/build_verbs.py
python3 axl/scripts/validate_atlas.py
python3 axl/scripts/build_atlas.py

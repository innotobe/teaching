#!/usr/bin/env bash
# Regenerate the index and push everything. Usage: ./publish.sh ["commit message"]
set -e
cd "$(dirname "$0")"
python3 make_index.py
git add -A
git commit -m "${1:-Update lecture materials}" || { echo "Nothing to publish."; exit 0; }
git push

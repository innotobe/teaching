#!/usr/bin/env bash
# Commit and push everything; GitHub Pages rebuilds the index. Usage: ./publish.sh ["commit message"]
set -e
cd "$(dirname "$0")"
git add -A
git commit -m "${1:-Update lecture materials}" || { echo "Nothing to publish."; exit 0; }
git push

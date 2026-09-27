#!/usr/bin/env bash
# Scaffold a new white-label brand: ./new-brand.sh <business-slug> [--no-activate]
set -euo pipefail
SLUG="${1:-}"
NO_ACTIVATE=0
if [[ "${2:-}" == "--no-activate" ]]; then
  NO_ACTIVATE=1
fi
if [[ -z "$SLUG" ]]; then
  echo "Usage: ./new-brand.sh <business-slug> [--no-activate]"
  echo "Example: ./new-brand.sh joes-pizza-tampa"
  exit 1
fi
DEST="agency/brands/$SLUG"
if [[ -e "$DEST" ]]; then
  echo "Brand '$SLUG' already exists at $DEST"
  exit 1
fi
cp -r agency/brands/_template "$DEST"
if [[ "$NO_ACTIVATE" -eq 1 ]]; then
  echo "Brand '$SLUG' created (ACTIVE unchanged)."
else
  echo "$SLUG" > agency/brands/ACTIVE
  echo "Brand '$SLUG' created and set ACTIVE."
fi
echo "Next: fill in the files in $DEST/"
ls "$DEST"

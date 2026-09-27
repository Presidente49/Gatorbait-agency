#!/usr/bin/env bash
# Scaffold a new white-label brand: ./new-brand.sh <business-slug>
set -euo pipefail
SLUG="${1:-}"
if [[ -z "$SLUG" ]]; then
  echo "Usage: ./new-brand.sh <business-slug>"
  echo "Example: ./new-brand.sh joes-pizza-tampa"
  exit 1
fi
DEST="agency/brands/$SLUG"
if [[ -e "$DEST" ]]; then
  echo "Brand '$SLUG' already exists at $DEST"
  exit 1
fi
cp -r agency/brands/_template "$DEST"
echo "$SLUG" > agency/brands/ACTIVE
echo "Brand '$SLUG' created and set ACTIVE."
echo "Next: fill in the files in $DEST/"
ls "$DEST"

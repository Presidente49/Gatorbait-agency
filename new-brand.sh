#!/usr/bin/env bash
# Scaffold a new white-label brand:
#   ./new-brand.sh <business-slug> ["Business Display Name"] [--no-activate]
# Works from any directory. Does not overwrite an existing brand.
# --no-activate creates the brand without switching agency/brands/ACTIVE.
set -euo pipefail
cd "$(dirname "$0")"

SLUG=""
NAME=""
NO_ACTIVATE=0
for arg in "$@"; do
  if [[ "$arg" == "--no-activate" ]]; then
    NO_ACTIVATE=1
  elif [[ -z "$SLUG" ]]; then
    SLUG="$arg"
  elif [[ -z "$NAME" ]]; then
    NAME="$arg"
  fi
done
if [[ -z "$SLUG" ]]; then
  echo "Usage: ./new-brand.sh <business-slug> [\"Business Display Name\"] [--no-activate]"
  echo "Example: ./new-brand.sh joes-pizza-tampa \"Joe's Pizza Tampa\""
  exit 1
fi
# Lowercase letters, digits and single hyphens only — no paths, no dots,
# no leading underscore (reserved for _template).
if [[ ! "$SLUG" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "Invalid slug '$SLUG': use lowercase letters, digits and hyphens (e.g. joes-pizza-tampa)."
  exit 1
fi
DEST="agency/brands/$SLUG"
if [[ -e "$DEST" ]]; then
  echo "Brand '$SLUG' already exists at $DEST"
  exit 1
fi

mkdir -p "$DEST"
# Copy the brand files, not the template's own README (agents read every
# .md in the brand folder; the template instructions must not become brand facts).
for f in agency/brands/_template/*.md; do
  [[ "$(basename "$f")" == "README.md" ]] && continue
  cp "$f" "$DEST/"
done
mkdir -p "$DEST/outputs"
touch "$DEST/outputs/.gitkeep"

if [[ -n "$NAME" ]]; then
  ESCAPED=$(printf '%s' "$NAME" | sed 's/[&/\]/\\&/g')
  for f in "$DEST"/*.md; do
    sed -i.bak "s/\[Business Name\]/$ESCAPED/g" "$f" && rm -f "$f.bak"
  done
fi

if [[ "$NO_ACTIVATE" -eq 1 ]]; then
  echo "Brand '$SLUG' created (ACTIVE unchanged)."
else
  PREV="$(cat agency/brands/ACTIVE 2>/dev/null || true)"
  echo "$SLUG" > agency/brands/ACTIVE
  echo "Brand '$SLUG' created and set ACTIVE (was: ${PREV:-none})."
  echo "Switch back any time: echo \"$PREV\" > agency/brands/ACTIVE"
fi
echo "Next: fill in the files in $DEST/ — start with about.md (who approves what)."
ls "$DEST"

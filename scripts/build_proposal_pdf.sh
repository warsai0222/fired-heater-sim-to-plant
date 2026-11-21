#!/usr/bin/env bash
# Rebuild docs/fired_heater_project_proposal.pdf from the markdown source.
# Requires: pandoc, and Google Chrome (headless) for printing.
# Run from the repository root:  ./scripts/build_proposal_pdf.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/docs/fired_heater_project_proposal.md"
CSS="$ROOT/docs/proposal.css"
HTML="$(mktemp -d)/proposal.html"
OUT="$ROOT/docs/fired_heater_project_proposal.pdf"

# Locate Chrome (macOS app bundle, then PATH).
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  CHROME="$(command -v google-chrome || command -v chromium || true)"
fi
[ -n "$CHROME" ] || { echo "Google Chrome not found" >&2; exit 1; }

pandoc "$SRC" --from=gfm --to=html5 --standalone --metadata title="" \
  --css="file://$CSS" --output="$HTML"

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT" "file://$HTML" >/dev/null 2>&1

echo "wrote $OUT"

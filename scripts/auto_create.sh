#!/usr/bin/env bash
set -euo pipefail

# Requires inotifywait (Linux) or fswatch (macOS). Tries either.
WATCH_ROOTS=("docs" "communications")
TOOL=""
if command -v inotifywait >/dev/null 2>&1; then
  TOOL="inotifywait"
elif command -v fswatch >/dev/null 2>&1; then
  TOOL="fswatch"
else
  echo "Please install inotify-tools (Linux) or fswatch (macOS) to enable watching." >&2
  echo "You can still manually create records: scripts/new_record.py <file> ..." >&2
  exit 1
fi

echo "Auto-create watcher running. Drop files into: ${WATCH_ROOTS[*]}"
echo "Press Ctrl+C to stop."

create_or_update() {
  local f="$1"
  # Ignore temp files
  [[ "$f" =~ (^|/)\. ]] && return 0
  [[ "$f" =~ \.swp$|~$|\.tmp$ ]] && return 0
  if [ -f "$f" ]; then
    echo "Creating record for: $f"
    scripts/new_record.py "$f" --status draft || true
    # Update checksums and validate
    python3 scripts/update_attachments.py || true
    bash scripts/validate.sh || true
  fi
}

if [ "$TOOL" = "inotifywait" ]; then
  inotifywait -m -r -e close_write,move,create --format "%w%f" "${WATCH_ROOTS[@]}" | while read -r path; do
    create_or_update "$path"
  done
else
  fswatch -0 -r "${WATCH_ROOTS[@]}" | while IFS= read -r -d "" path; do
    create_or_update "$path"
  done
fi

#!/usr/bin/env bash
set -euo pipefail
if [ $# -lt 2 ]; then
  echo "Usage: scripts/attach.sh <record.yaml> <path> [description...]"
  exit 1
fi
rec="$1"; shift
path="$1"; shift
desc="${*:-Attached file}"
if [ ! -f "$rec" ]; then
  echo "Record not found: $rec" >&2; exit 1
fi
mkdir -p "$(dirname "$path")"
if ! grep -q "^attachments:" "$rec"; then
  printf "\nattachments:\n" >> "$rec"
fi
printf "  - path: %s\n    description: %s\n" "$path" "$desc" >> "$rec"
echo "Added attachment entry to $rec"
echo "Run: python3 scripts/update_attachments.py"

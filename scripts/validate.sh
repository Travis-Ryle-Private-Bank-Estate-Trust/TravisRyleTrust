#!/usr/bin/env bash
set -euo pipefail
fail=0

if command -v yq >/dev/null 2>&1; then
  for f in records/*.y*ml; do
    [ -e "$f" ] || continue
    if ! yq ".id and .title and .created_at" "$f" >/dev/null; then
      echo "Invalid required fields: $f" >&2
      fail=1
    fi
  done
else
  echo "yq not installed; skipping YAML schema checks." >&2
fi

python3 - << "PYEOF" || fail=1
import os, glob, hashlib, yaml, sys
def sha256(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
errors=0
for f in sorted(glob.glob("records/*.yml")+glob.glob("records/*.yaml")):
    with open(f,"r",encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    for att in data.get("attachments") or []:
        p=(att.get("path") or "").strip()
        if not p: 
            continue
        if not os.path.isfile(p):
            print(f"[missing] {f}: {p}"); errors+=1; continue
        if "sha256" in att and att["sha256"] != sha256(p):
            print(f"[checksum-mismatch] {f}: {p}"); errors+=1
        if "bytes" in att and att["bytes"] != os.path.getsize(p):
            print(f"[size-mismatch] {f}: {p}"); errors+=1
if errors: sys.exit(1)
PYEOF

exit $fail

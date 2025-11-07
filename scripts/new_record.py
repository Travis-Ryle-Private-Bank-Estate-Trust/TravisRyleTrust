#!/usr/bin/env python3
import sys, os, uuid, datetime as dt, yaml, hashlib

ALLOWED_ROOTS = {"docs", "communications"}

def now_iso():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def normalize(p): return p.replace("\\", "/")

def build_attachment(path, description=None):
    path = normalize(path)
    att = {"path": path, "description": description or os.path.basename(path)}
    if os.path.isfile(path):
        att["exists"] = True
        att["bytes"] = os.path.getsize(path)
        att["sha256"] = sha256(path)
    else:
        att["exists"] = False
    return att

def safe_title_from_paths(paths):
    base = os.path.basename(paths[0])
    name, _ = os.path.splitext(base)
    # Trim overly long titles
    return (name.replace("_", " ").replace("-", " ")).strip()[:120] or "New Record"

def write_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: scripts/new_record.py <file1> [file2 ...] [--title \"Title\"] [--status draft|active] [--notes \"note text\"]", file=sys.stderr)
        return 2

    # Parse args
    args = sys.argv[1:]
    files = []
    title = None
    status = "draft"
    notes = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--title":
            i += 1; title = args[i]
        elif a == "--status":
            i += 1; status = args[i]
        elif a == "--notes":
            i += 1; notes.append(args[i])
        else:
            files.append(a)
        i += 1

    if not files:
        print("No files provided.", file=sys.stderr)
        return 2

    # Validate locations and normalize
    norm_files = []
    for p in files:
        p = normalize(p)
        root = p.split("/", 1)[0]
        if root not in ALLOWED_ROOTS:
            print(f"Skipping non-allowed path: {p} (allowed roots: {sorted(ALLOWED_ROOTS)})", file=sys.stderr)
            continue
        norm_files.append(p)

    if not norm_files:
        print("No valid files under allowed roots.", file=sys.stderr)
        return 2

    rec_id = str(uuid.uuid4())
    ts = now_iso()
    title = title or safe_title_from_paths(norm_files)

    record = {
        "id": rec_id,
        "title": title,
        "created_at": ts,
        "status": status,
        "notes": notes or ["Auto-created from files"],
        "metadata": {"source": "auto-create", "version": 1},
        "attachments": [build_attachment(p) for p in norm_files],
    }

    # Filename for record
    date_prefix = ts[:10]
    safe_title = "".join(c if c.isalnum() or c in ("-", "_") else "-" for c in title.lower().replace(" ", "-"))
    out = f"records/{date_prefix}-{safe_title or rec_id[:8]}.yaml"
    # Ensure unique
    base = out
    n = 2
    while os.path.exists(out):
        out = base.replace(".yaml", f"-{n}.yaml")
        n += 1

    write_yaml(out, record)
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

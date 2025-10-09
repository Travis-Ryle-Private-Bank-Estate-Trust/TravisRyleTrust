#!/usr/bin/env python3
import os, glob, hashlib, yaml

ALLOWED_ROOTS = {"docs", "communications"}

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def normalize(p): return p.replace("\\", "/")

def process_record(path):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    atts = data.get("attachments")
    if not atts:
        return False
    updated = False
    for att in atts:
        p = normalize(att.get("path","")).strip()
        if not p: 
            continue
        root = p.split("/",1)[0]
        if root not in ALLOWED_ROOTS:
            continue
        if not os.path.isfile(p):
            if att.get("exists") is not False:
                att["exists"] = False; updated = True
            continue
        size = os.path.getsize(p)
        digest = sha256(p)
        if att.get("exists") is not True:
            att["exists"] = True; updated = True
        if att.get("bytes") != size:
            att["bytes"] = size; updated = True
        if att.get("sha256") != digest:
            att["sha256"] = digest; updated = True
    if updated:
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
    return updated

def main():
    changed = False
    for rec in sorted(glob.glob("records/*.yml")+glob.glob("records/*.yaml")):
        if process_record(rec):
            print("updated:", rec); changed = True
    print("changes written" if changed else "no changes")

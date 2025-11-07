#!/usr/bin/env python3
"""
Track sent emails by creating a record with metadata.
Usage: scripts/track_email.py <email_file> --to <recipient> --subject "Subject" [options]
"""
import sys, os, datetime as dt, yaml, hashlib, uuid

def now_iso():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def normalize(p): 
    return p.replace("\\", "/")

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

def write_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: scripts/track_email.py <email_file> --to <recipient> --subject \"Subject\" [--cc <cc>] [--date YYYY-MM-DD] [--notes \"note\"]", file=sys.stderr)
        return 2

    # Parse arguments
    args = sys.argv[1:]
    email_file = None
    to_recipient = None
    subject = None
    cc_recipients = []
    sent_date = None
    notes = []
    
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--to":
            i += 1
            if i >= len(args):
                print("Error: --to requires a value", file=sys.stderr)
                return 2
            to_recipient = args[i]
        elif arg == "--subject":
            i += 1
            if i >= len(args):
                print("Error: --subject requires a value", file=sys.stderr)
                return 2
            subject = args[i]
        elif arg == "--cc":
            i += 1
            if i >= len(args):
                print("Error: --cc requires a value", file=sys.stderr)
                return 2
            cc_recipients.append(args[i])
        elif arg == "--date":
            i += 1
            if i >= len(args):
                print("Error: --date requires a value", file=sys.stderr)
                return 2
            sent_date = args[i]
        elif arg == "--notes":
            i += 1
            if i >= len(args):
                print("Error: --notes requires a value", file=sys.stderr)
                return 2
            notes.append(args[i])
        elif not email_file:
            email_file = arg
        i += 1

    # Validate required fields
    if not email_file:
        print("Error: Email file path is required", file=sys.stderr)
        return 2
    
    if not to_recipient:
        print("Error: --to recipient is required", file=sys.stderr)
        return 2
    
    if not subject:
        print("Error: --subject is required", file=sys.stderr)
        return 2

    # Normalize and validate path to prevent directory traversal
    email_file = normalize(email_file)
    abs_email_file = os.path.abspath(email_file)
    abs_emails_dir = os.path.abspath("communications/emails")
    
    # Validate that file is in communications/emails/ directory
    if not abs_email_file.startswith(abs_emails_dir + os.sep):
        print(f"Error: Email file must be in communications/emails/ directory", file=sys.stderr)
        print(f"Provided path: {email_file}", file=sys.stderr)
        return 2
    
    # Create record
    rec_id = str(uuid.uuid4())
    ts = now_iso()
    sent_date = sent_date or ts[:10]
    
    record = {
        "id": rec_id,
        "type": "email",
        "title": f"Email: {subject}",
        "created_at": ts,
        "status": "sent",
        "email_metadata": {
            "to": to_recipient,
            "cc": cc_recipients if cc_recipients else [],
            "subject": subject,
            "sent_date": sent_date,
        },
        "notes": notes if notes else [f"Email sent to {to_recipient}"],
        "metadata": {"source": "track_email", "version": 1},
        "attachments": [build_attachment(email_file, f"Email to {to_recipient}")],
    }

    # Create filename for record
    safe_subject = "".join(c if c.isalnum() or c in ("-", "_") else "-" for c in subject.lower().replace(" ", "-"))[:50]
    safe_recipient = "".join(c if c.isalnum() or c in ("-", "_") else "-" for c in to_recipient.split("@")[0].lower())[:30]
    out = f"records/{sent_date}-email-{safe_recipient}-{safe_subject}.yaml"
    
    # Ensure unique filename
    base = out
    n = 2
    while os.path.exists(out):
        out = base.replace(".yaml", f"-{n}.yaml")
        n += 1

    # Ensure records directory exists
    os.makedirs("records", exist_ok=True)
    
    write_yaml(out, record)
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

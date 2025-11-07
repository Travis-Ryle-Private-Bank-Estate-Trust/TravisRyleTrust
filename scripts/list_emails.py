#!/usr/bin/env python3
"""
List all tracked emails from the records directory.
Usage: scripts/list_emails.py [--format json|table]
"""
import sys, glob, yaml
from datetime import datetime

def main():
    format_type = "table"
    if len(sys.argv) > 1 and sys.argv[1] == "--format" and len(sys.argv) > 2:
        format_type = sys.argv[2]
    
    emails = []
    for record_file in sorted(glob.glob("records/*.yaml") + glob.glob("records/*.yml")):
        try:
            with open(record_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            
            if data.get("type") == "email":
                email_meta = data.get("email_metadata", {})
                emails.append({
                    "date": email_meta.get("sent_date", "Unknown"),
                    "to": email_meta.get("to", "Unknown"),
                    "cc": ", ".join(email_meta.get("cc", [])),
                    "subject": email_meta.get("subject", "No subject"),
                    "status": data.get("status", "unknown"),
                    "record": record_file
                })
        except Exception as e:
            print(f"Error reading {record_file}: {e}", file=sys.stderr)
    
    if format_type == "json":
        import json
        print(json.dumps(emails, indent=2))
    else:
        # Table format
        if not emails:
            print("No tracked emails found.")
            return 0
        
        print(f"\n{'Date':<12} {'To':<30} {'Subject':<40} {'Status':<10}")
        print("-" * 95)
        for email in emails:
            subject = email['subject'][:37] + "..." if len(email['subject']) > 40 else email['subject']
            to = email['to'][:27] + "..." if len(email['to']) > 30 else email['to']
            print(f"{email['date']:<12} {to:<30} {subject:<40} {email['status']:<10}")
        
        print(f"\nTotal emails tracked: {len(emails)}\n")
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

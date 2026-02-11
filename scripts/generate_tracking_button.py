#!/usr/bin/env python3
"""
Generate an HTML tracking button for email records.

Usage: 
    python3 scripts/generate_tracking_button.py <record_file.yaml>
    python3 scripts/generate_tracking_button.py --record-id <record-id>
"""

import sys
import os
import yaml
import urllib.parse

# Public Ledge URL base
PUBLIC_LEDGE_URL = "https://www.lawfully-illegal.com/public-ledge"


def load_record(record_path):
    """Load a YAML record file."""
    try:
        with open(record_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading record: {e}", file=sys.stderr)
        return None


def find_record_by_id(record_id):
    """Find a record file by its ID."""
    import glob
    pattern = "records/**/*.yaml"
    for filepath in glob.glob(pattern, recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data and data.get('id') == record_id:
                    return filepath, data
        except Exception:
            continue
    return None, None


def generate_tracking_url(record_id, record_data):
    """Generate tracking URL with record metadata."""
    # Build query parameters
    params = {
        'record_id': record_id,
        'type': record_data.get('type', 'email'),
    }
    
    # Add email metadata if available
    if 'email_metadata' in record_data:
        email_meta = record_data['email_metadata']
        params['subject'] = email_meta.get('subject', '')
        params['date'] = email_meta.get('sent_date', '')
    
    # URL encode parameters
    query_string = urllib.parse.urlencode(params)
    tracking_url = f"{PUBLIC_LEDGE_URL}?{query_string}"
    
    return tracking_url


def generate_html_button(tracking_url, button_text="View Evidence on Public Ledge"):
    """Generate HTML button code."""
    html = f"""
<!-- Email Tracking Button -->
<div style="margin: 30px 0; padding: 20px; background-color: #f5f5f5; border-radius: 5px; text-align: center;">
    <p style="margin: 0 0 15px 0; color: #666; font-size: 14px;">
        This correspondence is tracked and verified on the public ledger.
    </p>
    <a href="{tracking_url}" 
       style="display: inline-block; padding: 12px 30px; background-color: #0066cc; 
              color: white; text-decoration: none; border-radius: 4px; 
              font-weight: bold; font-size: 16px;"
       target="_blank">
        {button_text}
    </a>
    <p style="margin: 15px 0 0 0; color: #999; font-size: 12px;">
        Record ID: <code style="background: #fff; padding: 2px 6px; border-radius: 3px;">{tracking_url.split('record_id=')[1].split('&')[0] if 'record_id=' in tracking_url else 'N/A'}</code>
    </p>
</div>
"""
    return html


def generate_plain_text_link(tracking_url):
    """Generate plain text version of tracking link."""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 VIEW EVIDENCE ON PUBLIC LEDGER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This correspondence is tracked and verified on the public ledger.
Click the link below to view the evidence:

{tracking_url}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/generate_tracking_button.py <record_file.yaml>")
        print("   or: python3 scripts/generate_tracking_button.py --record-id <record-id>")
        return 2
    
    # Parse arguments
    record_path = None
    record_id = None
    record_data = None
    
    if sys.argv[1] == "--record-id":
        if len(sys.argv) < 3:
            print("Error: --record-id requires a value", file=sys.stderr)
            return 2
        record_id = sys.argv[2]
        record_path, record_data = find_record_by_id(record_id)
        if not record_path:
            print(f"Error: Record with ID '{record_id}' not found", file=sys.stderr)
            return 1
    else:
        record_path = sys.argv[1]
        record_data = load_record(record_path)
        if not record_data:
            return 1
        record_id = record_data.get('id')
    
    if not record_id:
        print("Error: Record does not have an 'id' field", file=sys.stderr)
        return 1
    
    # Generate tracking URL and button
    tracking_url = generate_tracking_url(record_id, record_data)
    html_button = generate_html_button(tracking_url)
    plain_text = generate_plain_text_link(tracking_url)
    
    # Output results
    print("=" * 70)
    print("  EMAIL TRACKING BUTTON GENERATED")
    print("=" * 70)
    print(f"\nRecord File: {record_path}")
    print(f"Record ID: {record_id}")
    print(f"Record Type: {record_data.get('type', 'N/A')}")
    
    if 'email_metadata' in record_data:
        email_meta = record_data['email_metadata']
        print(f"Subject: {email_meta.get('subject', 'N/A')}")
        print(f"To: {email_meta.get('to', 'N/A')}")
        print(f"Date: {email_meta.get('sent_date', 'N/A')}")
    
    print(f"\nTracking URL: {tracking_url}")
    print("\n" + "=" * 70)
    print("  HTML BUTTON CODE (copy and paste into email)")
    print("=" * 70)
    print(html_button)
    
    print("\n" + "=" * 70)
    print("  PLAIN TEXT VERSION (for text-only emails)")
    print("=" * 70)
    print(plain_text)
    
    # Save to files
    output_dir = "/tmp/tracking-buttons"
    os.makedirs(output_dir, exist_ok=True)
    
    safe_id = record_id[:8]
    html_file = f"{output_dir}/{safe_id}-button.html"
    txt_file = f"{output_dir}/{safe_id}-link.txt"
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_button)
    
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(plain_text)
    
    print("\n" + "=" * 70)
    print(f"  Files saved:")
    print(f"  - HTML: {html_file}")
    print(f"  - Text: {txt_file}")
    print("=" * 70)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Sync with lawfully-illegal.com public ledger.

Usage:
    python3 scripts/sync_public_ledge.py         # Opens public ledge in browser
    python3 scripts/sync_public_ledge.py --url   # Just print the URL
    python3 scripts/sync_public_ledge.py --list  # List local ledger entries
"""

import sys
import os
import webbrowser
import json
import glob
import yaml

# Public Ledge URL
PUBLIC_LEDGE_URL = "https://www.lawfully-illegal.com/public-ledge"

# Local ledger configuration
LEDGER_DIR = "records/public-ledger"
LEDGER_JSON = "ledger.json"


def load_ledger_entries():
    """Load all public ledger entries from YAML files."""
    entries = []
    pattern = os.path.join(LEDGER_DIR, "LED-*.yaml")
    for filepath in sorted(glob.glob(pattern)):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data:
                    entries.append(data)
        except Exception as e:
            print(f"Warning: Could not load {filepath}: {e}")
    return entries


def print_entries(entries):
    """Print ledger entries in a formatted table."""
    if not entries:
        print("No ledger entries found.")
        return
    
    print("\n" + "=" * 100)
    print("  PUBLIC LEDGER ENTRIES")
    print("=" * 100)
    print(f"{'ID':<20} {'Action':<40} {'Party':<25} {'Status':<10}")
    print("-" * 100)
    
    for entry in entries:
        led_id = entry.get('led_id', 'N/A')
        action = entry.get('action', 'N/A')[:38]
        party = entry.get('party', 'N/A')[:23]
        status = entry.get('status', 'N/A')
        print(f"{led_id:<20} {action:<40} {party:<25} {status:<10}")
    
    print("=" * 100)
    print(f"\nTotal entries: {len(entries)}")
    print(f"Local directory: {LEDGER_DIR}/")
    print(f"Website: {PUBLIC_LEDGE_URL}")


def main():
    print("=" * 60)
    print("  Lawfully Illegal - Public Ledge Integration")
    print("=" * 60)
    print(f"\nPublic Ledge URL: {PUBLIC_LEDGE_URL}")

    # Handle command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if arg == "--url":
            print(f"\nCopy this link: {PUBLIC_LEDGE_URL}")
            return 0
        
        if arg == "--list":
            entries = load_ledger_entries()
            print_entries(entries)
            return 0
        
        print(f"Unknown option: {arg}")
        print("Options: --url, --list")
        return 1

    # Default: open in browser
    print("\nOpening public ledge in your browser...")
    try:
        webbrowser.open(PUBLIC_LEDGE_URL)
        print("Done! Check your browser.")
    except Exception as e:
        print(f"\nFailed to open browser automatically: {e}")
        print(f"Please visit: {PUBLIC_LEDGE_URL}")

    # Also list local entries
    entries = load_ledger_entries()
    if entries:
        print_entries(entries)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

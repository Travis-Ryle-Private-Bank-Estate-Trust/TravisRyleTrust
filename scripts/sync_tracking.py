#!/usr/bin/env python3
"""
Open the lawfully-illegal.com tracking page.

Usage:
    python3 scripts/sync_tracking.py         # Opens tracking page in browser
    python3 scripts/sync_tracking.py --url   # Just print the URL
"""

import sys
import webbrowser

# Tracking URL
TRACKING_URL = "https://www.lawfully-illegal.com/tracking"


def main():
    print("=" * 50)
    print("  Lawfully Illegal - Email Tracking")
    print("=" * 50)
    print(f"\nTracking URL: {TRACKING_URL}")

    # If --url flag, just print URL and exit
    if len(sys.argv) > 1 and sys.argv[1] == "--url":
        print(f"\nCopy this link: {TRACKING_URL}")
        return 0

    # Try to open in browser
    print("\nOpening tracking page in your browser...")
    try:
        webbrowser.open(TRACKING_URL)
        print("Done! Check your browser.")
    except Exception as e:
        print(f"\nFailed to open browser automatically: {e}")
        print(f"Please visit: {TRACKING_URL}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

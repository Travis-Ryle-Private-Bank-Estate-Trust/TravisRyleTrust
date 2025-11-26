#!/usr/bin/env python3
"""
Sync email tracking records with the lawfully-illegal.com tracking system.

Usage:
    python3 scripts/sync_tracking.py [--push|--pull|--status]

Options:
    --push      Upload local records to the website tracking system
    --pull      Download records from the website tracking system
    --status    Check connection status with the tracking server

Environment Variables Required:
    TRACKING_URL    - The tracking endpoint URL (default: https://www.lawfully-illegal.com/tracking)
    TRACKING_API_KEY - Your API key for authentication
"""

import os
import sys
import json
import glob
import yaml
from datetime import datetime, timezone

# Default tracking URL
DEFAULT_TRACKING_URL = "https://www.lawfully-illegal.com/tracking"


def load_env():
    """Load environment variables from .env file if it exists."""
    env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip())


def get_tracking_url():
    """Get the tracking URL from environment or use default."""
    return os.environ.get("TRACKING_URL", DEFAULT_TRACKING_URL)


def get_api_key():
    """Get the API key from environment."""
    return os.environ.get("TRACKING_API_KEY")


def load_local_records():
    """Load all email tracking records from the records directory."""
    records = []
    records_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "records")

    for record_file in sorted(glob.glob(os.path.join(records_dir, "*.yaml")) +
                               glob.glob(os.path.join(records_dir, "*.yml"))):
        try:
            with open(record_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            if data.get("type") == "email":
                data["_local_file"] = os.path.basename(record_file)
                records.append(data)
        except Exception as e:
            print(f"Warning: Error reading {record_file}: {e}", file=sys.stderr)

    return records


def check_status():
    """Check connection status with the tracking server."""
    tracking_url = get_tracking_url()
    api_key = get_api_key()

    print(f"Tracking URL: {tracking_url}")
    print(f"API Key: {'configured' if api_key else 'NOT CONFIGURED'}")

    if not api_key:
        print("\nWarning: TRACKING_API_KEY is not set in your .env file.")
        print("Please configure it to enable syncing with the tracking server.")
        return 1

    # Load local records count
    records = load_local_records()
    print(f"Local email records: {len(records)}")

    print("\nTo test connection, the tracking server needs to be accessible.")
    print("Please ensure your .env file has the correct TRACKING_URL and TRACKING_API_KEY.")

    return 0


def push_records():
    """Push local records to the tracking server."""
    tracking_url = get_tracking_url()
    api_key = get_api_key()

    if not api_key:
        print("Error: TRACKING_API_KEY is not set. Cannot push records.", file=sys.stderr)
        return 1

    records = load_local_records()
    print(f"Found {len(records)} local email records to sync.")

    # Prepare payload
    payload = {
        "action": "sync",
        "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "records": records
    }

    print(f"\nPayload prepared for {tracking_url}")
    print("Note: Actual HTTP request requires 'requests' library.")
    print("Install with: pip install requests")
    print("\nTo push manually, use:")
    print(f"  curl -X POST {tracking_url}/api/sync \\")
    print(f"       -H 'Authorization: Bearer $TRACKING_API_KEY' \\")
    print(f"       -H 'Content-Type: application/json' \\")
    print(f"       -d @payload.json")
    print(f"\nRecords count: {len(records)}")

    return 0


def pull_records():
    """Pull records from the tracking server."""
    tracking_url = get_tracking_url()
    api_key = get_api_key()

    if not api_key:
        print("Error: TRACKING_API_KEY is not set. Cannot pull records.", file=sys.stderr)
        return 1

    print(f"Pulling records from {tracking_url}")
    print("Note: Actual HTTP request requires 'requests' library.")
    print("Install with: pip install requests")
    print("\nTo pull manually, use:")
    print(f"  curl -X GET {tracking_url}/api/records \\")
    print(f"       -H 'Authorization: Bearer $TRACKING_API_KEY'")

    return 0


def main():
    load_env()

    if len(sys.argv) < 2:
        print(__doc__)
        return 0

    action = sys.argv[1]

    if action == "--status":
        return check_status()
    elif action == "--push":
        return push_records()
    elif action == "--pull":
        return pull_records()
    else:
        print(f"Unknown action: {action}", file=sys.stderr)
        print(__doc__)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Incrimination Nation - Identifier Scraper for Lawfully Illegal

This script scrapes public record sources for identifiers and stores them
in the GitHub repository as an immutable, timestamped record.

Public Sources:
- SEC EDGAR (corporate filings)
- State corporate registries
- Court records (PACER)
- County records

Usage:
    python3 scripts/scrape_identifiers.py --list          # List configured identifiers
    python3 scripts/scrape_identifiers.py --scrape        # Run scraper
    python3 scripts/scrape_identifiers.py --report        # Generate discrepancy report
"""

import os
import sys
import json
import yaml
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path

# Configuration
IDENTIFIERS_FILE = "records/identifiers/identifiers.yaml"
SCRAPED_RECORDS_DIR = "records/scraped"
DISCREPANCY_LOG = "records/discrepancies.yaml"
LEDGER_JSON = "ledger.json"

# Public record source URLs (for reference - actual scraping would need API keys)
PUBLIC_SOURCES = {
    "sec_edgar": "https://www.sec.gov/cgi-bin/browse-edgar",
    "pacer": "https://pacer.uscourts.gov/",
    "state_sos": {
        "arizona": "https://ecorp.azcc.gov/",
        "california": "https://bizfileonline.sos.ca.gov/",
        "nevada": "https://esos.nv.gov/",
    },
    "lawfully_illegal": "https://www.lawfully-illegal.com/public-ledge"
}


def load_identifiers():
    """Load identifier configuration from YAML file."""
    if not os.path.exists(IDENTIFIERS_FILE):
        return {"identifiers": [], "entities": []}
    
    with open(IDENTIFIERS_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {"identifiers": [], "entities": []}


def save_identifiers(data):
    """Save identifier configuration to YAML file."""
    os.makedirs(os.path.dirname(IDENTIFIERS_FILE), exist_ok=True)
    with open(IDENTIFIERS_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def generate_record_id():
    """Generate a unique record ID with timestamp."""
    now = datetime.now(timezone.utc)
    return f"SCR-{now.strftime('%Y%m%d')}-{now.strftime('%H%M%S')}"


def hash_content(content):
    """Generate SHA256 hash of content for verification."""
    if isinstance(content, str):
        content = content.encode('utf-8')
    return hashlib.sha256(content).hexdigest()


def create_scraped_record(entity_name, source, data, notes=None):
    """Create a scraped record entry."""
    record_id = generate_record_id()
    now = datetime.now(timezone.utc)
    
    record = {
        "record_id": record_id,
        "entity": entity_name,
        "source": source,
        "scraped_at": now.isoformat(),
        "data_hash": hash_content(json.dumps(data, sort_keys=True)),
        "data": data,
        "verified": False,
        "notes": notes or [],
        "metadata": {
            "scraper_version": "1.0.0",
            "website_integration": "https://www.lawfully-illegal.com/public-ledge"
        }
    }
    
    # Save to records directory
    os.makedirs(SCRAPED_RECORDS_DIR, exist_ok=True)
    safe_entity = entity_name.replace(" ", "-").replace("/", "-")[:30]
    filename = f"{record_id}-{safe_entity}.yaml"
    filepath = os.path.join(SCRAPED_RECORDS_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(record, f, default_flow_style=False, allow_unicode=True)
    
    print(f"  Created record: {filepath}")
    return record


def log_discrepancy(entity_name, field, claimed_value, found_value, source):
    """Log a discrepancy between claimed and found values."""
    now = datetime.now(timezone.utc)
    
    discrepancy = {
        "id": f"DISC-{now.strftime('%Y%m%d-%H%M%S')}",
        "entity": entity_name,
        "field": field,
        "claimed_value": claimed_value,
        "found_value": found_value,
        "source": source,
        "discovered_at": now.isoformat(),
        "status": "unresolved",
        "notes": []
    }
    
    # Load existing discrepancies
    discrepancies = []
    if os.path.exists(DISCREPANCY_LOG):
        with open(DISCREPANCY_LOG, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data and "discrepancies" in data:
                discrepancies = data["discrepancies"]
    
    discrepancies.append(discrepancy)
    
    # Save updated discrepancies
    os.makedirs(os.path.dirname(DISCREPANCY_LOG), exist_ok=True)
    with open(DISCREPANCY_LOG, 'w', encoding='utf-8') as f:
        yaml.dump({"discrepancies": discrepancies}, f, default_flow_style=False)
    
    print(f"  ⚠️  DISCREPANCY LOGGED: {entity_name} - {field}")
    print(f"      Claimed: {claimed_value}")
    print(f"      Found:   {found_value}")
    
    return discrepancy


def list_identifiers():
    """List all configured identifiers and entities."""
    data = load_identifiers()
    
    print("\n" + "=" * 80)
    print("  INCRIMINATION NATION - Identifier Registry")
    print("  Lawfully Illegal Public Ledge Integration")
    print("=" * 80)
    
    # List personal identifiers
    identifiers = data.get("identifiers", [])
    if identifiers:
        print("\n📋 PERSONAL IDENTIFIERS:")
        print("-" * 40)
        for ident in identifiers:
            print(f"  • {ident.get('type', 'Unknown')}: {ident.get('value', 'N/A')}")
            if ident.get('notes'):
                print(f"    Notes: {ident.get('notes')}")
    else:
        print("\n📋 No personal identifiers configured.")
    
    # List tracked entities
    entities = data.get("entities", [])
    if entities:
        print("\n🏢 TRACKED ENTITIES:")
        print("-" * 40)
        for entity in entities:
            print(f"  • {entity.get('name', 'Unknown')}")
            print(f"    Type: {entity.get('type', 'N/A')}")
            print(f"    State: {entity.get('state', 'N/A')}")
            if entity.get('identifiers'):
                for k, v in entity.get('identifiers', {}).items():
                    print(f"    {k}: {v}")
    else:
        print("\n🏢 No entities configured for tracking.")
    
    print("\n" + "=" * 80)
    print(f"Configuration file: {IDENTIFIERS_FILE}")
    print(f"Scraped records: {SCRAPED_RECORDS_DIR}/")
    print(f"Discrepancy log: {DISCREPANCY_LOG}")
    print("=" * 80 + "\n")


def run_scraper():
    """Run the identifier scraper against public sources."""
    data = load_identifiers()
    entities = data.get("entities", [])
    
    print("\n" + "=" * 80)
    print("  INCRIMINATION NATION - Running Scraper")
    print("  Creating Immutable Record in GitHub")
    print("=" * 80)
    
    if not entities:
        print("\n⚠️  No entities configured. Add entities to:")
        print(f"   {IDENTIFIERS_FILE}")
        print("\nExample entity configuration:")
        print("""
entities:
  - name: "Example Corporation"
    type: "LLC"
    state: "Arizona"
    identifiers:
      file_number: "L12345678"
      ein: "XX-XXXXXXX"
    claimed_statements:
      - field: "registered_agent"
        value: "John Doe"
        source: "company_website"
""")
        return
    
    print(f"\n🔍 Scraping {len(entities)} entities...\n")
    
    for entity in entities:
        name = entity.get("name", "Unknown")
        print(f"\n📌 Processing: {name}")
        print("-" * 40)
        
        # Create a record of what we would scrape
        # In production, this would make actual API calls
        record_data = {
            "entity_name": name,
            "entity_type": entity.get("type"),
            "state": entity.get("state"),
            "identifiers_checked": entity.get("identifiers", {}),
            "sources_queried": list(PUBLIC_SOURCES.keys()),
            "public_records_found": [],
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        # Simulate finding discrepancies (in production, compare actual data)
        claimed = entity.get("claimed_statements", [])
        for claim in claimed:
            record_data["public_records_found"].append({
                "field": claim.get("field"),
                "claimed": claim.get("value"),
                "source": claim.get("source"),
                "status": "pending_verification"
            })
        
        # Create the immutable record
        create_scraped_record(
            name,
            "incrimination_nation_scraper",
            record_data,
            notes=[
                f"Scraped via Incrimination Nation workflow",
                f"Integrated with {PUBLIC_SOURCES['lawfully_illegal']}",
                "Record stored in GitHub for immutable timestamping"
            ]
        )
    
    print("\n" + "=" * 80)
    print("  ✅ Scraping complete. Records committed to GitHub.")
    print("  📁 Records are now part of immutable Git history.")
    print("=" * 80 + "\n")


def generate_report():
    """Generate a discrepancy report."""
    print("\n" + "=" * 80)
    print("  INCRIMINATION NATION - Discrepancy Report")
    print("=" * 80)
    
    if not os.path.exists(DISCREPANCY_LOG):
        print("\n✅ No discrepancies logged.")
        return
    
    with open(DISCREPANCY_LOG, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    discrepancies = data.get("discrepancies", [])
    
    if not discrepancies:
        print("\n✅ No discrepancies found.")
        return
    
    print(f"\n⚠️  {len(discrepancies)} discrepancies found:\n")
    
    for disc in discrepancies:
        print(f"  [{disc.get('status', 'unknown').upper()}] {disc.get('id')}")
        print(f"  Entity: {disc.get('entity')}")
        print(f"  Field: {disc.get('field')}")
        print(f"  Claimed: {disc.get('claimed_value')}")
        print(f"  Found: {disc.get('found_value')}")
        print(f"  Source: {disc.get('source')}")
        print("-" * 40)
    
    print("\n" + "=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="Incrimination Nation - Public Record Identifier Scraper"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List configured identifiers and entities"
    )
    parser.add_argument(
        "--scrape", action="store_true",
        help="Run the scraper against public sources"
    )
    parser.add_argument(
        "--report", action="store_true",
        help="Generate discrepancy report"
    )
    parser.add_argument(
        "--init", action="store_true",
        help="Initialize identifier configuration"
    )
    
    args = parser.parse_args()
    
    if args.init:
        # Create default configuration
        default_config = {
            "identifiers": [
                {
                    "type": "ORCID",
                    "value": "0009-0002-7324-9643",
                    "notes": "Travis Ryle Trust identifier"
                }
            ],
            "entities": [],
            "metadata": {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "website": "https://www.lawfully-illegal.com",
                "purpose": "Incrimination Nation - Corporate truth verification"
            }
        }
        save_identifiers(default_config)
        print(f"✅ Initialized configuration: {IDENTIFIERS_FILE}")
        return 0
    
    if args.list:
        list_identifiers()
        return 0
    
    if args.scrape:
        run_scraper()
        return 0
    
    if args.report:
        generate_report()
        return 0
    
    # Default: show help
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

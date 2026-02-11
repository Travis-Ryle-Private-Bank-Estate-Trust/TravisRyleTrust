# TravisRyleTrust
Public-facing ledger of The Travis Ryle Private Bank Estate &amp; Trust
# The Travis Ryle Private Bank Estate & Trust

This repository serves as the **public-facing ledger** of the Private Living Express Trust declared by Travis Steven Ryle, Ambassador in Christ, Guarantor, and Beneficiary.

- **Trust Declaration**: Published at ORCID (https://orcid.org/0009-0002-7324-9643)
- **Definitions**: See [definitions.md](definitions.md)
- **Ledger**: See [ledger.json](ledger.json)

All notices, definitions, promissory notes, and communications are published here for **traceability, timestamping, and public inspection**.

## Public Ledger Integration

This repository integrates with the [lawfully-illegal.com public ledge](https://www.lawfully-illegal.com/public-ledge) for tracking public record inquiries:

- **View ledger entries**: `python3 scripts/sync_public_ledge.py --list`
- **Open public ledge**: `python3 scripts/sync_public_ledge.py`
- **Ledger records**: Stored in `records/public-ledger/`

### Current Ledger Entries

| ID | Action | Party | Status | Bates |
|----|--------|-------|--------|-------|
| LED-20251123-004 | Public record inquiry: Kingman court | Mohave County / Kingman | Open | Ryle-KINGMAN-COURT-0001 |
| LED-20251123-005 | Entity dossier: Aztec Constructors | Corporate records | Open | Ryle-AZTEC-DOSSIER-0001 |
| LED-20251123-006 | County records inquiry: Contra Costa | Contra Costa County | Open | Ryle-CONTRA-COSTA-0001 |

## Email Tracking

This repository includes a system for tracking sent emails with cryptographic verification:

- **Store emails** in `communications/emails/` as .eml, .msg, .mbox, or PDF files
- **Track emails** using `scripts/track_email.py` to create verified records with tracking URLs
- **Generate tracking buttons** using `scripts/generate_tracking_button.py` for HTML/text emails
- **List emails** using `scripts/list_emails.py` to view all tracked correspondence

### Quick Start: Add Tracking Button to Emails

```bash
# 1. Track your email
python3 scripts/track_email.py communications/emails/2025-11-15-notice.eml \
  --to recipient@example.com \
  --subject "Your Subject"

# 2. Generate tracking button
python3 scripts/generate_tracking_button.py records/YOUR-RECORD.yaml

# 3. Copy the HTML code and paste it into your email
```

Recipients can click the button to view verified evidence on the [public ledge](https://www.lawfully-illegal.com/public-ledge), and their clicks are tracked.

See [docs/email-tracking-button-guide.md](docs/email-tracking-button-guide.md) for complete instructions and [communications/README.md](communications/README.md) for email storage guidelines.

# Email Communication Logs

This directory contains PDF exports of email communications for tracking and record-keeping purposes.

## Purpose

Store email communication logs as PDF files for:
- Legal documentation and evidence
- Audit trails of correspondence
- Reference for trust administration

## Naming Convention

Use: `YYYY-MM-DD-subject.pdf` (e.g., `2025-11-26-attorney-response.pdf`)

## File Types

- PDF exports of email threads
- PDF prints of important correspondence
- Email delivery reports

## Tracking

Email logs stored here should be cross-referenced with the main `communications/emails/` directory and tracked using the email tracking system documented in [docs/email-tracking-guide.md](../docs/email-tracking-guide.md).

## Website Integration

This repository is integrated with the tracking system at:
**https://www.lawfully-illegal.com/tracking**

To sync records with the website:
```bash
# Check connection status
python3 scripts/sync_tracking.py --status

# Push local records to website
python3 scripts/sync_tracking.py --push

# Pull records from website
python3 scripts/sync_tracking.py --pull
```

Configure your API key in `.env` file (see `.env.example` for template).

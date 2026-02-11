# Email Tracking Button - Quick Reference

## Quick Start (3 Steps)

### Step 1: Track Your Email
```bash
python3 scripts/track_email.py communications/emails/YYYY-MM-DD-subject.eml \
  --to recipient@example.com \
  --subject "Your Email Subject" \
  --date YYYY-MM-DD
```

### Step 2: Generate Tracking Button
```bash
python3 scripts/generate_tracking_button.py records/YOUR-RECORD.yaml
```

### Step 3: Use the Output
- Copy the **HTML code** for HTML emails
- Copy the **plain text link** for text-only emails
- Files saved to `/tmp/tracking-buttons/` for reference

## What Recipients See

When they click the button, they're taken to:
```
https://www.lawfully-illegal.com/public-ledge?record_id=<ID>&type=email&subject=<SUBJECT>&date=<DATE>
```

They can view:
- ✅ Email subject and date
- ✅ SHA-256 checksum
- ✅ Timestamp
- ✅ Record type and status
- ✅ Link to GitHub for full verification

## Files Created

| File | Purpose |
|------|---------|
| `records/YYYY-MM-DD-email-*.yaml` | Email record with metadata |
| `/tmp/tracking-buttons/*-button.html` | HTML button code |
| `/tmp/tracking-buttons/*-link.txt` | Plain text link |

## Templates Available

| Template | Location | Use For |
|----------|----------|---------|
| HTML Email | `templates/email-with-tracking-button.html` | Rich HTML emails |
| Plain Text | `templates/email-with-tracking-link.txt` | Text-only emails |

## Lookup by Record ID

If you only know the record ID:
```bash
python3 scripts/generate_tracking_button.py --record-id <RECORD-ID>
```

## Full Documentation

See: [docs/email-tracking-button-guide.md](../docs/email-tracking-button-guide.md)

## Demo

See: [docs/tracking-button-demo.html](../docs/tracking-button-demo.html)

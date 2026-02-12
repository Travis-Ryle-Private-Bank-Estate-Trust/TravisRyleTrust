# Email Tracking Button Guide

This guide explains how to add tracking buttons to your emails so recipients can view evidence on the public ledger.

## Overview

When you send important correspondence, you can include a tracking button that:
1. **Links to the public ledger** - Provides transparent, verifiable proof of the correspondence
2. **Tracks recipient clicks** - Shows when recipients view the evidence (via public ledger analytics)
3. **Displays evidence clearly** - Recipients can see checksums, timestamps, and full metadata

## Quick Start

### Step 1: Save Your Email

Save your email file in `communications/emails/` following the naming convention:

```bash
YYYY-MM-DD-description.eml
```

Example: `2025-11-15-legal-notice.eml`

### Step 2: Track the Email

Run the tracking script:

```bash
python3 scripts/track_email.py communications/emails/2025-11-15-legal-notice.eml \
  --to recipient@example.com \
  --subject "Legal Notice - Evidence Required" \
  --date 2025-11-15 \
  --notes "Formal notice sent regarding court case"
```

This will:
- Create a YAML record with metadata
- Generate a unique tracking URL
- Output the record file path and tracking URL

### Step 3: Generate Tracking Button

Generate the HTML button code:

```bash
python3 scripts/generate_tracking_button.py records/2025-11-15-email-recipient-legal-notice.yaml
```

This outputs:
- **HTML code** - Copy and paste into HTML emails
- **Plain text link** - For text-only emails
- **Saved files** - In `/tmp/tracking-buttons/` for easy access

### Step 4: Add Button to Your Email

#### For HTML Emails:

1. Copy the HTML code from the script output
2. Paste it at the bottom of your email (before your signature)
3. The button will appear styled and clickable

#### For Plain Text Emails:

1. Copy the plain text version
2. Paste it at the bottom of your email
3. Recipients can click the URL in most email clients

## Templates

### Using Email Templates

Pre-made templates are available in `templates/`:

**HTML Template:**
```bash
templates/email-with-tracking-button.html
```

**Plain Text Template:**
```bash
templates/email-with-tracking-link.txt
```

To use a template:
1. Copy the template file
2. Replace placeholder text with your content
3. Replace `RECORD_ID_HERE` with your actual record ID
4. Replace `SHA256_HASH_HERE` with the checksum from your record

## Advanced Usage

### Find Record by ID

If you know the record ID but not the file path:

```bash
python3 scripts/generate_tracking_button.py --record-id fc066e76-dc52-4dfc-8be9-eecf997dc6eb
```

### Customize Button Text

Edit the `generate_tracking_button.py` script and modify the `button_text` parameter in the function call.

### Multiple Recipients

For multiple recipients (CC):

```bash
python3 scripts/track_email.py communications/emails/2025-11-15-notice.eml \
  --to primary@example.com \
  --cc secondary@example.com \
  --cc tertiary@example.com \
  --subject "Group Notice"
```

## What Recipients See

When recipients click the tracking button:

1. **Public Ledge Website** - Opens https://www.lawfully-illegal.com/public-ledge
2. **Record Details** - Shows the record ID, date, subject, and type
3. **Verification Info** - Displays checksums and timestamps for verification
4. **Evidence Trail** - Provides transparent proof of the correspondence

## Tracking URL Format

The tracking URL includes these parameters:
- `record_id` - Unique identifier for the email record
- `type` - Record type (always "email")
- `subject` - Email subject line
- `date` - Date the email was sent

Example:
```
https://www.lawfully-illegal.com/public-ledge?record_id=fc066e76-dc52-4dfc-8be9-eecf997dc6eb&type=email&subject=Legal+Notice&date=2025-11-15
```

## Security Features

### Cryptographic Verification

Each tracked email includes:
- **SHA-256 checksum** - Verifies file integrity
- **Timestamp** - ISO 8601 format with timezone
- **File size** - In bytes
- **UUID** - Universally unique identifier

### Public Transparency

All records are:
- **Published on GitHub** - Transparent and timestamped via Git
- **Linked on public ledger** - Accessible at lawfully-illegal.com
- **Immutable** - Git history preserves all changes

## Best Practices

1. **Track Important Emails** - Use for legal notices, formal correspondence, and evidence
2. **Add Button Before Sending** - Include tracking button in original email
3. **Verify Links** - Test tracking URLs before sending
4. **Keep Records** - Don't delete YAML records or email files
5. **Update Notes** - Add detailed notes to records for context

## Troubleshooting

### Button Not Appearing

- Check HTML rendering in your email client
- Some clients strip styles - use plain text version
- Test in webmail (Gmail, Outlook.com) for best compatibility

### Tracking URL Not Working

- Verify record ID matches the YAML file
- Check that record file exists in `records/`
- Ensure public ledge website is accessible

### Script Errors

- Check Python 3 is installed: `python3 --version`
- Verify PyYAML is available: `python3 -c "import yaml"`
- Check file paths are correct (absolute or relative to repo root)

## Example Workflow

Complete example from start to finish:

```bash
# 1. Create email file
cat > communications/emails/2025-11-15-court-notice.eml << 'EOF'
From: travis@trust.com
To: court@example.com
Subject: Evidence Submission - Case #12345
Date: Fri, 15 Nov 2025 10:00:00 +0000

Dear Court Clerk,

Please find attached evidence for Case #12345.

Best regards,
Travis Steven Ryle
EOF

# 2. Track the email
python3 scripts/track_email.py communications/emails/2025-11-15-court-notice.eml \
  --to court@example.com \
  --subject "Evidence Submission - Case #12345" \
  --date 2025-11-15 \
  --notes "Formal evidence submission"

# Output shows: records/2025-11-15-email-court-evidence-submission.yaml
# Output shows: Tracking URL: https://www.lawfully-illegal.com/public-ledge?...

# 3. Generate button
python3 scripts/generate_tracking_button.py records/2025-11-15-email-court-evidence-submission.yaml

# 4. Copy HTML code from output and paste into email

# 5. Send email with tracking button included
```

## Integration with Public Ledge

The public ledge at https://www.lawfully-illegal.com/public-ledge provides:

- **Public inquiry tracking** - Court records, entity dossiers
- **Ledger entries** - Timestamped actions and parties
- **Evidence verification** - Checksum validation
- **Click tracking** - Analytics on who views evidence (server-side)

All tracked emails integrate seamlessly with this system.

## Support

For questions or issues:
- Review this guide
- Check existing records in `records/` for examples
- Review templates in `templates/`
- Open an issue on GitHub if needed

---

**The Travis Ryle Private Bank Estate & Trust**  
Public Ledger: https://www.lawfully-illegal.com/public-ledge  
Repository: https://github.com/Travis-Ryle-Private-Bank-Estate-Trust/TravisRyleTrust

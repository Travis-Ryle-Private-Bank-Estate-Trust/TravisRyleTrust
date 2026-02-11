# Templates Directory

Reusable templates for letters, email drafts, tracking buttons, and checklists.

## Email Templates

### Email with Tracking Button (HTML)
**File:** `email-with-tracking-button.html`

HTML email template with embedded tracking button that links to the public ledger.

**Usage:**
1. Copy the template
2. Replace `[Your email message content here]` with your message
3. Replace `RECORD_ID_HERE` with your actual record ID
4. Replace `SHA256_HASH_HERE` with the checksum from your record
5. Send as HTML email

**Features:**
- Styled tracking button
- Professional footer with trust information
- Public ledger links
- Cryptographic verification notice

### Email with Tracking Link (Plain Text)
**File:** `email-with-tracking-link.txt`

Plain text email template with tracking link for text-only email clients.

**Usage:**
1. Copy the template
2. Replace `[Your email message content here]` with your message
3. Replace `RECORD_ID_HERE` with your actual record ID
4. Replace `SHA256_HASH_HERE` with the checksum from your record
5. Send as plain text email

**Features:**
- ASCII art formatting
- Clear tracking link
- Professional signature
- Works in all email clients

## Generating Custom Tracking Buttons

Instead of manually editing templates, use the automated script:

```bash
# Track an email first
python3 scripts/track_email.py communications/emails/YOUR-EMAIL.eml \
  --to recipient@example.com \
  --subject "Your Subject"

# Generate tracking button automatically
python3 scripts/generate_tracking_button.py records/YOUR-RECORD.yaml
```

This generates:
- HTML button code (ready to paste)
- Plain text link (ready to paste)
- Pre-filled templates with your record details

## Documentation

See [docs/email-tracking-button-guide.md](../docs/email-tracking-button-guide.md) for complete instructions on using email tracking buttons.


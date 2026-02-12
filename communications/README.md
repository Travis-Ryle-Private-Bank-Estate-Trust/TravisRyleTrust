# Communications Directory

Store all correspondence and communications here with proper tracking.

## Subdirectories

- **emails/**: Save exported .eml/.msg/.mbox or PDF prints of email threads
- **letters/**: PDFs or images of physical letters
- **notes/**: Call notes, meeting summaries (Markdown or text)

## Naming Convention

Use: `YYYY-MM-DD-topic.ext` (e.g., `2025-11-07-attorney-response.pdf`)

## Email Tracking

To track a sent email:

1. Save the email file in `communications/emails/` following the naming convention
2. Run the tracking script:
   ```bash
   python3 scripts/track_email.py communications/emails/YYYY-MM-DD-subject.eml \
     --to recipient@example.com \
     --subject "Email Subject" \
     --date YYYY-MM-DD \
     --notes "Optional note about the email"
   ```

This will create a YAML record in `records/` with metadata including:
- Recipient(s)
- Subject
- Send date
- File checksum (SHA-256)
- File size
- **Tracking URL** for public ledge

### Adding Tracking Buttons to Emails

After tracking an email, generate a tracking button:

```bash
python3 scripts/generate_tracking_button.py records/YOUR-RECORD.yaml
```

This outputs:
- **HTML button code** - Paste into HTML emails
- **Plain text link** - Paste into text emails
- **Pre-filled templates** - Saved to `/tmp/tracking-buttons/`

When recipients click the button, they can:
- View verified evidence on the public ledger
- See cryptographic checksums and timestamps
- Their click is tracked via web analytics

For detailed usage examples and best practices, see [docs/email-tracking-button-guide.md](../docs/email-tracking-button-guide.md).

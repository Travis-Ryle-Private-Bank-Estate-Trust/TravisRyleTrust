# Email Tracking Usage Examples

This document provides practical examples of how to use the email tracking system.

## Basic Email Tracking

### 1. Save Your Email
First, save your sent email in the `communications/emails/` directory:
- For Gmail/Outlook: Export as .eml or save as PDF
- For Thunderbird: Copy .eml file
- For Apple Mail: Save as .eml

Use the naming convention: `YYYY-MM-DD-brief-description.ext`

Example: `communications/emails/2025-11-07-attorney-response.eml`

### 2. Track the Email
Run the tracking script with required information:

```bash
python3 scripts/track_email.py communications/emails/2025-11-07-attorney-response.eml \
  --to attorney@lawfirm.com \
  --subject "Response to Trust Inquiry" \
  --date 2025-11-07
```

### 3. View Tracked Emails
List all tracked emails:

```bash
# Table format (default)
python3 scripts/list_emails.py

# JSON format
python3 scripts/list_emails.py --format json
```

## Advanced Examples

### Email with CC Recipients
```bash
python3 scripts/track_email.py communications/emails/2025-11-07-notice-to-trustees.eml \
  --to trustee1@example.com \
  --cc trustee2@example.com \
  --cc trustee3@example.com \
  --subject "Annual Trust Notice" \
  --date 2025-11-07 \
  --notes "Sent annual notice as required by trust declaration"
```

### Email with Multiple Notes
```bash
python3 scripts/track_email.py communications/emails/2025-11-07-legal-demand.eml \
  --to debtor@example.com \
  --subject "Demand for Payment" \
  --date 2025-11-07 \
  --notes "First demand letter sent via certified mail" \
  --notes "Tracking number: 1234567890"
```

## Verification

### Check Email Record
After tracking an email, verify it was recorded correctly:

```bash
# The script outputs the record filename
# View the record:
cat records/2025-11-07-email-attorney-response-to-trust-inquiry.yaml
```

### Validate All Records
Run the validation script to ensure all records are valid:

```bash
bash scripts/validate.sh
```

### Update Checksums
If you modify an email file, update its checksum:

```bash
python3 scripts/update_attachments.py
```

## Integration with Ledger

Email tracking is integrated with the trust ledger system. All tracked emails:
- Are recorded in YAML format in `records/`
- Have SHA-256 checksums for verification
- Are timestamped via Git commits
- Can be validated against their original files

## Best Practices

1. **Track emails promptly** after sending to ensure accurate timestamps
2. **Use descriptive subject lines** to make emails easy to find later
3. **Include relevant notes** about the context or purpose of the email
4. **Validate regularly** to ensure all records are accurate
5. **Backup email files** along with the repository to preserve evidence

## Troubleshooting

### "Email file must be in communications/emails/ directory"
Make sure your email file is saved in the correct directory:
```bash
# Correct
communications/emails/2025-11-07-example.eml

# Incorrect
emails/2025-11-07-example.eml
```

### "Error: --to requires a value"
Ensure you provide all required arguments:
```bash
# Incorrect
python3 scripts/track_email.py file.eml --to

# Correct
python3 scripts/track_email.py file.eml --to recipient@example.com --subject "Subject"
```

## Legal Considerations

Tracked emails serve as:
- **Evidence** of communication in legal proceedings
- **Proof of notice** for trust matters
- **Timestamped records** via Git commit history
- **Cryptographically verified** documents via SHA-256 checksums

Always retain original email files and do not modify them after tracking to preserve their evidentiary value.

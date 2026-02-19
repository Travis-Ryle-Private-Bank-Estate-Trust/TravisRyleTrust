---
layout: default
title: Tracked Identifiers
permalink: /identifiers/
---

# 🔑 Tracked Identifiers

Incrimination Nation - Public Record Tracking

## ⚖️ About Incrimination Nation

This system tracks identifiers across public record sources to verify corporate statements. All scraped data is stored in GitHub as an **immutable, tamper-evident record**.

**Purpose:** Force truth through public record verification. Corporations cannot hide — Git history preserves everything.

## 👤 Personal Identifiers

| Type | Value | Source | Notes |
|---|---|---|---|
| ORCID | `0009-0002-7324-9643` | [orcid.org](https://orcid.org/0009-0002-7324-9643) | Travis Ryle Trust identifier |
| Trust Name | The Travis Ryle Private Bank Estate & Trust | Declaration | Official trust name |
| LexID | `4022387079` | LexisNexis | Person identifier for public record tracking |
| Consumer # | `11133734` | LexisNexis | Updated consumer file number |
| SSA BNC | `26J6558J21517` | SSA | Social Security Administration identifier |
| SSA Case # | `31568224` | SSA | Active case number tracking |
| IRS 1098-1 | `109804891192` | IRS | Mortgage Interest Statement identifier |
| IRS 1098-2 | `109804896318` | IRS | Mortgage Interest Statement identifier |

## 📡 Public Record Sources

| Source | Type | URL | Description |
|---|---|---|---|
| LexisNexis | Aggregator | [lexisnexis.com](https://www.lexisnexis.com/) | Public records aggregator - tracks LexID and consumer identifiers |
| SSA | Federal | [ssa.gov](https://www.ssa.gov/) | Social Security Administration records |
| IRS | Federal | [irs.gov](https://www.irs.gov/) | Internal Revenue Service filings |
| SEC EDGAR | Federal | [sec.gov](https://www.sec.gov/cgi-bin/browse-edgar) | Securities and Exchange Commission filings |
| PACER | Federal | [pacer.uscourts.gov](https://pacer.uscourts.gov/) | Federal court records |
| Arizona Corp Commission | State | [ecorp.azcc.gov](https://ecorp.azcc.gov/) | Arizona corporate records |
| California SOS | State | [bizfileonline.sos.ca.gov](https://bizfileonline.sos.ca.gov/) | California business filings |
| Lawfully Illegal | Integration | [lawfully-illegal.com](https://www.lawfully-illegal.com/public-ledge) | Primary website integration |

## 🤖 Automated Scraping

The **Incrimination Nation** workflow runs daily to:
- Query public record sources for tracked identifiers
- Compare corporate statements against official records
- Log discrepancies when claimed values don't match public records
- Commit all findings to immutable Git history

[▶️ View Workflow Runs](https://github.com/Travis-Ryle-Private-Bank-Estate-Trust/TravisRyleTrust/actions/workflows/incrimination-nation.yml)

## ➕ Add More Identifiers

To add new identifiers for tracking, edit:
`records/identifiers/identifiers.yaml`

[📄 View/Edit Identifiers Config](https://github.com/Travis-Ryle-Private-Bank-Estate-Trust/TravisRyleTrust/blob/main/records/identifiers/identifiers.yaml)

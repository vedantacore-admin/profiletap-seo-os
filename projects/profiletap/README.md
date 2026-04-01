# ProfileTap SEO OS

Structured SEO operating system for ProfileTap, a smart identity management platform for digital profiles, NFC cards, QR sharing, reputation support, and multi-use identity pages.

This project follows the central SEO OS pipeline:

`keyword → page → content → backlink`

## Quick Start

Open Claude Code from **this directory** (`projects/profiletap/`) — both the root CLAUDE.md (generic skills) and this project's CLAUDE.md (ProfileTap rules, schemas, workflows) will auto-load.

## Operating Rules

- One keyword intent maps to one page only — no cannibalization
- No content is created without a mapped target page
- India-first transactional opportunities are prioritized before broader global expansion
- Comparisons, use cases, and blogs support commercial landing pages — never compete with them
- Features are embedded into hub and child pages, not standalone pages, unless keyword data proves distinct intent
- Product family pages own buying intent; solution pages own use-case intent

## Objective

Build ProfileTap into:

- the leading smart identity platform in India
- a strong SEO authority across business and multi-use identity workflows
- a conversion-focused landing page system with sustainable backlink growth

## Key Files

| File | Purpose |
|------|---------|
| `data/keywords/raw_keyword_bank.csv` | Full keyword research inventory (232 rows) |
| `data/keywords/execution_seo_master.csv` | Canonical page-to-keyword families (one row per page) |
| `data/pages/page_master.csv` | Master page inventory with architecture |
| `data/content/content_calendar.csv` | Content production queue |
| `data/backlinks/backlink_targets.csv` | Link prospect list |
| `data/products/product_catalog.json` | Product catalog with variants and hub mapping |

## System Check

```bash
python scripts/validate_system.py
```

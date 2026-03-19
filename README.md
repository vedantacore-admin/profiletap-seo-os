# ProfileTap SEO OS

Structured SEO operating system for ProfileTap, a smart identity platform for digital profiles, NFC cards, QR sharing, and multi-use identity pages.

This repository is designed to run SEO work as a controlled system:

`keyword -> page -> content -> backlink`

The operating rules are:

- one keyword intent maps to one page only
- no content is created without a mapped target page
- India-first transactional opportunities are prioritized before broader global expansion
- comparisons, use cases, and blogs support commercial landing pages instead of competing with them

## Objective

Build ProfileTap into:

- the leading smart identity platform in India
- a strong SEO authority in digital business cards and identity pages
- a conversion-focused landing page system with sustainable backlink growth

## Repository Structure

### Core data files

- [data/keywords/master_keywords.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/keywords/master_keywords.csv)
  Source of truth for all tracked keywords.
- [data/pages/page_master.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/pages/page_master.csv)
  Master list of pages that exist or should be created.
- [data/pages/page_keyword_map.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/pages/page_keyword_map.csv)
  One-to-one mapping between keywords and pages.
- [data/content/content_calendar.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/content/content_calendar.csv)
  Content production queue.
- [data/backlinks/backlink_targets.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/backlinks/backlink_targets.csv)
  Backlink prospect list tied to target pages.
- [data/backlinks/outreach_tracker.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/backlinks/outreach_tracker.csv)
  Outreach execution tracker.

### Supporting docs

- [docs/02-seo-strategy.md](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/docs/02-seo-strategy.md)
  High-level SEO strategy notes.
- [sop/page-mapping-process.md](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/sop/page-mapping-process.md)
  Page mapping rule: one keyword intent to one page.
- [briefs/templates/page-brief-template.md](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/briefs/templates/page-brief-template.md)
  Template for page and content briefs.
- [prompts/content-brief-prompt.md](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/prompts/content-brief-prompt.md)
  Prompt scaffold for generating briefs from mapped keywords.

## CSV Schemas

### `master_keywords.csv`

| Column | Meaning |
| --- | --- |
| `keyword` | Exact target keyword |
| `cluster` | Intent cluster or topic group |
| `pillar` | Broad strategic theme for annual planning |
| `intent` | `transactional`, `comparison`, `commercial`, or `informational` |
| `funnel_stage` | `TOFU`, `MOFU`, or `BOFU` |
| `target_market` | `IN`, `GLOBAL`, or `IN+GLOBAL` |
| `target_language` | Primary language for the target page |
| `volume` | Search volume when available |
| `kd` | Keyword difficulty when available |
| `cpc` | Paid CPC reference from Semrush when available |
| `business_score` | Manual value score for commercial importance |
| `priority` | `P1`, `P2`, `P3` |
| `status` | Current workflow state |
| `target_page_type` | Intended page type |
| `semrush_last_checked` | Date of last metric refresh |
| `notes` | Normalization or research notes |

### `page_master.csv`

| Column | Meaning |
| --- | --- |
| `page_slug` | Canonical URL path |
| `page_type` | `homepage`, `category`, `use_case`, `comparison`, `blog` |
| `page_title` | Working SEO title |
| `primary_keyword` | Main keyword for the page |
| `target_market` | Primary market this page serves |
| `target_language` | Page language |
| `funnel_stage` | Primary funnel role |
| `conversion_goal` | Main business outcome from the page |
| `primary_cta` | CTA the page should drive |
| `owner` | Responsible person |
| `status` | `planned`, `in_progress`, `published`, or `refresh_needed` |
| `target_publish_quarter` | Quarter target for the annual plan |
| `publish_date` | Actual publish date |
| `last_updated` | Last significant update date |
| `next_refresh` | Planned refresh date |
| `notes` | Internal page notes |

### `page_keyword_map.csv`

| Column | Meaning |
| --- | --- |
| `keyword` | Keyword being assigned |
| `page_slug` | Target page |
| `is_primary` | `yes` or `no` |
| `mapping_role` | `primary` or `secondary` |
| `mapping_notes` | Why the keyword belongs to this page |

### `content_calendar.csv`

| Column | Meaning |
| --- | --- |
| `content_id` | Internal content task ID |
| `page_slug` | Canonical page the content supports |
| `title` | Working content title |
| `content_type` | Page/content format |
| `target_keyword` | Mapped keyword to support |
| `target_market` | Primary target market |
| `target_language` | Content language |
| `funnel_stage` | Funnel role |
| `priority` | Publishing priority |
| `owner` | Responsible person |
| `status` | Overall execution status |
| `brief_status` | Brief readiness status |
| `due_date` | Working due date |
| `publish_date` | Actual publish date |
| `refresh_date` | Planned refresh date |
| `target_quarter` | Quarter target in the annual plan |
| `notes` | Internal production notes |

### `backlink_targets.csv`

| Column | Meaning |
| --- | --- |
| `domain` | Target publication or website |
| `site_type` | Publication category |
| `target_page_slug` | Page the link should support |
| `target_keyword` | Primary keyword the link should strengthen |
| `suggested_anchor` | Recommended anchor text |
| `anchor_type` | `brand`, `partial`, `exact`, or other anchor class |
| `target_market` | Market relevance of the link target |
| `link_angle` | Outreach angle or editorial hook |
| `priority` | Outreach priority |
| `owner` | Responsible person |
| `status` | Prospect status |
| `notes` | Qualification notes |

### `outreach_tracker.csv`

| Column | Meaning |
| --- | --- |
| `domain` | Outreach target |
| `target_page_slug` | Page being supported by the pitch |
| `contact_name` | Main contact when known |
| `contact_email` | Primary email when known |
| `status` | Outreach status |
| `first_contact_date` | First outreach date |
| `last_contact_date` | Latest touchpoint date |
| `next_follow_up_date` | Next scheduled follow-up |
| `outcome` | Result summary |
| `live_url` | Published link URL when won |
| `notes` | Internal notes |

## Semrush Update Workflow

When reviewing keywords in Semrush, update these fields in [master_keywords.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/keywords/master_keywords.csv):

- `volume`
- `kd`
- `cpc`
- `semrush_last_checked`
- `priority` if the market data changes the order
- `notes` for useful SERP observations

Do not change:

- `cluster`
- `pillar`
- `intent`
- `target_page_type`

unless the underlying keyword intent has actually changed.

## Annual Management Layer

The management layer is now built around:

- keyword scoring in `master_keywords.csv`
- quarterly publishing targets in `page_master.csv`
- execution status in `content_calendar.csv`
- prospect qualification in `backlink_targets.csv`
- follow-up control in `outreach_tracker.csv`

## Current Baseline

The repository is initialized with a starting India-first SEO system:

- 22 mapped keywords
- 17 planned pages
- 17 content items in the calendar
- 12 backlink prospects

Priority emphasis:

- `P1` India transactional category pages
- `P1` India comparison pages against direct competitors
- `P1` high-conversion use cases for doctors, real estate, and freelancers
- supporting blogs for authority and internal linking

Current `P1` keyword groups:

- `digital business card india`
- `digital visiting card india`
- `nfc business card india`
- `qr business card`
- `digital business card for doctors`
- `digital business card for real estate agents`
- `digital business card for freelancers`
- `hihello alternative india`
- `popl alternative india`
- `taponn alternative`

## Default Workflow

1. Update `master_keywords.csv` with cleaned keywords and intent clusters.
2. Check `page_keyword_map.csv` before creating any new page.
3. Add or update the canonical page in `page_master.csv`.
4. Add the corresponding content task in `content_calendar.csv`.
5. Add backlink prospects in `backlink_targets.csv`.
6. Track contact progress in `outreach_tracker.csv`.

## Guardrails

- Never create duplicate pages for the same keyword intent.
- Never assign one keyword to multiple pages.
- Never add content ideas without a mapped keyword.
- Prioritize India transactional demand before low-intent traffic.
- Use comparison and blog pages to strengthen commercial pages, not cannibalize them.

## Next Operations

- populate `volume` and `kd` fields with validated keyword data
- expand India category and use-case coverage
- create briefs for all `P1` pages first
- qualify backlink targets with named contacts and outreach angles

## Document Index

- `README.md`
  Operating summary and file contracts.
- `docs/02-seo-strategy.md`
  Market strategy, keyword buckets, and current execution priorities.
- `sop/page-mapping-process.md`
  Mapping logic and anti-cannibalization rules.
- `briefs/templates/page-brief-template.md`
  Standard brief template for pages and content.
- `prompts/content-brief-prompt.md`
  Prompt for generating briefs from the structured datasets.

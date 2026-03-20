# ProfileTap SEO OS

Structured SEO operating system for ProfileTap, a smart identity management platform for digital profiles, NFC cards, QR sharing, reputation support, and multi-use identity pages.

This repository is designed to run SEO work as a controlled system:

`keyword -> page -> content -> backlink`

The operating rules are:

- one keyword intent maps to one page only
- no content is created without a mapped target page
- India-first transactional opportunities are prioritized before broader global expansion
- comparisons, use cases, and blogs support commercial landing pages instead of competing with them
- features are embedded into homepage, hub pages, and child pages instead of becoming standalone SEO pages by default

## Objective

Build ProfileTap into:

- the leading smart identity platform in India
- a strong SEO authority across business and multi-use identity workflows
- a conversion-focused landing page system with sustainable backlink growth

## Repository Structure

### Core data files

- [data/keywords/master_keywords.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/keywords/master_keywords.csv)
  Source of truth for all tracked keywords.
- [data/pages/page_master.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/pages/page_master.csv)
  Master list of planned and mapped pages.
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
  Prompt scaffold for generating briefs from mapped keywords and architecture rows.

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
| `page_type` | `homepage`, `solution_hub`, `category`, `use_case`, `comparison`, or `blog` |
| `page_group` | Planning bucket for architecture and rollup |
| `parent_page_slug` | Logical parent page in the launch hierarchy |
| `hub` | Main solution hub this page belongs to |
| `page_title` | Working SEO title |
| `primary_keyword` | Main keyword for the page; may be blank for architecture rows pending keyword import |
| `primary_intent` | Short description of the page's owned intent |
| `target_market` | Primary market this page serves |
| `target_language` | Page language |
| `funnel_stage` | Primary funnel role |
| `conversion_goal` | Main business outcome from the page |
| `feature_set` | Embedded feature modules relevant to this page |
| `pricing_visibility` | How pricing-sensitive features should be surfaced |
| `primary_cta` | CTA the page should drive |
| `owner` | Responsible person |
| `status` | `planned`, `in_progress`, `published`, or `refresh_needed` |
| `lifecycle_stage` | `launch_core`, `launch_secondary`, or `later_support` |
| `publish_wave` | `launch`, `post_launch_q1`, `post_launch_q2`, or `later` |
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
| `page_group` | Architecture bucket copied from the page inventory |
| `hub` | Main hub the content belongs to |
| `title` | Working content title |
| `content_type` | Page/content format |
| `target_keyword` | Mapped keyword to support; may be blank for architecture rows pending keyword import |
| `target_market` | Primary target market |
| `target_language` | Content language |
| `funnel_stage` | Funnel role |
| `priority` | Publishing priority |
| `feature_set` | Relevant embedded features for the brief and page sections |
| `pricing_visibility` | How to qualify plan-gated features in the content |
| `owner` | Responsible person |
| `status` | Overall execution status |
| `brief_status` | Brief readiness status |
| `due_date` | Working due date |
| `publish_date` | Actual publish date |
| `refresh_date` | Planned refresh date |
| `publish_wave` | Release wave for launch planning |
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

## Launch Architecture

The fixed launch pages are:

- `/`
- `/business-identity`
- `/creator-identity`
- `/family-safety-profile`
- `/pet-id-profile`
- `/travel-profile`
- `/vehicle-profile`

Launch rule:

- homepage lists the full feature inventory once
- hub and child pages only surface the relevant subset from `feature_set`
- no standalone feature pages are planned at this stage

## Canonical Feature Inventory

`feature_set` uses canonical internal tokens. These tokens are planning metadata, not final on-page copy.

| Token | Human meaning | Notes |
| --- | --- | --- |
| `digital_profiles` | Digital profiles | Broad profile creation and sharing foundation |
| `nfc_sharing` | NFC sharing | Tap-based profile sharing |
| `qr_sharing` | QR sharing | Scan-based profile access |
| `ai_review_assist` | AI review assist | Review support and related AI-assisted workflows |
| `analytics` | Analytics | General engagement and interaction analytics |
| `account_collaborators` | Manage account collaborators | Multiple collaborators helping manage one account |
| `multi_account_team_management` | Manage multiple accounts / teams | Team, business, or multi-account management |
| `multi_profile_type_profiles` | Multi-profile / multi-type profiles | Different profiles for different identity needs |
| `call_masking` | Call masking | Privacy layer for phone sharing |
| `whatsapp_masking` | WhatsApp masking | Privacy layer for WhatsApp sharing |
| `theme_library` | Wide range of themes | Theme and presentation customization |
| `advanced_creator_analytics` | Advanced analytics for creators | Creator-specific deeper analytics, likely plan-sensitive |

Rules for future use:

- use canonical tokens in CSVs
- use human-facing labels in briefs and page copy
- do not create new near-duplicate tokens for wording variations
- if a feature is plan-sensitive, capture that in `pricing_visibility`, not in a new feature token

## Feature Placement Model

Feature logic for planning:

- homepage shows the full inventory once
- hub pages show only the subset relevant to that hub
- child pages inherit only the features that help that page convert
- comparison pages should surface only the features relevant to the switch decision
- blog pages should mention features only where they support the informational intent

Current hub logic:

| Hub | Typical feature emphasis |
| --- | --- |
| `business` | digital profiles, NFC, QR, AI review assist, analytics, collaborators, teams, masking, themes |
| `creator` | digital profiles, NFC, QR, AI review assist, analytics, teams, multi-profile types, themes, creator analytics |
| `family_safety` | digital profiles, QR, multi-profile types, masking, themes |
| `pet` | digital profiles, QR, multi-profile types, themes |
| `travel` | digital profiles, QR, multi-profile types, masking, themes |
| `vehicle` | digital profiles, QR, multi-profile types, masking, themes |

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

## Current Baseline

The repository is initialized with a launch-first SEO system:

- 22 mapped sample keywords
- 23 planned pages
- 23 content items in the calendar
- 12 backlink prospects

Current mapped sample keyword groups:

- `smart identity platform`
- `digital business card india`
- `nfc business card india`
- `qr business card`
- `digital business card for doctors`
- `digital business card for creators`
- `hihello alternative india`
- `popl alternative india`
- `taponn alternative`
- `linktree alternative for creators`

## Default Workflow

1. Update `master_keywords.csv` with cleaned keywords and intent clusters.
2. Create or update architecture rows in `page_master.csv`, including `page_group`, `hub`, `feature_set`, and `publish_wave`.
3. Check `page_keyword_map.csv` before turning a planned row into a keyword-owned page.
4. Add or update the corresponding task in `content_calendar.csv`.
5. Only surface features inside the relevant hub or child page; do not create standalone feature pages without distinct keyword intent.
6. Add backlink prospects in `backlink_targets.csv`.
7. Track contact progress in `outreach_tracker.csv`.

## Guardrails

- Never create duplicate pages for the same keyword intent.
- Never assign one keyword to multiple pages.
- Never add content ideas without a mapped or planned target page.
- Prioritize India transactional demand before low-intent traffic.
- Use comparison and blog pages to strengthen commercial pages, not cannibalize them.
- Do not create standalone feature pages unless keyword research proves distinct feature-led intent.

## Document Index

- `README.md`
  Operating summary and file contracts.
- `docs/02-seo-strategy.md`
  Market strategy, launch architecture, and execution priorities.
- `sop/page-mapping-process.md`
  Mapping logic and anti-cannibalization rules.
- `briefs/templates/page-brief-template.md`
  Standard brief template for pages and content.
- `prompts/content-brief-prompt.md`
  Prompt for generating briefs from the structured datasets.

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
- physical product-family pages are documented separately from solution pages and are not added to the live page inventory until validated

## Objective

Build ProfileTap into:

- the leading smart identity platform in India
- a strong SEO authority across business and multi-use identity workflows
- a conversion-focused landing page system with sustainable backlink growth

## Repository Structure

### Core data files

- [data/keywords/raw_keyword_bank.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/keywords/raw_keyword_bank.csv)
  Retained research inventory. Keeps only approved `keep_primary` and `keep_secondary` keyword rows.
- [data/keywords/execution_seo_master.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/keywords/execution_seo_master.csv)
  Final canonical keyword system. One page-owned keyword family per row for execution and planning.
- [data/pages/page_master.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/pages/page_master.csv)
  Master list of planned and mapped pages.
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

### Rebuild tooling

- [scripts/rebuild_keyword_system.py](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/scripts/rebuild_keyword_system.py)
  Rebuilds `raw_keyword_bank.csv` and `execution_seo_master.csv` from the current source export in `Downloads`, including direct `.xlsx` imports.

## Keyword Workflow

ProfileTap now uses a two-sheet keyword model for large imports:

1. `raw_keyword_bank.csv`
   Keeps every discovered keyword from the source export.
2. `execution_seo_master.csv`
   Keeps only canonical, page-worthy keyword families.

Working rule:

- raw export feeds `raw_keyword_bank.csv`
- `raw_keyword_bank.csv` keeps only `keep_primary` and `keep_secondary` rows
- `execution_seo_master.csv` becomes the page-ready keyword system
- only validated execution rows should later flow into page mapping, briefs, and content production

## CSV Schemas

### `raw_keyword_bank.csv`

| Column | Meaning |
| --- | --- |
| `keyword` | Exact imported keyword from the source sheet |
| `source_category` | Imported bucket such as `Business`, `Use Case`, or `Competitor` |
| `observed_intent` | Source intent label normalized to lowercase |
| `market` | `IN` or `IN+GLOBAL` based on modifier signals |
| `modifier_type` | Primary modifier classification such as `city`, `best`, `comparison`, `profession`, or `feature` |
| `root_topic` | Internal canonical family label |
| `canonical_keyword` | Canonical keyword the row consolidates into |
| `canonical_page_slug` | Canonical page that should own the keyword family |
| `keep_status` | `keep_primary` or `keep_secondary` |
| `merge_reason` | Why the row belongs to that canonical family |
| `notes` | Free notes for research observations |
| `ubersuggest_volume` | Search volume to be filled later |
| `ubersuggest_kd` | Keyword difficulty to be filled later |
| `ubersuggest_cpc` | CPC to be filled later |
| `ubersuggest_last_checked` | Last Ubersuggest refresh date |

### `execution_seo_master.csv`

| Column | Meaning |
| --- | --- |
| `page_slug` | Canonical page that owns the keyword family |
| `page_type` | `homepage`, `solution_hub`, `category`, `use_case`, `comparison`, or `blog` |
| `page_group` | Planning bucket for architecture and reporting |
| `hub` | Main hub the page belongs to |
| `primary_keyword` | The one keyword family the page should own |
| `secondary_keywords` | A short list of approved supporting variants, not all raw variants |
| `search_intent` | `commercial`, `transactional`, `comparison`, or `informational` |
| `funnel_stage` | `TOFU`, `MOFU`, or `BOFU` |
| `market` | Primary market target |
| `priority` | `P1`, `P2`, or `P3` |
| `publish_wave` | `launch`, `post_launch_q1`, `post_launch_q2`, or `later` |
| `feature_set` | Embedded features relevant to that page family |
| `pricing_visibility` | How plan-sensitive features should be qualified |
| `keyword_family_notes` | Why the page owns that family |
| `status` | Planning state for the row |

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

### `content_calendar.csv`

| Column | Meaning |
| --- | --- |
| `content_id` | Internal content task ID |
| `page_slug` | Canonical page the content supports |
| `page_group` | Architecture bucket copied from the page inventory |
| `hub` | Main hub the content belongs to |
| `title` | Working content title |
| `content_type` | Page/content format |
| `parent_page_slug` | Primary money page this content supports; mainly used for blogs and support content |
| `parent_keyword_family` | Canonical keyword family the content is designed to strengthen |
| `content_role` | Content job such as `money_page`, `definition`, `how_to`, `comparison`, `examples`, or `use_case_support` |
| `cluster_name` | Cluster label used to group related support content around the same parent family |
| `target_keyword` | Mapped keyword to support; may be blank for architecture rows pending keyword import |
| `target_market` | Primary target market |
| `target_language` | Content language |
| `funnel_stage` | Funnel role |
| `priority` | Publishing priority |
| `feature_set` | Relevant embedded features for the brief and page sections |
| `pricing_visibility` | How to qualify plan-gated features in the content |
| `primary_internal_link_target` | Main page this content should push authority to |
| `secondary_internal_link_targets` | Optional supporting internal-link targets |
| `serp_intent_type` | Search-intent format such as `informational`, `comparison`, `examples`, or `commercial_informational` |
| `refresh_priority` | Relative refresh urgency such as `high`, `medium`, or `low` |
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
| `da_score` | Domain authority score |
| `monthly_traffic` | Estimated monthly traffic |
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

### `rank_tracker.csv`

| Column | Meaning |
| --- | --- |
| `keyword` | Tracked keyword |
| `page_slug` | Page owning the keyword |
| `hub` | Hub the keyword belongs to |
| `priority` | Keyword priority (P1/P2/P3) |
| `position` | Current SERP position |
| `previous_position` | Previous SERP position |
| `change` | Position change (+/-) |
| `serp_features` | SERP features present (featured snippet, PAA, etc.) |
| `date` | Date of measurement |
| `notes` | Observations |

### `monthly_metrics.csv`

| Column | Meaning |
| --- | --- |
| `month` | Reporting month (YYYY-MM) |
| `organic_traffic` | Total organic sessions |
| `organic_users` | Total organic users |
| `conversions_create_profile` | Profile creation conversions from organic |
| `top_keyword` | Best performing keyword |
| `top_page` | Best performing page |
| `backlinks_acquired` | New backlinks acquired |
| `new_referring_domains` | New referring domains |
| `indexed_pages` | Total indexed pages |
| `avg_position_p1` | Average position for P1 keywords |
| `cwv_pass_rate` | Core Web Vitals pass rate |
| `notes` | Monthly observations |

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

## Product Catalog Model

ProfileTap also has a future product-catalog layer. This is documented now, but not yet added to `page_master.csv`.

Two parallel commercial layers are planned:

- `solution pages`
  Hubs, categories, use cases, and comparisons that explain the workflow, audience, or use case
- `product pages`
  Physical product-family buying pages intended to live under `/products/...`

Current documented product families:

- metal business cards
- wooden NFC cards
- PVC business cards
- business standees
- keychains
- pet tags
- google review cards
- travel safety kit / luggage card
- vehicle sticker

Product-intent rules:

- product pages own buyable physical-product intent
- solution pages own use-case, workflow, and identity intent
- solution pages can recommend product families
- product pages can link back to relevant solution pages
- overlapping families must be separated by intent, not merged blindly

Key overlap examples:

- `pet tags` vs `pet ID profile`
- `luggage card` vs `qr luggage tag`
- `vehicle sticker` vs `vehicle qr code sticker`
- `google review card` vs review-assist or review-solution messaging

Recommended future product-page model:

- use a dedicated `/products/...` catalog area
- start with family pages, not variant pages
- keep colors, finishes, QR-only, NFC+QR, and similar options on the family page
- create standalone variant pages only when keyword demand and SERP behavior justify them
- do not create profession-specific product pages like `metal business card for doctors` by default

Documented future product-family examples:

- `/products/metal-business-cards`
- `/products/wooden-nfc-cards`
- `/products/pvc-business-cards`
- `/products/business-standees`
- `/products/keychains`
- `/products/pet-tags`
- `/products/google-review-cards`
- `/products/luggage-cards`
- `/products/vehicle-stickers`

Reserved future schema support for product pages:

- `page_type=product_family`
- `page_group=product_catalog`
- `page_subtype`
- `variant_strategy`
- `commercial_model=physical_product`

Operating rule:

- do not add product rows to `page_master.csv` until keyword validation and page decisions are finalized

## Current Keyword Rebuild

The current rebuild was generated from the temporary source export in `Downloads` and produces:

- `2023` raw keyword rows in `raw_keyword_bank.csv`
- `29` canonical execution rows in `execution_seo_master.csv`

Current consolidation rule:

- city, adjective, and price-modified variants are excluded from the raw bank by default
- only canonical page-worthy families surface in the execution master
- unsupported profession/use-case rows are excluded instead of being forced into the wrong page family

## Blog Cluster Model

Blogs are managed as children of money pages, not as standalone topic ideas.

Core rule:

- every blog gets one `parent_page_slug`
- every blog gets one `parent_keyword_family`
- every blog exists to strengthen one conversion page first

Recommended `content_role` values:

- `money_page`
- `definition`
- `how_to`
- `comparison`
- `examples`
- `use_case_support`
- `feature_support`
- `industry_support`
- `problem_solution`

Recommended cluster model:

- one parent page
- 5 to 10 child blogs
- all child blogs link back to the parent page
- strongest child blogs can cross-link within the same cluster

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

## Ubersuggest Update Workflow

When reviewing keywords in Ubersuggest, update these fields in [raw_keyword_bank.csv](/Users/hariomshah/Documents/GitHub/profiletap-seo-os/data/keywords/raw_keyword_bank.csv):

- `ubersuggest_volume`
- `ubersuggest_kd`
- `ubersuggest_cpc`
- `ubersuggest_last_checked`
- `notes` for useful SERP observations

## Current Baseline

The repository is initialized with a launch-first SEO system:

- 46 mapped keyword families in execution_seo_master.csv
- 46 planned pages in page_master.csv
- 40 content items in the calendar
- 35 backlink prospects

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

1. Import and clean keywords into `raw_keyword_bank.csv`.
2. Promote approved families into `execution_seo_master.csv`.
3. Create or update architecture rows in `page_master.csv`, including `page_group`, `hub`, `feature_set`, and `publish_wave`.
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

### Strategy Docs

- `docs/02-seo-strategy.md` — Market strategy, launch architecture, and execution priorities
- `docs/03-technical-seo.md` — Schema markup, meta tags, Core Web Vitals, sitemaps, canonicals
- `docs/04-internal-linking-strategy.md` — Cross-linking matrix, anchor text rules, link equity flow
- `docs/05-measurement-plan.md` — KPIs, tools, reporting cadence, alert thresholds
- `docs/06-competitor-serp-analysis.md` — SERP analysis workflow, competitor monitoring
- `docs/07-content-distribution.md` — Social, community, email distribution channels
- `docs/08-image-seo-guidelines.md` — Alt text, file naming, OG/Twitter Card templates

### SOPs

- `sop/page-mapping-process.md` — Anti-cannibalization, keyword-to-page mapping
- `sop/content-review-process.md` — Brief-to-publish QA workflow
- `sop/keyword-refresh-cycle.md` — Monthly/quarterly keyword refresh
- `sop/backlink-audit-process.md` — Prospect qualification, outreach templates
- `sop/content-refresh-triggers.md` — When and how to refresh published pages
- `sop/schema-markup-implementation.md` — JSON-LD templates by page type

### Prompts & Templates

- `prompts/content-brief-prompt.md` — Brief generation rules (12-section output)
- `prompts/competitor-analysis-prompt.md` — SERP competitor analysis
- `prompts/blog-cluster-expansion-prompt.md` — Blog cluster plans per hub
- `prompts/schema-markup-prompt.md` — JSON-LD generation by page type
- `briefs/templates/page-brief-template.md` — Standard brief template (12 sections)

### Scripts

- `scripts/rebuild_keyword_system.py` — Rebuild keyword CSVs from source exports
- `scripts/validate_system.py` — Cross-file integrity checks (run with `python3 scripts/validate_system.py`)

### Skills (Claude Code Slash Commands)

**General SEO** (reusable across projects — `skills/general-seo/`):
- `/keyword-research` — Keyword research methodology
- `/content-optimization` — On-page SEO optimization
- `/technical-seo-audit` — Technical SEO audit
- `/backlink-strategy` — Link building strategy
- `/serp-analysis` — SERP analysis
- `/content-cluster-planning` — Topic cluster design
- `/local-seo` — Local SEO strategy
- `/rank-tracking-analytics` — Measurement and analytics
- `/content-refresh-strategy` — Content refresh methodology
- `/programmatic-seo` — Programmatic SEO
- `/blog-writer` — Full blog draft generation from briefs

**ProfileTap-Specific** (`skills/profiletap/`):
- `/profiletap-context` — Product, features, market, competitors
- `/profiletap-architecture` — Page architecture and structure
- `/profiletap-keywords` — Keyword system management
- `/profiletap-brief` — Content brief generation
- `/profiletap-backlinks` — Backlink operations
- `/profiletap-measurement` — Performance measurement
- `/profiletap-blog-writer` — Full blog drafts with ProfileTap voice and context

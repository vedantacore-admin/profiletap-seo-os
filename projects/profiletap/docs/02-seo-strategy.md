# ProfileTap SEO Strategy

## Positioning

ProfileTap is positioned as a smart identity management platform, not only as an NFC card or link-in-bio tool.

Core capability areas:

- digital business cards using NFC and QR
- smart profile pages for business and personal identity
- multi-use identity for creators, families, pets, travel, and vehicles
- analytics, AI-assisted review support, and privacy features

## Market Priority

- Primary market: India
- Secondary market: global English demand

The operating assumption is that India transactional demand and India-focused competitor comparisons produce the fastest commercial SEO wins, but the launch architecture must already reflect the broader platform.

## Competitor Landscape

### Direct competitors

- HiHello
- Popl
- Blinq
- TapOnn
- Tapmo

### Indirect competitors

- Linktree
- Beacons
- Carrd

### Strategic implication

- global competitors are useful for discovering demand and comparison terms
- India competitors and India-modified commercial terms are the faster path to page-one opportunities
- informational content exists to support commercial pages, not replace them as the primary growth engine

## Keyword Model

The keyword system now has two layers:

- `data/keywords/raw_keyword_bank.csv`
  Retained import inventory for approved keyword families only
- `data/keywords/execution_seo_master.csv`
  Canonical page-owned keyword families for execution

### Raw keyword bank role

Use `raw_keyword_bank.csv` as the clean retained keyword bank.

Critical fields:

- `canonical_keyword`
- `canonical_page_slug`
- `keep_status`
- `merge_reason`
- `modifier_type`
- `ubersuggest_volume`
- `ubersuggest_kd`
- `ubersuggest_cpc`

Allowed `keep_status` values:

- `keep_primary`
- `keep_secondary`

The rebuild script may still reject imported rows internally, but those rows are not stored in the raw bank.

### Execution SEO master role

Use `execution_seo_master.csv` as the actual SEO planning sheet.

Its job is:

- one page owns one keyword family
- secondary variations stay short and controlled
- city and adjective variants do not become standalone execution rows
- rejected ideas stay out of the publishing system until validated elsewhere

### Rebuild rules

Current rebuild assumptions:

- city, `best`, `cheap`, `premium`, `custom`, `buy`, `online`, and similar variants are merged by default
- unsupported professions are excluded instead of being force-mapped
- comparison terms stay separate from category and hub intent
- travel-agent business intent stays separate from travel utility intent
- blogs only survive as support content tied to commercial parents

### Ubersuggest workflow

After each import rebuild:

- fill Ubersuggest metrics in `raw_keyword_bank.csv`
- validate `keep_status` and `canonical_page_slug` for the kept rows
- promote only approved families into downstream mapping and content work

## Launch Architecture

### Homepage

- `/`
  Owns broad platform positioning and lists the full feature inventory once

### Fixed launch hubs

- `/business-identity`
- `/creator-identity`
- `/family-safety-profile`
- `/pet-id-profile`
- `/travel-profile`
- `/vehicle-profile`

These pages are the fixed launch architecture. They own the top-level product story by audience or life category, and they repeat only the feature subset relevant to that hub.

### Business child pages

- `/digital-business-card-india`
- `/nfc-business-card-india`
- `/qr-business-card`
- `/digital-business-card-for-doctors`
- `/digital-business-card-for-real-estate-agents`
- `/digital-business-card-for-freelancers`
- `/hihello-alternative-india`
- `/popl-alternative-india`
- `/tapmo-alternative`
- `/profiletap-vs-hihello`
- `/profiletap-vs-tapmo`

### Creator child pages

- `/digital-business-card-for-creators`
- `/linktree-alternative-for-creators`

## Product Catalog Layer

The product catalog is live. Data source: `data/products/product_catalog.json`. Product family pages live at `/products/{slug}`.

### Product vs solution intent

- solution pages own use-case, workflow, and identity intent
- product pages own physical-product buying intent
- solution pages show product cards via the `relevant_pages` mapping in product_catalog.json
- product pages link back to solution pages
- overlapping product and solution areas are separated by intent, not merged

Intent separation examples:

| Product Page (buying intent) | Solution Page (use-case intent) |
|---|---|
| `/products/car-stickers` | `/vehicle-qr-code-sticker` |
| `/products/luggage-tags` | `/qr-luggage-tag` |
| `/products/pet-collar-tags` | `/lost-and-found-qr-tag` |
| `/products/family-safety-tags` | `/emergency-qr-code` |
| `/products/review-cards` | `/ai-review-assist` |

### Active product families

| Product ID | Product Family | Hubs | Type |
|---|---|---|---|
| `metal-business-cards` | Metal Business Cards | business | physical |
| `business-standees` | Business Standees | business | physical |
| `pvc-business-cards` | PVC Business Cards | business | physical |
| `keychains` | Keychains | business, family_safety | physical |
| `pet-collar-tags` | Pet Collar Tags | pet | physical |
| `review-cards` | Review Cards | business | physical |
| `car-stickers` | Car Stickers | vehicle | physical |
| `luggage-tags` | Luggage Tags | travel | physical |
| `family-safety-tags` | Family Safety Tags | family_safety | physical |
| `digital-profiles` | Digital Profiles | all hubs | digital |

### Product-page model

- dedicated `/products/...` URL area with `/products` index page
- one product-family page per product — variants (colors, designs) on the family page
- `page_type=product_family`, `page_group=product_catalog` in CSVs
- do not create profession-specific product pages (e.g., "metal business card for doctors") — the solution use-case page owns that intent
- product cards render dynamically on solution pages and blogs using `relevant_pages` and `relevant_blogs` arrays from product_catalog.json

### Later support blogs

- `/blog/what-is-digital-business-card`
- `/blog/how-nfc-business-cards-work`
- `/blog/how-qr-code-works`
- `/blog/nfc-vs-qr-business-card`
- `/blog/digital-business-card-examples`

Blogs are not part of the launch architecture and should only support existing hubs or child money pages.

## Feature Handling

Features are reusable modules, not standalone SEO pages in the current architecture.

Rules:

- homepage lists the full feature inventory once
- top-level hubs only surface the subset of features relevant to that category
- child pages inherit only the features that support their conversion intent
- pricing sensitivity is managed in page messaging through `pricing_visibility`, not by splitting features into separate URLs
- if later keyword data proves distinct standalone feature demand, a dedicated feature page can be added later

### Canonical feature glossary

Use these canonical `feature_set` tokens in planning data:

| Token | Human label |
| --- | --- |
| `digital_profiles` | Digital profiles |
| `nfc_sharing` | NFC sharing |
| `qr_sharing` | QR sharing |
| `ai_review_assist` | AI review assist |
| `analytics` | Analytics |
| `account_collaborators` | Manage account collaborators |
| `multi_account_team_management` | Manage multiple accounts / teams |
| `multi_profile_type_profiles` | Multi-profile / multi-type profiles |
| `call_masking` | Call masking |
| `whatsapp_masking` | WhatsApp masking |
| `theme_library` | Wide range of themes |
| `advanced_creator_analytics` | Advanced analytics for creators |

Interpretation rules:

- token names are for internal consistency in CSVs
- page copy should use natural human phrasing
- `advanced_creator_analytics` is creator-specific and likely subscription-sensitive
- masking features are privacy tools, not separate privacy-page intents
- collaboration and team management should usually appear on business and creator pages, not safety-led hubs

### Hub-level feature emphasis

| Hub | Main embedded features |
| --- | --- |
| `business` | profiles, NFC, QR, AI review assist, analytics, collaborators, team management, masking, themes |
| `creator` | profiles, NFC, QR, AI review assist, analytics, team management, multi-profile types, themes, creator analytics |
| `family_safety` | profiles, QR, multi-profile types, masking, themes |
| `pet` | profiles, QR, multi-profile types, themes |
| `travel` | profiles, QR, multi-profile types, masking, themes |
| `vehicle` | profiles, QR, multi-profile types, masking, themes |

## Current Execution Sequence

### Phase 1: launch architecture

- homepage messaging refresh
- business identity hub
- creator identity hub
- family safety hub
- pet hub
- travel hub
- vehicle hub

### Phase 2: business and creator child pages

- digital business card India category page
- NFC business card India category page
- QR business card category page
- doctors
- real estate agents
- freelancers
- creators

### Phase 3: competitor capture

- HiHello alternative India
- Popl alternative India
- TapMo alternative
- ProfileTap vs HiHello
- ProfileTap vs TapMo
- Linktree alternative for creators

### Phase 4: authority support content

- what is digital business card
- how NFC business cards work
- how QR code works
- NFC vs QR business card
- digital business card examples

## Blog Cluster Model

Support content should scale through parent-child clusters, not isolated blog ideas.

### Parent-child rule

- every blog has one `parent_page_slug`
- every blog has one `parent_keyword_family`
- every blog should pass authority to one primary conversion page
- a blog may link to multiple pages on-site, but the system should treat only one page as its primary parent

### Required content-calendar fields

Add and use these fields in `data/content/content_calendar.csv`:

- `parent_page_slug`
- `parent_keyword_family`
- `content_role`
- `cluster_name`
- `primary_internal_link_target`
- `secondary_internal_link_targets`
- `serp_intent_type`
- `refresh_priority`

### Recommended `content_role` values

- `money_page`
- `definition`
- `how_to`
- `comparison`
- `examples`
- `use_case_support`
- `feature_support`
- `industry_support`
- `problem_solution`

### Cluster sizing by segment

Recommended long-term blog-cluster range:

| Segment | Cluster count |
| --- | ---: |
| Business | 12-18 |
| Creator | 6-10 |
| Family safety | 4-6 |
| Pet | 4-6 |
| Travel | 3-5 |
| Vehicle | 4-6 |
| Comparison support | 5-8 |
| Platform / identity education | 4-6 |

Rule of thumb:

- 5 to 10 blogs per cluster
- one money page can support multiple clusters
- do not create a cluster unless the parent page is commercially important

## Management Cadence

### Weekly

- update content and outreach statuses
- resolve blocked briefs
- add new keyword mapping decisions

### Monthly

- refresh Ubersuggest metrics for active clusters
- re-rank `P1`, `P2`, and `P3` using business score plus demand
- review pages due for refresh
- compare published output vs launch and post-launch waves

### Quarterly

- decide the next cluster expansion beneath the launch hubs
- review whether India-first focus is still returning the best commercial outcomes
- expand feature-led or vertical-led coverage only when keyword data shows distinct intent

## Backlink Strategy

The backlink system is maintained in `data/backlinks/backlink_targets.csv` and executed via `data/backlinks/outreach_tracker.csv`.

### Current target themes

- startup and founder media for homepage and business category pages
- marketing publications for creator positioning
- healthcare media for the doctor vertical
- real estate media for the agent vertical

### Current seeded support

| Target page | Example domains |
| --- | --- |
| `/` | `yourstory.com` |
| `/digital-business-card-india` | `inc42.com`, `entrackr.com` |
| `/nfc-business-card-india` | `businessworld.in` |
| `/digital-business-card-for-creators` | `exchange4media.com`, `socialsamosa.com` |
| `/hihello-alternative-india` | `indianstartupnews.com` |
| `/digital-business-card-for-doctors` | `expresshealthcare.in` |

## Operating Rules

- one keyword intent maps to one page only
- no new page is created without checking existing mapped intent
- no content item is added without a target keyword or planned architecture row
- every backlink target must support an existing page slug
- India commercial demand outranks global top-of-funnel traffic until core pages are live
- do not create standalone feature pages unless keyword intent is clearly distinct from the parent hub

## Data Gaps

- `volume` is not populated yet
- `kd` is not populated yet
- `cpc` is not populated yet
- launch hub rows still need full keyword import
- page statuses are still `planned`
- content statuses are still `brief_pending`
- outreach contacts have not been qualified yet

## Immediate Next Actions

1. import the full keyword master and map it into the launch hub architecture
2. brief all launch-core hub pages first
3. re-rank child pages after Ubersuggest enrichment
4. qualify outreach contacts for the seeded backlink targets

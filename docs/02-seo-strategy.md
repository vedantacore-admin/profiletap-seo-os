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

The keyword system is maintained in `data/keywords/master_keywords.csv` with a one-to-one mapping into `data/pages/page_keyword_map.csv`.

The file supports annual management, not only ideation. Use these fields actively:

- `pillar` for portfolio planning
- `funnel_stage` for balancing TOFU, MOFU, and BOFU output
- `target_market` and `target_language` for India-first expansion control
- `business_score` for commercial weighting
- `volume`, `kd`, and `cpc` for Semrush-backed reprioritization
- `semrush_last_checked` to keep research current

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
- `/taponn-alternative`
- `/blinq-alternative`

### Creator child pages

- `/digital-business-card-for-creators`
- `/linktree-alternative-for-creators`

### Later support blogs

- `/blog/nfc-business-card-vs-qr-code`
- `/blog/paper-vs-digital-business-card`
- `/blog/best-digital-business-card-for-doctors-india`
- `/blog/how-to-create-digital-business-card`

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
- TapOnn alternative
- Blinq alternative
- Linktree alternative for creators

### Phase 4: authority support content

- NFC vs QR
- paper vs digital business cards
- doctor-focused roundup
- digital business card how-to

## Management Cadence

### Weekly

- update content and outreach statuses
- resolve blocked briefs
- add new keyword mapping decisions

### Monthly

- refresh Semrush metrics for active clusters
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
3. re-rank child pages after Semrush enrichment
4. qualify outreach contacts for the seeded backlink targets

# ProfileTap SEO Strategy

## Positioning

ProfileTap is positioned as a smart identity platform, not only as an NFC card or link-in-bio tool.

Core capability areas:

- digital business cards using NFC and QR
- smart profile pages for business and personal identity
- multi-use identity for professionals, creators, families, pets, travel, and vehicles
- analytics, AI-assisted profile content, and privacy features

## Market Priority

- Primary market: India
- Secondary market: global English demand

The operating assumption is that India transactional demand and India-focused competitor comparisons produce the fastest commercial SEO wins.

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

- Global competitors are useful for discovering demand and comparison terms.
- India competitors and India-modified commercial terms are the faster path to page-one opportunities.
- Informational content exists to support commercial pages, not replace them as the primary growth engine.

## Keyword Model

The keyword system is maintained in `data/keywords/master_keywords.csv` with a one-to-one mapping into `data/pages/page_keyword_map.csv`.

The file now supports annual management, not only ideation. Use these fields actively:

- `pillar` for portfolio planning
- `funnel_stage` for balancing TOFU, MOFU, and BOFU output
- `target_market` and `target_language` for India-first expansion control
- `business_score` for commercial weighting
- `volume`, `kd`, and `cpc` for Semrush-backed reprioritization
- `semrush_last_checked` to keep research current

### Priority buckets

- `P1`: India-first transactional and high-intent comparison terms
- `P2`: supporting transactional variations, secondary comparisons, and commercial education
- `P3`: lower-priority informational expansion

### Current clusters

| Cluster | Intent | Priority focus | Page type |
| --- | --- | --- | --- |
| `digital_business_card` | transactional | India commercial demand | category |
| `nfc_business_card` | transactional | product-led commercial demand | category |
| `qr_business_card` | transactional | product-led commercial demand | category |
| `doctor_use_case` | transactional | vertical conversion | use_case |
| `real_estate_use_case` | transactional | vertical conversion | use_case |
| `freelancer_use_case` | transactional | vertical conversion | use_case |
| `creator_use_case` | transactional | creator segment expansion | use_case |
| `hihello_comparison` | comparison | competitor capture | comparison |
| `popl_comparison` | comparison | competitor capture | comparison |
| `taponn_comparison` | comparison | India competitor capture | comparison |
| `blinq_comparison` | comparison | secondary competitor capture | comparison |
| `linktree_comparison` | comparison | adjacent demand capture | comparison |
| `nfc_vs_qr` | informational | mid-funnel education | blog |
| `paper_vs_digital` | informational | demand reframing | blog |
| `doctor_roundup` | informational | vertical authority | blog |
| `how_to_digital_card` | informational | low-priority education | blog |
| `brand_positioning` | commercial | homepage narrative | homepage |

## Page Architecture

### Homepage

- `/`
  Owns the broad positioning term `smart identity platform`

### Category pages

- `/digital-business-card-india`
- `/nfc-business-card-india`
- `/qr-business-card`

These pages should absorb generic transactional demand and link outward to vertical and comparison pages.

### Use-case pages

- `/digital-business-card-for-doctors`
- `/digital-business-card-for-real-estate-agents`
- `/digital-business-card-for-freelancers`
- `/digital-business-card-for-creators`

These pages should convert vertical demand using segment-specific proof, workflows, and CTAs.

### Comparison pages

- `/hihello-alternative-india`
- `/popl-alternative-india`
- `/taponn-alternative`
- `/blinq-alternative`
- `/linktree-alternative-for-professionals`

These pages should target switch intent and product evaluation intent.

### Blog pages

- `/blog/nfc-business-card-vs-qr-code`
- `/blog/paper-vs-digital-business-card`
- `/blog/best-digital-business-card-for-doctors-india`
- `/blog/how-to-create-digital-business-card`

These pages should internally link to the relevant category or use-case money pages.

## Current Execution Sequence

### Phase 1: commercial foundation

- homepage messaging refresh
- digital business card India category page
- NFC business card India category page
- QR business card category page

### Phase 2: high-conversion vertical pages

- doctors
- real estate agents
- freelancers

### Phase 3: competitor capture

- HiHello alternative India
- Popl alternative India
- TapOnn alternative

### Phase 4: authority support content

- NFC vs QR
- paper vs digital business cards
- doctor-focused roundup

## Management Cadence

### Weekly

- update content and outreach statuses
- resolve blocked briefs
- add new keyword mapping decisions

### Monthly

- refresh Semrush metrics for active clusters
- re-rank `P1`, `P2`, and `P3` using business score plus demand
- review pages due for refresh
- compare published output vs quarter plan

### Quarterly

- decide the next cluster expansion
- review whether India-first focus is still returning the best commercial outcomes
- expand feature-led or vertical-led coverage based on live performance

## Backlink Strategy

The backlink system is maintained in `data/backlinks/backlink_targets.csv` and executed via `data/backlinks/outreach_tracker.csv`.

### Current target themes

- startup and founder media for homepage and category pages
- marketing publications for creator and professional identity positioning
- healthcare media for the doctor vertical
- real estate media for the agent vertical

### Current `P1` backlink support

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
- no content item is added without a target keyword
- every backlink target must support an existing page slug
- India commercial demand outranks global top-of-funnel traffic until core pages are live

## Data Gaps

- `volume` is not populated yet
- `kd` is not populated yet
- `cpc` is not populated yet
- page statuses are still `planned`
- content statuses are still `brief_pending`
- outreach contacts have not been qualified yet

## Immediate Next Actions

1. populate `volume` and `kd` for all existing keywords
2. brief all `P1` pages first
3. qualify outreach contacts for the 12 seeded backlink targets
4. expand India-specific vertical and city-intent keyword coverage after the first commercial pages are published

# ProfileTap Keyword System

## Two-Layer Architecture

ProfileTap uses a two-layer keyword model:

1. **Raw Bank** (`data/keywords/raw_keyword_bank.csv`): Retained research inventory of all approved keyword rows
2. **Execution Master** (`data/keywords/execution_seo_master.csv`): Canonical page-to-keyword mapping for execution

Flow: raw export -> raw_keyword_bank.csv (keep_primary + keep_secondary only) -> execution_seo_master.csv (page-ready families)

## Layer 1: Raw Keyword Bank

File: `data/keywords/raw_keyword_bank.csv`

### Column Schema

| Column | Purpose |
| --- | --- |
| `keyword` | Exact imported keyword from source sheet |
| `source_category` | Imported bucket: `Platform`, `Business`, `Use Case`, `Competitor`, `Discovery`, `Supplemental`, `AI` |
| `observed_intent` | Normalized intent: `commercial`, `transactional`, `informational`, `navigational` |
| `market` | `IN` or `IN+GLOBAL` based on modifier signals |
| `modifier_type` | Classification: `none`, `city`, `best`, `comparison`, `profession`, `feature`, `online`, `buy`, `country` |
| `root_topic` | Internal canonical family label (e.g., `smart_identity_platform`, `digital_business_card`) |
| `canonical_keyword` | The canonical keyword the row consolidates into |
| `canonical_page_slug` | Canonical page that owns this keyword family |
| `keep_status` | `keep_primary` or `keep_secondary` |
| `merge_reason` | Why the row belongs to that canonical family |
| `notes` | Free notes, source sheet references, volume hints |
| `ubersuggest_volume` | Search volume (to be filled via Ubersuggest) |
| `ubersuggest_kd` | Keyword difficulty (to be filled) |
| `ubersuggest_cpc` | CPC (to be filled) |
| `ubersuggest_last_checked` | Last Ubersuggest refresh date |

### Keep Status Rules

- `keep_primary`: The canonical head keyword for a family. Exactly one per family. This keyword becomes the `primary_keyword` in execution_seo_master.csv.
- `keep_secondary`: Approved supporting variant within the same family. Contributes to `secondary_keywords` in the execution master.
- Rejected rows are NOT stored in the raw bank at all. The rebuild script filters them out.

### Modifier Handling

These modifiers are merged into their parent family by default:

| Modifier Type | Example | Merge Rule |
| --- | --- | --- |
| `city` | "digital business card mumbai" | Merged into `/digital-business-card-india` |
| `best` | "best digital business card" | Merged into parent category family |
| `cheap` / `premium` / `custom` | "cheap NFC card" | Merged into parent category family |
| `buy` / `online` | "buy NFC business card online" | Merged into parent category family |
| `country` (India) | "NFC business card India" | Becomes part of India-targeted page family |

City list used for exclusion: Mumbai, Delhi, Bangalore/Bengaluru, Pune, Hyderabad, Chennai, Kolkata, Ahmedabad, Jaipur, Noida, Gurgaon/Gurugram.

### Profession Mapping Rules

Professions that get dedicated use-case pages:
- Doctors -> `/digital-business-card-for-doctors`
- Real estate agents -> `/digital-business-card-for-real-estate-agents`
- Freelancers -> `/digital-business-card-for-freelancers`
- Creators (including influencers, bloggers, YouTubers) -> `/digital-business-card-for-creators`

Professions that are EXCLUDED from dedicated pages by default:
- Lawyers, accountants, consultants, architects, photographers, musicians, teachers, trainers, coaches
- These are merged into the parent category page or excluded entirely
- Only create profession pages when keyword demand and distinct pain points justify them

### Current Raw Bank Stats

- Total rows: ~200+ approved keywords
- Families represented: platform, business, NFC, QR, profession (4 types), competitor (6 brands), discovery, supplemental utilities
- Source categories: Platform, Business, Use Case, Competitor, Discovery, Supplemental, AI

## Layer 2: Execution Master

File: `data/keywords/execution_seo_master.csv`

### Column Schema

| Column | Purpose |
| --- | --- |
| `page_slug` | Canonical page that owns the keyword family |
| `page_type` | `homepage`, `solution_hub`, `category`, `use_case`, `comparison`, `blog` |
| `page_group` | Planning bucket: `homepage`, `solution_hub`, `category`, `use_case`, `comparison`, `blog` |
| `hub` | Main hub: `platform`, `business`, `creator`, `family_safety`, `pet`, `travel`, `vehicle` |
| `primary_keyword` | The one keyword family the page owns |
| `secondary_keywords` | Short list of approved supporting variants (pipe-delimited) |
| `search_intent` | `commercial`, `transactional`, `comparison`, `informational` |
| `funnel_stage` | `TOFU`, `MOFU`, `BOFU` |
| `market` | `IN` or `IN+GLOBAL` |
| `priority` | `P1`, `P2`, `P3` |
| `publish_wave` | `launch`, `post_launch_q1`, `post_launch_q2`, `later` |
| `feature_set` | Embedded features (pipe-delimited tokens) |
| `pricing_visibility` | `contextual` or `all_plans` |
| `keyword_family_notes` | Why the page owns that family |
| `status` | `planned`, `needs_validation`, `in_progress`, `published` |

### One Keyword Intent = One Page Rule

This is the core operating principle:
- Every keyword intent maps to exactly one page
- No keyword is assigned to multiple pages
- If two keywords express the same underlying intent, they belong to one page
- Secondary keywords are supporting variants within the same family, not separate intents

### Priority Tiers

| Tier | Meaning | Execution Impact |
| --- | --- | --- |
| `P1` | Highest commercial value, fastest path to revenue | Brief and publish first; daily keyword monitoring |
| `P2` | Strong commercial or strategic value | Brief after P1 wave; weekly monitoring |
| `P3` | Support content or lower-volume opportunity | Brief when parent pages are live; monthly monitoring |

### Current P1 Keywords (13 families)

| Primary Keyword | Page Slug | Hub | Wave |
| --- | --- | --- | --- |
| smart identity platform | `/` | platform | launch |
| business identity management platform | `/business-identity` | business | launch |
| digital business card india | `/digital-business-card-india` | business | post_launch_q1 |
| nfc business card india | `/nfc-business-card-india` | business | post_launch_q1 |
| qr business card | `/qr-business-card` | business | post_launch_q1 |
| digital business card for doctors | `/digital-business-card-for-doctors` | business | post_launch_q2 |
| digital business card for real estate agents | `/digital-business-card-for-real-estate-agents` | business | post_launch_q2 |
| digital business card for freelancers | `/digital-business-card-for-freelancers` | business | post_launch_q2 |
| hihello alternative india | `/hihello-alternative-india` | business | post_launch_q1 |
| popl alternative india | `/popl-alternative-india` | business | post_launch_q1 |
| tapmo alternative | `/tapmo-alternative` | business | post_launch_q1 |
| taponn alternative | `/taponn-alternative` | business | post_launch_q1 |

### Publish Waves

| Wave | Scope | Typical Priority |
| --- | --- | --- |
| `launch` | Homepage + 6 hubs (7 pages) | P1-P3 |
| `post_launch_q1` | Core business categories + comparisons + creator child (8 pages) | P1-P2 |
| `post_launch_q2` | Profession pages + deeper comparisons + utility child pages (12 pages) | P1-P2 |
| `later` | Blog support content + deferred utilities (5+ pages) | P3 |

## Rebuild Script

Usage:
```
python scripts/rebuild_keyword_system.py [source_path]
```

If no `source_path` is given, defaults to the temporary export in `~/Downloads/`.

The script:
1. Reads the source CSV or XLSX export
2. Normalizes keyword text and applies modifier detection
3. Filters out city, adjective, and price variants
4. Maps keywords to canonical families and page slugs
5. Assigns `keep_status` (keep_primary, keep_secondary)
6. Outputs `raw_keyword_bank.csv` and `execution_seo_master.csv`

The script handles XLSX imports directly via XML parsing.

## Ubersuggest Enrichment Workflow

After each import rebuild:

1. Open `raw_keyword_bank.csv`
2. For each `keep_primary` row, look up in Ubersuggest:
   - `ubersuggest_volume`
   - `ubersuggest_kd`
   - `ubersuggest_cpc`
3. Update `ubersuggest_last_checked` with the date
4. Add SERP observations to `notes` column
5. Validate `keep_status` and `canonical_page_slug` based on volume data
6. Promote only validated families into downstream mapping and content work
7. Re-rank P1/P2/P3 priorities based on volume + business value

## Validation Checks

Run these checks before any content production:

### Orphan Keywords
- Every `keep_primary` row in raw_keyword_bank.csv must have a matching `page_slug` in execution_seo_master.csv
- Every `canonical_page_slug` in the raw bank must exist in page_master.csv

### Slug Mismatches
- `canonical_page_slug` in raw bank must match `page_slug` in execution master
- `page_slug` in execution master must match `page_slug` in page_master.csv

### Duplicate Primaries
- No two rows in execution_seo_master.csv should have the same `primary_keyword`
- No two rows in raw_keyword_bank.csv should have `keep_primary` for the same `canonical_keyword`

### Intent Overlap
- Check that no two execution rows target the same underlying search intent
- Comparison keywords must not overlap with category keywords

## When to Add New Keywords vs Merge

Add a NEW keyword family (new execution row) when:
- The keyword represents a genuinely distinct search intent
- The keyword needs a different page type (category vs use_case vs comparison)
- The keyword targets a different audience segment
- SERP results for the keyword differ significantly from existing families

MERGE into an existing family when:
- The keyword is a wording variation (digital business card = digital visiting card)
- The keyword adds a modifier (city, adjective, price) to an existing family
- The keyword is a long-tail version of an existing family
- SERP results overlap significantly with the existing family

## Comparison Keyword Isolation Rules

Comparison keywords must ALWAYS be isolated from category and hub intent:
- "hihello alternative" -> comparison page, never on business hub
- "hihello alternative india" -> India-specific comparison page
- "profiletap vs hihello" -> separate vs page (different from alternative page)
- "linktree alternative for creators" -> creator comparison page, never on creator hub
- "best digital business card" -> merges into category page (this is NOT a comparison keyword)

Alternative pages and vs pages are separate intents:
- `/hihello-alternative-india` (alternative/switch intent)
- `/profiletap-vs-hihello` (head-to-head comparison intent)

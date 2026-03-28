# ProfileTap SEO OS

## What This Is

SEO operating system for **ProfileTap** — a smart identity management platform (not just an NFC card tool). This repo manages the full keyword → page → content → backlink pipeline.

## File Map

```
data/
  keywords/raw_keyword_bank.csv       # 232 retained keyword rows (research inventory)
  keywords/execution_seo_master.csv   # Canonical page-to-keyword families (one row per page)
  pages/page_master.csv               # Master page inventory with architecture
  content/content_calendar.csv        # Content production queue
  backlinks/backlink_targets.csv      # Link prospect list
  backlinks/outreach_tracker.csv      # Outreach execution status
  tracking/rank_tracker.csv           # Rank tracking data
  tracking/monthly_metrics.csv        # Monthly metrics rollup
  products/product_catalog.json       # Product catalog with variants, hub mapping, page mapping

docs/
  02-seo-strategy.md                  # Market strategy, launch architecture, execution phases
  03-technical-seo.md                 # Schema markup, meta tags, Core Web Vitals, sitemaps
  04-internal-linking-strategy.md     # Cross-linking matrix, anchor text rules
  05-measurement-plan.md              # KPIs, tools, reporting cadence
  06-competitor-serp-analysis.md      # SERP analysis workflow
  07-content-distribution.md          # Social, community, email distribution
  08-image-seo-guidelines.md          # Alt text, file naming, OG templates
  segment-feature-matrix.md           # Feature coverage by hub/segment

sop/
  page-mapping-process.md             # Anti-cannibalization, keyword-to-page mapping
  content-review-process.md           # Brief-to-publish QA workflow
  keyword-refresh-cycle.md            # Monthly/quarterly keyword refresh
  backlink-audit-process.md           # Prospect qualification, outreach templates
  content-refresh-triggers.md         # When and how to refresh published pages
  schema-markup-implementation.md     # JSON-LD templates by page type

prompts/
  content-brief-prompt.md             # Brief generation rules for Claude
  competitor-analysis-prompt.md       # SERP competitor analysis
  blog-cluster-expansion-prompt.md    # Blog cluster plans per hub
  schema-markup-prompt.md             # JSON-LD generation

briefs/templates/
  page-brief-template.md              # Standard brief structure (9 sections)

scripts/
  rebuild_keyword_system.py           # Rebuild keyword CSVs from source exports
  validate_system.py                  # Cross-file integrity checks

skills/
  general-seo/                        # Reusable SEO methodology (10 skills)
  profiletap/                         # ProfileTap domain knowledge (6 skills)
```

## CSV Schemas (Quick Reference)

**raw_keyword_bank.csv**: keyword, source_category, observed_intent, market, modifier_type, root_topic, canonical_keyword, canonical_page_slug, keep_status, merge_reason, notes, ubersuggest_volume, ubersuggest_kd, ubersuggest_cpc, ubersuggest_last_checked

**execution_seo_master.csv**: page_slug, page_type, page_group, hub, primary_keyword, secondary_keywords, search_intent, funnel_stage, market, priority, publish_wave, feature_set, pricing_visibility, keyword_family_notes, status

**page_master.csv**: page_slug, page_type, page_group, parent_page_slug, hub, page_title, primary_keyword, primary_intent, target_market, target_language, funnel_stage, conversion_goal, feature_set, pricing_visibility, primary_cta, owner, status, lifecycle_stage, publish_wave, publish_date, last_updated, next_refresh, notes

**content_calendar.csv**: content_id, page_slug, page_group, hub, title, content_type, parent_page_slug, parent_keyword_family, content_role, cluster_name, target_keyword, target_market, target_language, funnel_stage, priority, feature_set, pricing_visibility, primary_internal_link_target, secondary_internal_link_targets, serp_intent_type, refresh_priority, owner, status, brief_status, due_date, publish_date, refresh_date, publish_wave, notes

**backlink_targets.csv**: domain, site_type, da_score, monthly_traffic, target_page_slug, target_keyword, suggested_anchor, anchor_type, target_market, link_angle, priority, owner, status, notes

**outreach_tracker.csv**: domain, target_page_slug, contact_name, contact_email, status, first_contact_date, last_contact_date, next_follow_up_date, outcome, live_url, notes

**product_catalog.json**: product_id, product_family, product_name, description, product_type, hubs[], technology[], feature_set[], variants[], pricing_tier, pricing_visibility, page_slug, seo{primary_keyword, secondary_keywords, meta_description, search_intent, target_market}, relevant_pages[], relevant_blogs[], status, notes

## Operating Rules

1. **One keyword intent maps to one page only** — no cannibalization
2. **No content created without a mapped target page** — always check page_master first
3. **India-first transactional demand prioritized** before global expansion
4. **Comparisons, use cases, and blogs support commercial pages** — never cannibalize
5. **Features embedded into pages via feature_set** — no standalone feature pages unless keyword data proves distinct intent
6. **Product catalog lives in `data/products/product_catalog.json`** — product family pages own buying intent, solution pages own use-case intent

## Canonical Features (13 tokens)

| Token | Human Label |
|-------|-------------|
| `digital_profiles` | Digital profiles |
| `nfc_sharing` | NFC sharing |
| `qr_sharing` | QR sharing |
| `ai_review_assist` | AI review assist |
| `business_ai` | Business AI tools |
| `analytics` | Analytics |
| `account_collaborators` | Manage account collaborators |
| `multi_account_team_management` | Manage multiple accounts / teams |
| `multi_profile_type_profiles` | Multi-profile / multi-type profiles |
| `call_masking` | Call masking |
| `whatsapp_masking` | WhatsApp masking |
| `theme_library` | Wide range of themes |
| `advanced_creator_analytics` | Advanced analytics for creators |

## Hubs

| Hub | Features | Child Focus |
|-----|----------|-------------|
| platform | All 13 | Homepage only |
| business | 12 (no advanced_creator_analytics, adds business_ai) | Cards, professions, comparisons, Business AI |
| creator | 10 (no masking, adds creator analytics) | Creator tools, Linktree alternative |
| family_safety | 6 | Safety tags, emergency QR |
| pet | 4 | Pet ID, lost & found |
| travel | 6 | Travel QR, luggage tags |
| vehicle | 6 | Vehicle QR, parking stickers |

## Common Workflows

### Add a new keyword
1. Check if intent is already owned by an existing page in `execution_seo_master.csv`
2. If new intent → add to `raw_keyword_bank.csv` with `keep_primary`
3. Create page row in `page_master.csv` and `execution_seo_master.csv`
4. Add content task in `content_calendar.csv`

### Generate a content brief
1. Read the page's row from `page_master.csv` and `execution_seo_master.csv`
2. Read the content task from `content_calendar.csv`
3. Use `prompts/content-brief-prompt.md` with the `briefs/templates/page-brief-template.md`
4. Translate feature tokens to human labels using the table above

### Write a full blog draft
1. Pick a blog from `content_calendar.csv` (filter by `status=planned`, sort by `priority`)
2. Generate a brief first: `/profiletap-brief` with the `page_slug`
3. Generate the full draft: `/profiletap-blog-writer` with the `page_slug`
4. Review, edit, and publish
5. Update `content_calendar.csv`: `status` → `published`, `publish_date` → today

### Add a new product family
1. Add product entry to `data/products/product_catalog.json`
2. Add page row to `page_master.csv` with `page_type=product_family`, `page_group=product_catalog`
3. Add keyword family row to `execution_seo_master.csv`
4. Add content task to `content_calendar.csv`
5. Add product keywords to `raw_keyword_bank.csv` with `canonical_page_slug` pointing to the product page
6. Verify intent separation: product page owns buying intent, solution page owns use-case intent
7. Run `python scripts/validate_system.py` to check integrity

### Check system consistency
Run `python scripts/validate_system.py` to verify cross-file integrity.

### Rebuild keyword system from source
```bash
python scripts/rebuild_keyword_system.py [optional_source_path]
```

## Skills (Slash Commands)

### General SEO (reusable across projects)
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

### ProfileTap-Specific
- `/profiletap-context` — Product, features, market, competitors
- `/profiletap-architecture` — Page architecture and structure
- `/profiletap-keywords` — Keyword system management
- `/profiletap-brief` — Content brief generation
- `/profiletap-backlinks` — Backlink operations
- `/profiletap-measurement` — Performance measurement
- `/profiletap-blog-writer` — Full blog drafts with ProfileTap voice and context

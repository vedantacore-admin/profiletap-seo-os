# [PROJECT_NAME] — SEO OS Project

> **How to use:** Open Claude Code from this directory (`projects/[project-folder]/`) to auto-load both the generic root CLAUDE.md (generic skills, system navigation) and this file (project-specific rules, data schemas, workflows).

## What This Is

SEO operating system for **[PROJECT_NAME]** — [one-line description of the product/brand]. Manages the full keyword → page → content → backlink pipeline.

## File Map

```
data/
  keywords/raw_keyword_bank.csv       # Keyword research inventory
  keywords/execution_seo_master.csv   # Canonical page-to-keyword families (one row per page)
  pages/page_master.csv               # Master page inventory with architecture
  content/content_calendar.csv        # Content production queue
  backlinks/backlink_targets.csv      # Link prospect list
  backlinks/outreach_tracker.csv      # Outreach execution status
  tracking/rank_tracker.csv           # Rank tracking data
  tracking/monthly_metrics.csv        # Monthly metrics rollup
  products/product_catalog.json       # Product catalog (if applicable)

docs/
  02-seo-strategy.md                  # Market strategy, launch architecture, execution phases
  04-internal-linking-strategy.md     # Cross-linking matrix, anchor text rules
  05-measurement-plan.md              # KPIs, tools, reporting cadence
  06-competitor-serp-analysis.md      # SERP analysis workflow

prompts/
  content-brief-prompt.md             # Brief generation rules for Claude
  competitor-analysis-prompt.md       # SERP competitor analysis
  blog-cluster-expansion-prompt.md    # Blog cluster plans per hub
  schema-markup-prompt.md             # JSON-LD generation

briefs/templates/
  page-brief-template.md              # Standard brief structure

scripts/
  validate_system.py                  # Cross-file integrity checks
  rebuild_keyword_system.py           # Rebuild keyword CSVs from source exports

skills/
  [project]-context.md                # Product, features, market, competitors
  [project]-brief.md                  # Content brief generation
  [project]-blog-writer.md            # Full blog drafts with project voice

content/
  pages/                              # Landing and hub pages
  blogs/                              # Blog posts organised by hub/segment
  products/                           # Product pages (if applicable)
```

## CSV Schemas (Quick Reference)

These schemas are universal across all SEO OS projects. Column definitions are fixed — only the data changes per project.

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
3. **[Add project-specific priority rule, e.g. market focus]**
4. **Comparisons, use cases, and blogs support commercial pages** — never cannibalize
5. **Features embedded into pages via feature_set** — no standalone feature pages unless keyword data proves distinct intent
6. **[Add any additional project-specific rules]**

## Canonical Features

Define the feature tokens for this project. These are used in `feature_set` columns across all CSVs.

| Token | Human Label |
|-------|-------------|
| (fill in) | (fill in) |

## Hubs / Segments

Define the content hubs or audience segments for this project.

| Hub | Features | Child Focus |
|-----|----------|-------------|
| (fill in) | (fill in) | (fill in) |

## Common Workflows

### Add a new keyword
1. Check if intent is already owned by an existing page in `data/keywords/execution_seo_master.csv`
2. If new intent → add to `data/keywords/raw_keyword_bank.csv` with `keep_primary`
3. Create page row in `data/pages/page_master.csv` and `data/keywords/execution_seo_master.csv`
4. Add content task in `data/content/content_calendar.csv`

### Generate a content brief
1. Read the page's row from `data/pages/page_master.csv` and `data/keywords/execution_seo_master.csv`
2. Read the content task from `data/content/content_calendar.csv`
3. Use `prompts/content-brief-prompt.md` with the `briefs/templates/page-brief-template.md`
4. Translate feature tokens to human labels using the table above

### Write a full blog draft
1. Pick a blog from `data/content/content_calendar.csv` (filter by `status=planned`, sort by `priority`)
2. Generate a brief first using the project brief skill
3. Generate the full draft using the project blog-writer skill
4. Review, edit, and publish
5. Update `data/content/content_calendar.csv`: `status` → `published`, `publish_date` → today

### Check system consistency
```bash
python scripts/validate_system.py
```

## Skills (Slash Commands)

### Project-Specific
- `/[project]-context` — Product, features, market, competitors
- `/[project]-brief` — Content brief generation
- `/[project]-blog-writer` — Full blog drafts with project voice

### Generic SEO Skills
See root CLAUDE.md — 11 general-seo skills are available from the root and load automatically when both CLAUDE.md files are active.

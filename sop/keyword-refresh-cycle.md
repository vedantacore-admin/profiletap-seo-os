# SOP: Keyword Refresh Cycle

## Purpose

Maintain accurate keyword data, validate priorities, and detect new opportunities through regular keyword system refreshes.

---

## 1. Monthly Refresh (P1 Keywords)

**When:** First week of each month
**Time:** 1-2 hours

### Steps

1. Open Ubersuggest (or chosen keyword tool)
2. For each P1 keyword in `execution_seo_master.csv`:
   - Look up current search volume, keyword difficulty (KD), and CPC
   - Update `ubersuggest_volume`, `ubersuggest_kd`, `ubersuggest_cpc` in `raw_keyword_bank.csv`
   - Update `ubersuggest_last_checked` to today's date
3. Compare new volume/KD data against current priority:
   - If a P1 keyword has dropped to < 100 monthly volume → flag for review
   - If a P2/P3 keyword has risen to > 500 monthly volume with reasonable KD → flag for promotion
4. Document any priority changes in `keyword_family_notes` in `execution_seo_master.csv`

### Output

- Updated `raw_keyword_bank.csv` with fresh metrics for P1 keywords
- List of flagged keywords (volume drops or opportunities)

---

## 2. Quarterly Full Refresh

**When:** First week of Q1, Q2, Q3, Q4
**Time:** 4-6 hours

### Steps

1. **Refresh all keyword data** (P1, P2, P3):
   - Update Ubersuggest metrics for ALL rows in `raw_keyword_bank.csv`
   - Update `ubersuggest_last_checked` dates

2. **Re-validate priorities**:
   - Recalculate priority using: business value + search volume + keyword difficulty
   - Any P1 keyword with volume < 50 and no ranking traction → demote to P2 or hold
   - Any P2 keyword with volume > 300 and KD < 40 → promote to P1
   - Update `priority` in `execution_seo_master.csv`

3. **Detect new opportunities**:
   - Check Search Console "Queries" report for keywords the site is appearing for but doesn't target
   - Check competitor keyword tools for new keywords competitors rank for
   - For each new keyword:
     a. Does it fit an existing page? → Add as secondary keyword
     b. Does it need a new page? → Run anti-cannibalization check (see `sop/page-mapping-process.md`)
     c. Is it irrelevant? → Skip

4. **Validate `needs_validation` pages**:
   - Review any pages with `status=needs_validation` in `execution_seo_master.csv`
   - If keyword data now supports the page → update to `planned`
   - If keyword data does NOT support → hold or remove from execution_master

5. **Check for cannibalization**:
   - Search Console: Are multiple pages from our site appearing for the same query?
   - If yes → consolidate or differentiate (see `sop/page-mapping-process.md`)

6. **Run system validation**:
   - Execute `python scripts/validate_system.py`
   - Fix any cross-file inconsistencies

### Output

- Fully updated `raw_keyword_bank.csv` and `execution_seo_master.csv`
- Priority changes documented
- New keyword opportunities logged
- Cannibalization issues resolved
- Validation script passes clean

---

## 3. Triggered Refresh

### Trigger: Ranking Drop > 5 Positions on P1 Keyword

**When:** Detected via rank tracker or Search Console
**Time:** 30-60 minutes

1. Check if the drop is widespread (algorithm update) or isolated (page-specific)
2. If isolated:
   - Check for technical issues (indexing, page errors)
   - Check for content freshness (is our content outdated vs competitors?)
   - Check for new competitor content targeting the same keyword
   - If content issue → trigger content refresh (see `sop/content-refresh-triggers.md`)
   - If technical issue → fix immediately
3. If widespread:
   - Document the algorithm update
   - Wait 1-2 weeks for volatility to settle
   - Then assess impact and adjust strategy

### Trigger: New Competitor Entering Market

**When:** Discovered via monitoring
**Time:** 2-3 hours

1. Identify which keywords the new competitor targets
2. Check overlap with our keyword set
3. If significant overlap → add comparison page to pipeline (if none exists)
4. Assess their content quality and backlink profile
5. Update competitor landscape in `docs/02-seo-strategy.md`

---

## 4. Keyword Data Hygiene Rules

| Rule | Check Frequency |
|------|:---:|
| Every `raw_keyword_bank.csv` row has `canonical_page_slug` | Monthly |
| Every `keep_primary` keyword maps to exactly one page | Monthly |
| No orphan keywords (mapped to non-existent page slugs) | Quarterly |
| All `ubersuggest_last_checked` dates < 90 days old for P1 keywords | Monthly |
| All `ubersuggest_last_checked` dates < 180 days old for all keywords | Quarterly |
| No duplicate `primary_keyword` values in `execution_seo_master.csv` | Every edit |

---

## 5. Rebuild Script Usage

When keyword data needs a full rebuild from source exports:

```bash
python scripts/rebuild_keyword_system.py [path_to_source_csv_or_xlsx]
```

- Default source: `~/Downloads/SEO Master Sheet - ProfileTap - SEO Master Sheet_temp.csv`
- Generates fresh `raw_keyword_bank.csv` and `execution_seo_master.csv`
- **Always review the output before committing** — check for unexpected changes
- Run `python scripts/validate_system.py` after rebuild to verify integrity

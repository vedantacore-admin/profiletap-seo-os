# Content Refresh Strategy — General SEO Skill

> Reusable content refresh methodology for identifying, prioritizing, and executing content updates.

---

## 1. Why Content Refresh Matters

Content decay is real: pages that once ranked well lose positions over time due to freshness signals, competitor updates, algorithm changes, and evolving search intent. Refreshing existing content is often 3-5x more efficient than creating new content for the same keyword.

---

## 2. Refresh Trigger Criteria

### Automatic Triggers (act within 2 weeks)

| Trigger | Detection Method | Threshold |
|---------|-----------------|-----------|
| Ranking drop | Rank tracker / Search Console | Drop > 5 positions for target keyword |
| Traffic decline | GA4 organic landing page report | > 20% decline MoM for 2+ consecutive months |
| Impression decline | Search Console Performance | > 30% decline in impressions MoM |
| CTR decline | Search Console Performance | CTR drops below page-type average |

### Scheduled Triggers (periodic review)

| Trigger | Frequency | Action |
|---------|-----------|--------|
| Content age > 6 months | Monthly audit | Review for freshness, accuracy, completeness |
| Content age > 12 months | Quarterly audit | Full refresh evaluation |
| Year change | January | Update all "YYYY" references, statistics, examples |
| Algorithm update | When announced | Review affected pages within 1 week |

### Competitive Triggers (monitor continuously)

| Trigger | Detection | Action |
|---------|-----------|--------|
| Competitor publishes stronger content | SERP monitoring | Assess gap, plan refresh within 2 weeks |
| Competitor gains featured snippet | SERP monitoring | Optimize content structure for snippet capture |
| New SERP features appear | SERP monitoring | Add relevant schema, restructure content |
| SERP intent shifts | Top results change type | Realign content format to match new intent |

---

## 3. Content Audit Methodology

### Step 1: Inventory All Content

Pull a complete list of indexed pages with:
- URL
- Primary keyword
- Current ranking
- Organic traffic (last 90 days)
- Organic traffic (prior 90 days)
- Publication date
- Last modified date
- Word count
- Backlinks pointing to page

### Step 2: Score Each Page

| Factor | Weight | Score (1-5) |
|--------|:---:|:---:|
| Business value (conversion potential) | 30% | 5: money page, 4: high-traffic hub, 3: support content, 2: low-value, 1: irrelevant |
| Performance trend | 25% | 5: growing, 4: stable at target, 3: stable below target, 2: declining, 1: crashed |
| Refresh effort required | 20% | 5: minor tweaks, 4: section updates, 3: significant rewrite, 2: major overhaul, 1: full rebuild |
| Competitive gap | 15% | 5: no gap, 4: minor gaps, 3: moderate gaps, 2: significant gaps, 1: completely outclassed |
| Content age | 10% | 5: < 3 months, 4: 3-6 months, 3: 6-12 months, 2: 12-18 months, 1: 18+ months |

**Prioritize pages with:** High business value + declining performance + low effort = highest ROI refreshes.

### Step 3: Categorize by Action

| Category | Criteria | Action |
|----------|----------|--------|
| Optimize | Ranking 4-20, minor gaps | Minor optimization (title, meta, headers, internal links) |
| Expand | Ranking 10-30, content gaps identified | Add sections, update data, improve depth |
| Rewrite | Ranking 20+, significant gaps, outdated angle | Full content rewrite with new structure |
| Consolidate | Multiple pages targeting similar keywords, none ranking well | Merge into one comprehensive page, redirect others |
| Prune | No traffic, no rankings, no backlinks, no business value | Noindex or redirect to relevant page |
| Keep | Ranking well, traffic stable, content fresh | No action needed — monitor |

---

## 4. Update Types (Detail)

### 4.1 Minor Optimization

**When:** Page ranks 4-20, no major content gaps, just needs tuning.

Checklist:
- [ ] Improve title tag (add power words, ensure keyword, optimize for CTR)
- [ ] Rewrite meta description (add CTA, current year if applicable)
- [ ] Check H1 alignment with target keyword
- [ ] Add 2-3 internal links from high-authority pages
- [ ] Add/update FAQ section matching current PAA questions
- [ ] Update any outdated statistics or dates
- [ ] Add/improve schema markup
- [ ] Optimize images (alt text, compression, WebP format)
- [ ] Fix any broken internal or external links

**Expected timeline:** 1-2 hours per page
**Expected impact:** +3-10 positions within 2-4 weeks

### 4.2 Content Expansion

**When:** Page has foundation but competitors cover more ground.

Checklist:
- [ ] Run SERP analysis for target keyword (see `/serp-analysis` skill)
- [ ] Identify content gaps vs top 3 ranking pages
- [ ] Add missing subtopics as new H2/H3 sections
- [ ] Add comparison table (if competitors have one)
- [ ] Add step-by-step instructions (if "how to" intent)
- [ ] Add original data, examples, or case studies
- [ ] Update all statistics to current year
- [ ] Add/expand FAQ section (5-8 questions)
- [ ] Improve internal linking (add 3-5 contextual links)
- [ ] Add supporting media (images, diagrams, videos)
- [ ] Update schema markup for new content sections

**Expected timeline:** 3-5 hours per page
**Expected impact:** +5-15 positions within 4-8 weeks

### 4.3 Major Rewrite

**When:** Page structure/angle no longer matches search intent, or fundamentally outclassed by competitors.

Process:
1. Archive the current content (for reference)
2. Re-analyze the keyword's SERP — intent may have shifted
3. Create a new content brief as if writing from scratch
4. Write new content with updated structure, angle, and depth
5. Preserve the same URL (do NOT change the URL)
6. Preserve any good backlinks by keeping relevant content elements
7. Update all internal links pointing to this page (anchor text may need updating)
8. Resubmit URL for indexing via Search Console

**Expected timeline:** 8-12 hours per page
**Expected impact:** +10-30 positions within 4-12 weeks (larger variance)

### 4.4 Content Consolidation

**When:** Multiple pages compete for the same keyword (cannibalization), none ranking well.

Process:
1. Identify all pages targeting similar keywords
2. Choose the strongest page as the consolidation target (most backlinks, best ranking, most traffic)
3. Merge the best content from all pages into the target page
4. 301 redirect all other pages to the target page
5. Update internal links to point to the target page
6. Monitor rankings for 4-6 weeks

**Expected timeline:** 4-6 hours
**Expected impact:** Often dramatic — the consolidated page gets all the link equity and stops competing with itself

### 4.5 Content Pruning

**When:** Page has zero traffic, zero rankings, zero backlinks, and no business value.

Decision framework:
- If the page has backlinks → redirect to the most relevant page (preserve link equity)
- If the page has no backlinks but targets a valid keyword → refresh instead of prune
- If the page has no backlinks AND targets an irrelevant/low-value keyword → noindex or redirect
- **Never delete a URL that has external backlinks without redirecting**

---

## 5. Before/After Measurement

### Pre-Refresh Snapshot (capture before making changes)

| Metric | Source | Timeframe |
|--------|--------|-----------|
| Keyword rankings | Search Console / rank tracker | Current positions |
| Organic traffic | GA4 | Last 30, 60, 90 days |
| Impressions | Search Console | Last 28 days |
| CTR | Search Console | Last 28 days |
| Conversions | GA4 | Last 30 days |
| Word count | Screaming Frog or manual | Current |
| Backlinks | Ahrefs / Search Console | Current count |
| Core Web Vitals | PageSpeed Insights | Current scores |

### Post-Refresh Tracking

| Timeframe | What to Check |
|-----------|---------------|
| +1 week | Has Google recrawled the page? (check cache date) |
| +2 weeks | Any initial ranking movement? |
| +4 weeks | Meaningful ranking changes? Traffic trend? |
| +8 weeks | Stabilized rankings? Compare vs baseline |
| +12 weeks | Full assessment — did the refresh achieve its goal? |

---

## 6. Content Decay Detection

### Early Warning System

Set up automated alerts for:
- Any P1 keyword dropping 3+ positions WoW
- Any page losing > 15% organic traffic MoM
- Any page's impressions dropping > 20% MoM

### Monthly Decay Scan

1. Export all organic landing pages from GA4 (past 90 days vs prior 90 days)
2. Sort by traffic change (largest decline first)
3. Cross-reference declining pages with ranking data
4. For each declining page, check: is this seasonal? competitive? technical? content decay?
5. Add confirmed decay pages to refresh queue

---

## 7. Seasonal Content Calendar

| Month | Refresh Focus |
|-------|--------------|
| January | Update all year references (YYYY), annual statistics, "best of" lists |
| April | Q1 performance review — refresh underperformers |
| July | Mid-year content audit — identify decay, plan H2 refreshes |
| October | Prep for holiday/year-end traffic — refresh high-value commercial pages |
| Ongoing | Monitor SERP changes, competitor updates, algorithm updates |

---

## 8. Output Format: Refresh Priority List

```markdown
## Content Refresh Queue — [Date]

### Priority 1 (This Week)
| Page | Current Pos | Traffic Trend | Action Type | Est. Effort |
|------|:---:|-----------|-------------|:---:|
| /page-1 | 15 → 23 | -35% MoM | Expand | 4 hrs |

### Priority 2 (This Month)
| Page | Current Pos | Traffic Trend | Action Type | Est. Effort |
|------|:---:|-----------|-------------|:---:|
| /page-2 | 8 → 12 | -15% MoM | Optimize | 2 hrs |

### Priority 3 (Next Month)
| Page | Current Pos | Traffic Trend | Action Type | Est. Effort |
|------|:---:|-----------|-------------|:---:|
| /page-3 | 18 (stable) | Flat | Expand | 3 hrs |

### Consolidation Candidates
| Target Page | Pages to Merge | Combined Backlinks |
|------------|---------------|:---:|
| /target | /page-a, /page-b | 12 |

### Prune Candidates
| Page | Traffic (90d) | Backlinks | Action |
|------|:---:|:---:|--------|
| /old-page | 0 | 0 | Noindex |
```

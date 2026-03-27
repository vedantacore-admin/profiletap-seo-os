# SOP: Content Refresh Triggers

## Purpose

Define when and how to trigger content refreshes for published ProfileTap pages, ensuring pages stay competitive and accurate.

---

## 1. Automatic Triggers

| Trigger | Threshold | Detection | Response Time |
|---------|-----------|-----------|:---:|
| Ranking drop | > 5 positions for primary keyword | Rank tracker / Search Console weekly check | 2 weeks |
| Traffic decline | > 20% organic MoM for 2 consecutive months | GA4 monthly report | 2 weeks |
| Impression decline | > 30% MoM in Search Console | Search Console monthly report | 2 weeks |
| CTR decline | Below page-type average for 2 consecutive months | Search Console | 1 month |
| Content age | > 6 months since publish/last update | `last_updated` field in `page_master.csv` | Review within 1 month |
| Year change | January each year | Calendar | January |

---

## 2. Competitive Triggers

| Trigger | Detection | Response Time |
|---------|-----------|:---:|
| Competitor publishes stronger content for our keyword | SERP monitoring (monthly) | 2 weeks |
| Competitor gains featured snippet we held | SERP monitoring | 1 week |
| New SERP features appear for our keyword | SERP monitoring | 2 weeks |
| SERP intent shifts (top results change format) | Quarterly SERP analysis | 1 month |

---

## 3. Refresh Decision Matrix

When a trigger fires, determine the refresh type:

| Situation | Refresh Type | Effort |
|-----------|-------------|:---:|
| Title/meta could be better, content is fine | Minor optimization | 1-2 hrs |
| Competitors cover subtopics we miss | Content expansion | 3-5 hrs |
| Content structure/angle no longer matches SERP intent | Major rewrite | 8-12 hrs |
| Multiple pages competing for same keyword | Consolidation | 4-6 hrs |
| Page has zero value, no traffic, no backlinks | Prune (noindex/redirect) | 30 min |
| Statistics/dates are outdated | Data update | 1-2 hrs |
| FAQ/PAA section is stale or missing | FAQ refresh | 1-2 hrs |

---

## 4. Refresh Workflow

### Step 1: Diagnose

- Check Search Console for the page: impressions, clicks, CTR, average position trends
- Check GA4: organic traffic trend, bounce rate, time on page
- Run SERP analysis for the primary keyword (use `/serp-analysis` skill)
- Compare our content against current top 3 results

### Step 2: Plan the Refresh

- Determine refresh type from the decision matrix above
- If content expansion or rewrite: create a brief update using `/profiletap-brief` skill
- Document planned changes

### Step 3: Execute

- Make the changes following the refresh type guidelines
- Run through the content QA checklist from `sop/content-review-process.md`
- Update `last_updated` in `page_master.csv`
- Update `refresh_date` in `content_calendar.csv`

### Step 4: Measure

- Capture post-refresh snapshot: ranking, traffic, impressions, CTR
- Compare at +7, +14, +30, +60 days
- Document results

---

## 5. Refresh Priority Scoring

When multiple pages need refresh, prioritize:

| Factor | Weight |
|--------|:---:|
| Business value (P1 > P2 > P3 keyword) | 35% |
| Severity of decline (larger drop = higher priority) | 25% |
| Effort required (lower effort = higher priority for quick wins) | 20% |
| Competitive pressure (competitor just published = urgent) | 20% |

---

## 6. Scheduled Refresh Calendar

| Month | Scheduled Action |
|-------|-----------------|
| Every month | Check P1 page metrics, flag any triggers |
| January | Update all year references, statistics across all pages |
| April | Quarterly content audit — flag underperformers |
| July | Mid-year full audit — plan H2 refreshes |
| October | Pre-holiday refresh — optimize high-value commercial pages |

---

## 7. Status Tracking

When a page enters refresh:

1. Update `status` in `page_master.csv` to `refresh_needed`
2. Add refresh task to content calendar or tracking system
3. After refresh complete: update `status` back to `published`, set new `last_updated`
4. Set `next_refresh` to 6 months from now

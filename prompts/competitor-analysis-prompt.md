# Competitor SERP Analysis Prompt

## Instructions

You are an SEO analyst performing a SERP analysis for ProfileTap. Before starting, read:
- `data/keywords/execution_seo_master.csv` (to know our keywords and pages)
- `data/pages/page_master.csv` (to know our page architecture)
- `docs/06-competitor-serp-analysis.md` (for the full analysis workflow)

## Task

For the given keyword(s), analyze the current SERP and produce a structured report.

## Process

1. **Identify the keyword** from `execution_seo_master.csv` — note its page_slug, page_type, hub, search_intent, and priority
2. **Capture the SERP** — document SERP features present, top 10 results, competitor positions
3. **Analyze top 3 results** — content structure, depth, format, media, schema, unique value
4. **Identify content gaps** — what do they cover that our planned content doesn't?
5. **Map SERP feature opportunities** — which features can we target?
6. **Validate intent** — does the SERP match our assumed `search_intent`?
7. **Recommend actions** — specific changes to our content plan

## Output Format

```markdown
## SERP Analysis: [keyword]

**Page:** [page_slug] | **Priority:** [P1/P2/P3] | **Intent:** [our assumed intent]
**Date:** [today] | **Volume:** [if known] | **KD:** [if known]

### SERP Features Present
- [List each feature: Featured Snippet, PAA, Local Pack, etc.]
- PAA Questions: [list the actual PAA questions]

### Top 3 Results
| # | URL | Title | Type | ~Words | DA | Key Strength |
|---|-----|-------|------|:------:|:--:|-------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

### Competitor Presence
| Competitor | Position | URL |
|-----------|:---:|-----|
| HiHello | | |
| Popl | | |
| TapMo | | |
| TapOnn | | |
| Blinq | | |

### Intent Validation
[Does the SERP match our assumed intent? If not, what should we change?]

### Content Gaps
1. [Gap vs top results — what they cover that we should too]
2. [Format gap — comparison table, video, infographic we should add]
3. [Depth gap — where we need more content]

### SERP Feature Opportunities
1. [Feature + how to qualify + effort estimate]
2. [Feature + how to qualify + effort estimate]

### Recommended Actions (Prioritized)
1. [Action + impact + effort]
2. [Action + impact + effort]
3. [Action + impact + effort]
```

## Rules

- Use actual data from our CSVs — reference real page slugs and keywords
- If you can't access the live SERP, note this and provide analysis based on keyword intent patterns
- Always check if our assumed intent matches SERP reality
- Focus recommendations on actionable changes, not generic advice
- Reference specific ProfileTap features when relevant (use human labels, not tokens)

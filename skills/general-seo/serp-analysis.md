# SERP Analysis — General SEO Skill

> Reusable SERP analysis and competitive intelligence methodology for any project.

---

## 1. Purpose

SERP analysis validates search intent assumptions, identifies content gaps, maps feature opportunities, and informs content strategy by studying what Google actually rewards for target keywords.

---

## 2. SERP Feature Identification

### Feature Types and What They Signal

| SERP Feature | Signal | Opportunity |
|-------------|--------|-------------|
| Featured Snippet (position 0) | Google wants a direct, concise answer | Structure content with clear Q&A, definitions, or step lists |
| People Also Ask (PAA) | Related questions users have | Add FAQ section matching PAA questions |
| Local Pack (map results) | Location-specific intent | Optimize Google Business Profile, add local schema |
| Image Pack | Visual/product intent | Optimize images with descriptive alt text, file names |
| Video Carousel | Tutorial/demo intent | Create YouTube video with optimized metadata |
| Knowledge Panel | Entity/brand query | Claim Google Knowledge Panel, add Organization schema |
| Site Links | Brand authority signal | Clean site structure, breadcrumbs, clear navigation |
| Top Stories | News/trending intent | Publish timely content, use Article schema |
| Shopping Results | Purchase intent | Product schema, Google Merchant Center |
| Reviews/Stars | Review/comparison intent | Aggregate rating schema, review content |

### How to Qualify for Each Feature

#### Featured Snippets
- **Paragraph snippet:** Write a 40-60 word direct answer immediately after the question as H2
- **List snippet:** Use ordered/unordered list with 5-8 items under a clear heading
- **Table snippet:** Use HTML table with clear headers
- **Video snippet:** YouTube video with timestamp chapters
- **Prerequisite:** Must rank in top 10 already (snippets pull from page 1 results)

#### People Also Ask
- Identify PAA questions for your target keyword
- Add each as an H2 or H3 in your content
- Follow with a concise 2-3 sentence answer
- Then expand with more detail
- Structure as FAQ schema for double opportunity

#### Local Pack
- Verified Google Business Profile with complete information
- NAP consistency across all citations
- LocalBusiness schema on your site
- Reviews (quantity and recency)
- Local content on your site

---

## 3. SERP Analysis Workflow

### Step 1: Keyword Selection

Choose keywords to analyze:
- All P1 (highest priority) keywords
- Keywords you're actively creating content for
- Keywords where you've seen ranking changes
- New keyword opportunities you're evaluating

### Step 2: Capture the SERP

For each keyword, record in a structured format:

```
Keyword: [exact query]
Date: [YYYY-MM-DD]
Location: [geo target]
Device: [desktop / mobile]

SERP Features Present:
- [ ] Featured Snippet (type: paragraph/list/table/video)
- [ ] People Also Ask (list questions)
- [ ] Local Pack
- [ ] Image Pack
- [ ] Video Carousel
- [ ] Knowledge Panel
- [ ] Site Links
- [ ] Shopping Results
- [ ] Ads (count: top ___, bottom ___)

Top 10 Results:
| Pos | URL | Title | Page Type | Est. Word Count | Domain DA |
|-----|-----|-------|-----------|----------------|-----------|
| 1   |     |       |           |                |           |
| ... |     |       |           |                |           |
| 10  |     |       |           |                |           |

Our Position: [X / Not ranking]
Competitor Positions: [list]
```

### Step 3: Analyze Content Patterns

For the top 3 ranking pages, deep-dive:

| Element | What to Record |
|---------|---------------|
| URL structure | Depth, keyword inclusion, format |
| Title tag | Formula used, keyword placement, length |
| H1 | Keyword use, differentiation from title |
| Header hierarchy | All H2/H3 headings — reveals topic coverage |
| Content structure | Intro → sections → conclusion? Comparison table? FAQ? |
| Content length | Word count (proxy for depth) |
| Content format | Long-form guide, listicle, comparison, tool, calculator |
| Media | Images (count, types), videos, infographics, interactive elements |
| Schema markup | Types used (check via Rich Results Test) |
| Internal links | Count, anchor text patterns |
| External links | Count, types of sources cited |
| CTAs | Type, placement, frequency |
| Freshness signals | Published date, updated date, current year references |
| E-E-A-T signals | Author bios, credentials, citations, methodology |

### Step 4: Intent Validation

Use SERP composition to validate or adjust your assumed search intent:

| SERP Composition | Validated Intent | Content Implication |
|-----------------|-----------------|-------------------|
| All product/category pages | Transactional | Create a commercial landing page |
| All blog posts / guides | Informational | Create educational content (blog) |
| Mix of product + blog | Mixed / commercial investigation | Create a commercial page with educational depth |
| Comparison tables dominate | Comparison | Include comparison table, feature matrix |
| Video results dominate | Visual / tutorial | Create video content |
| Local pack appears | Local | Optimize for local SEO |
| PAA questions are "how to" | Procedural / educational | Include step-by-step instructions |
| PAA questions are "best" / "vs" | Commercial investigation | Include comparisons, recommendations |

**If SERP signals contradict your assumed intent, update your content plan before writing.**

### Step 5: Content Gap Analysis

Compare your planned content against what's ranking:

| Gap Type | How to Identify | Action |
|----------|----------------|--------|
| Topic gap | Competitors cover subtopics you haven't planned | Add missing subtopics to your outline |
| Depth gap | Competitors go deeper (longer content, more examples) | Expand your content scope |
| Format gap | Competitors use comparison tables, you don't | Add the winning format |
| Media gap | Competitors have video/images, you don't | Plan media creation |
| Schema gap | Competitors have rich results, you don't | Add appropriate schema |
| Freshness gap | Competitors have current-year data, you don't | Include updated statistics |
| Authority gap | Competitors cite sources/experts, you don't | Add citations, expert quotes |
| UX gap | Competitors have better page experience | Improve design, speed, mobile experience |

### Step 6: Opportunity Scoring

Score each SERP feature opportunity:

| Factor | Weight | Score (1-5) |
|--------|:---:|:---:|
| Feature present in SERP | 25% | 5 if yes, 1 if no |
| Current ranking (closer = more attainable) | 25% | 5 if top 5, 3 if top 10, 1 if not ranking |
| Content readiness (do we have content that could qualify?) | 25% | 5 if ready, 3 if needs updates, 1 if needs creation |
| Business value (traffic + conversion potential) | 25% | 5 if high value keyword, 1 if low value |

Prioritize opportunities with score > 3.5.

---

## 4. Competitive Position Analysis

### Competitor Visibility Matrix

For your keyword set, map competitor visibility:

```
| Keyword | Our Pos | Comp A | Comp B | Comp C | Gap |
|---------|:---:|:---:|:---:|:---:|-----|
| [kw1]   | 12  | 3   | 7   | -   | Need to improve content depth |
| [kw2]   | -   | 1   | 2   | 5   | Need to create page |
| [kw3]   | 5   | 8   | -   | 4   | Close to winning |
```

### Competitor Content Audit

For each competitor page that outranks you:

1. **What do they cover that you don't?** → Content gaps to fill
2. **What format advantages do they have?** → Structure improvements
3. **What authority signals do they have?** → E-E-A-T improvements
4. **What backlinks do they have that you don't?** → Link building targets
5. **What schema do they use?** → Schema additions
6. **What's their page experience like?** → UX improvements

### Backlink Gap Analysis

1. Pull referring domains for top 3 competitors for each keyword
2. Filter to DA > 30
3. Identify domains linking to competitors but not you
4. Score by relevance and authority
5. Add to outreach pipeline

---

## 5. Click-Through Rate Estimation

### Average CTR by Position (Organic)

| Position | Desktop CTR | Mobile CTR |
|:---:|:---:|:---:|
| 1 | 28-32% | 24-28% |
| 2 | 15-18% | 13-16% |
| 3 | 10-12% | 9-11% |
| 4 | 7-8% | 6-7% |
| 5 | 5-6% | 4-5% |
| 6-10 | 2-4% | 2-3% |

### CTR Modifiers

| Factor | Impact |
|--------|--------|
| Featured snippet captured | +20-35% CTR for that position |
| Rich results (stars, FAQ, etc.) | +10-20% CTR |
| Brand recognition | +5-15% CTR |
| Compelling title tag | +5-10% CTR |
| Many ads above organic | -10-20% CTR for all organic |
| Local pack above organic | -5-10% CTR for non-local organic |

### Traffic Estimation Formula

```
Estimated monthly traffic = Search volume × CTR for your position × Seasonality factor
```

---

## 6. SERP Volatility Assessment

### What Volatility Means

| Volatility Level | Description | Implication |
|:---:|------------|-------------|
| Low (< 5% change) | Same pages rank consistently | Established intent, hard to displace incumbents |
| Medium (5-15%) | Some movement, mostly top 10 shuffling | Opportunity to break in with strong content |
| High (> 15%) | Frequent ranking changes, new pages appearing | Google hasn't settled on best result — opportunity |

### How to Assess

1. Check the same keyword weekly for 4 weeks
2. Note which URLs appear and their positions
3. Calculate position changes for each URL
4. High movement = Google is still testing → opportunity to win with fresh, high-quality content

---

## 7. Output Formats

### Per-Keyword Analysis Report

```markdown
## SERP Analysis: [keyword]

**Search Volume:** [monthly]  |  **KD:** [score]  |  **Our Position:** [X]
**Date:** [YYYY-MM-DD]  |  **Location:** [geo]

### SERP Features
[List features present with notes]

### Top 3 Analysis
[URL, title, word count, format, key strengths for each]

### Content Gaps
[Bullet list of gaps between our content and top results]

### Feature Opportunities
[Ranked list of SERP feature opportunities with effort/impact]

### Recommended Actions
[Prioritized list of specific actions]
```

### Keyword Set Summary

```markdown
## SERP Intelligence Summary — [Date Range]

### Ranking Distribution
- Top 3: [X] keywords
- Top 10: [X] keywords
- Page 2: [X] keywords
- Not ranking: [X] keywords

### SERP Feature Presence
- Featured snippets available: [X] keywords (we hold: [Y])
- PAA present: [X] keywords
- Local pack: [X] keywords

### Key Competitor Positions
[Table of competitor visibility across keyword set]

### Top Opportunities (by impact)
1. [Opportunity + recommended action]
2. [Opportunity + recommended action]
3. [Opportunity + recommended action]

### Content Gaps to Address
[Prioritized list]
```

---

## 8. SERP Analysis Checklist

Run for each target keyword before creating content:

- [ ] SERP features identified and documented
- [ ] Top 3 results analyzed (structure, depth, format, media)
- [ ] Search intent validated against SERP composition
- [ ] Content gaps identified
- [ ] Featured snippet opportunity assessed
- [ ] PAA questions captured for FAQ section
- [ ] Competitor positions mapped
- [ ] CTR and traffic potential estimated
- [ ] Content plan adjusted based on findings
- [ ] Schema requirements identified from SERP features

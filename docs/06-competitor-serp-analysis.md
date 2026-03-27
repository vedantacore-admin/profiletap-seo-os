# Competitor SERP Analysis — ProfileTap

## Purpose

Define the workflow for analyzing competitor positions in search results, identifying content gaps, mapping SERP features, and monitoring competitor moves.

---

## 1. Competitor Landscape

### Direct Competitors (Digital Business Card / Identity)

| Competitor | Market | Strengths | ProfileTap Differentiator |
|-----------|--------|-----------|--------------------------|
| HiHello | Global, some India presence | Established brand, enterprise features | India-first, multi-identity (not just business), privacy features |
| Popl | Global, weak in India | Strong NFC hardware, US-focused | India pricing, broader identity use cases |
| TapMo | India | Local presence, physical cards | Platform depth (6 hubs vs single-use) |
| TapOnn | India | NFC-first, enterprise sales | Multi-segment identity, AI review assist |
| Blinq | Global | Clean UI, easy setup | India market, multi-identity beyond business |

### Indirect Competitors (Link-in-Bio / Creator Tools)

| Competitor | Overlap | Our Angle |
|-----------|---------|-----------|
| Linktree | Creator audience, link-in-bio intent | Full identity platform vs link aggregator |
| Beacons | Creator monetization | Identity management vs monetization |
| Carrd | Simple web presence | Smart profiles vs static pages |

---

## 2. SERP Analysis Workflow

### Step 1: Keyword Selection

Select keywords for analysis from `execution_seo_master.csv`:
- All P1 keywords (priority)
- P2 keywords in upcoming publish wave
- Any keyword where ranking has dropped

### Step 2: SERP Capture

For each keyword, record:

| Field | What to Capture |
|-------|----------------|
| Keyword | The exact search query |
| Date | When the SERP was checked |
| SERP features present | Featured snippet, PAA, local pack, image pack, video, knowledge panel, site links, ads |
| Position 1-3 results | URL, title, meta description, page type, word count estimate |
| Position 4-10 results | URL, title, page type |
| Our position | Current ranking (if any) |
| Competitor positions | Which competitors appear and where |

### Step 3: Content Structure Audit

For the top 3 ranking pages, analyze:

| Element | What to Record |
|---------|---------------|
| URL structure | Path depth, keyword in URL |
| Title tag | Format, keyword placement, length |
| H1 | Keyword inclusion, format |
| Header hierarchy | H2/H3 structure, topic coverage |
| Content length | Approximate word count |
| Content format | Listicle, guide, comparison table, FAQ, video |
| Media | Images, videos, infographics, interactive elements |
| Schema markup | What structured data they use |
| Internal links | How many, anchor text patterns |
| CTAs | Type, placement, frequency |
| Unique value | What they offer that others don't |

### Step 4: Content Gap Identification

Compare our planned/published content against top-ranking content:

| Gap Type | How to Identify | Action |
|----------|----------------|--------|
| Missing topics | Competitor covers subtopics we don't | Add to content plan or expand existing page |
| Missing format | Competitor uses comparison table, we don't | Add the format to our brief |
| Missing media | Competitor has video/infographic, we don't | Plan media creation |
| Missing schema | Competitor has FAQ/HowTo schema, we don't | Add schema markup |
| Missing depth | Competitor covers topic in 3000 words, we plan 1000 | Expand content scope |
| Missing freshness | Competitor has 2026 data, we don't | Plan content refresh with current data |

### Step 5: SERP Feature Opportunity Assessment

| SERP Feature | How to Qualify | Content Requirements |
|-------------|---------------|---------------------|
| Featured Snippet | Rank top 10, answer a clear question | Concise answer paragraph (40-60 words) after the question as H2 |
| People Also Ask | Related questions visible in SERP | FAQ section with matching questions and concise answers |
| Image Pack | Visual/product queries | Optimized images with descriptive alt text and file names |
| Video Carousel | How-to or tutorial queries | YouTube video with optimized title and description |
| Site Links | Brand queries, strong site structure | Clear navigation, breadcrumbs, schema markup |
| Local Pack | Location-specific queries | Google Business Profile, local schema, NAP consistency |
| Knowledge Panel | Brand queries | Organization schema, Wikipedia/Wikidata presence, social profiles |

---

## 3. Competitor Page Structure Templates

### How to Analyze a Competitor Page

Use this template for each competitor page you analyze:

```
## Competitor Page Analysis

**URL:** [competitor URL]
**Keyword:** [target keyword]
**Position:** [current SERP position]
**Date Analyzed:** [date]

### Content Structure
- Title Tag: [exact title]
- H1: [exact H1]
- Word Count: [estimate]
- H2 Topics: [list all H2 headings]
- Content Format: [guide / listicle / comparison / etc.]

### SEO Elements
- Meta Description: [exact description]
- Schema Markup: [types found]
- Internal Links: [count and notable targets]
- External Links: [count and notable sources]
- Images: [count, alt text quality]

### Strengths
- [What they do well]

### Weaknesses
- [Where they fall short]

### Opportunities for ProfileTap
- [How we can differentiate or do better]
```

---

## 4. Competitor Monitoring Schedule

### Monthly (P1 Competitors: HiHello, Popl, TapMo, TapOnn)

- [ ] Check their rankings for our P1 keywords
- [ ] Scan for new pages published on their sites
- [ ] Note any new SERP features they've gained
- [ ] Check their backlink growth (using Ubersuggest or similar)

### Quarterly (All Competitors including Blinq, Linktree)

- [ ] Full SERP analysis for all P1 and P2 keywords
- [ ] Content gap analysis against top 3 competitors
- [ ] Backlink gap analysis (domains linking to them but not us)
- [ ] Feature comparison update (have they launched new features?)
- [ ] Pricing comparison update
- [ ] New competitor identification (any new players in the market?)

---

## 5. SERP Analysis Output Template

### Per-Keyword Report

```
## SERP Analysis: [keyword]

**Date:** [date]
**Search Volume:** [monthly volume]
**Current Position:** [our ranking]
**SERP Features:** [list features present]

### Top 3 Results
1. [URL] — [title] — [word count] — [page type]
2. [URL] — [title] — [word count] — [page type]
3. [URL] — [title] — [word count] — [page type]

### Competitor Presence
- HiHello: Position [X] / Not ranking
- Popl: Position [X] / Not ranking
- TapMo: Position [X] / Not ranking

### Content Gap vs Top Results
- [Gap 1]
- [Gap 2]

### SERP Feature Opportunities
- [Opportunity 1]
- [Opportunity 2]

### Recommended Actions
- [Action 1]
- [Action 2]
```

### Quarterly Summary Report

```
## Quarterly SERP Intelligence Summary — Q[X] [Year]

### Overall Ranking Progress
- P1 keywords in top 10: [X/Y]
- P2 keywords in top 10: [X/Y]
- New top-10 rankings this quarter: [list]
- Lost top-10 rankings: [list]

### Competitor Movement
- [Competitor]: [gained/lost] [X] positions on [keywords]
- New competitor pages: [list]

### SERP Feature Wins/Losses
- Featured snippets held: [X]
- Featured snippets lost: [X]
- PAA presence: [X keywords]

### Content Gaps Identified
- [Gap 1]: [recommended action]
- [Gap 2]: [recommended action]

### Priority Actions for Next Quarter
1. [Action]
2. [Action]
3. [Action]
```

---

## 6. Backlink Gap Analysis

### Process

1. Pull top referring domains for each P1 competitor (Ubersuggest or Ahrefs)
2. Filter for domains with DA > 30
3. Identify domains linking to competitors but NOT to ProfileTap
4. Qualify by relevance (is this domain topically relevant?)
5. Add qualified prospects to `data/backlinks/backlink_targets.csv`

### Output: Backlink Gap Prospect List

| Domain | Links to | DA | Relevance | Our Status |
|--------|---------|:---:|:---------:|-----------|
| example.com | HiHello, Popl | 55 | High | Not linked |

---

## 7. Intent Validation from SERP

Use SERP results to validate or adjust our assumed search intent:

| SERP Signal | Indicates |
|------------|-----------|
| All results are product/category pages | Transactional intent — our category page is correct |
| Mix of blog posts and product pages | Mixed intent — consider both a category page AND a blog post |
| All results are how-to guides | Informational intent — blog post is the right format |
| Featured snippet with a comparison table | Comparison intent — include a comparison table |
| Local pack appears | Local intent — consider local SEO optimization |
| PAA questions are all "how to" | Educational intent — include step-by-step content |
| Video carousel present | Video intent — consider creating video content |

If SERP signals contradict our assumed intent in `execution_seo_master.csv`, update the `search_intent` field and adjust the content plan accordingly.

# Keyword Research Methodology

> Claude Code Skill: Comprehensive keyword research framework for any website or project.
> Use this as a step-by-step reference when conducting keyword research from scratch or auditing an existing keyword set.

---

## 1. Seed Keyword Expansion

### 1.1 Starting Points
Begin with 5-15 seed keywords that describe the core offering. Expand from there using these sources:

**Competitor Mining**
- Identify 3-5 direct competitors and 2-3 indirect competitors.
- Pull their top 100 organic keywords from Ahrefs, Semrush, or Similarweb.
- Focus on keywords where competitors rank positions 1-20 — these are proven demand signals.
- Flag keywords where multiple competitors rank but you do not (immediate gaps).

**Related Terms and Synonyms**
- For each seed keyword, list 3-5 synonyms or alternate phrasings (e.g., "project management tool" vs "task management software" vs "team collaboration app").
- Use Google Autocomplete: type each seed keyword and record all suggestions.
- Use Google "Related Searches" at the bottom of the SERP.
- Use Google "People Also Ask" (PAA) boxes — each question is a keyword candidate.
- Use "Also Ranked For" reports in Ahrefs/Semrush to find semantic siblings.

**Question Modifiers**
Append these to every seed keyword and check volume:
- what is [keyword]
- how to [keyword]
- best [keyword]
- [keyword] vs [keyword]
- [keyword] for [audience]
- why [keyword]
- [keyword] examples
- [keyword] alternatives
- [keyword] pricing / cost
- [keyword] reviews

**Commercial and Transactional Modifiers**
- buy, pricing, cost, free, trial, demo, best, top, review, comparison, alternative, vs, cheap, affordable, premium, enterprise

**Audience Modifiers**
- for small business, for startups, for enterprise, for freelancers, for agencies, for beginners, for developers, for marketers

### 1.2 Expansion Tools and Data Sources
| Tool | Best For | Free/Paid |
|------|----------|-----------|
| Google Search Console | Existing impressions and clicks | Free |
| Google Keyword Planner | Volume ranges, CPC data | Free (with Ads account) |
| Ahrefs Keywords Explorer | Volume, KD, SERP analysis | Paid |
| Semrush Keyword Magic Tool | Large-scale expansion | Paid |
| Ubersuggest | Budget-friendly volume data | Freemium |
| AnswerThePublic | Question-based keywords | Freemium |
| AlsoAsked | PAA clustering | Freemium |
| Google Trends | Seasonality, trending topics | Free |
| Reddit / Quora / Forums | Real user language and pain points | Free |
| ChatGPT / Claude | Brainstorming synonyms and angles | Varies |

---

## 2. Search Intent Classification

Every keyword must be classified into one of four intent buckets. This determines content format, page type, and conversion expectations.

### 2.1 Intent Definitions

| Intent | Signal Words | User Goal | Content Format | Conversion Expectation |
|--------|-------------|-----------|----------------|----------------------|
| **Informational** | what, how, why, guide, tutorial, examples, tips | Learn something | Blog post, guide, video, infographic | Low (email capture, awareness) |
| **Navigational** | [brand name], login, pricing page, support | Find a specific page/brand | Homepage, branded landing page | Medium (brand loyalty) |
| **Commercial Investigation** | best, top, review, comparison, vs, alternatives | Evaluate options before buying | Comparison page, review, listicle | High (consideration stage) |
| **Transactional** | buy, pricing, signup, demo, free trial, discount, coupon | Complete a purchase or action | Product page, pricing page, signup flow | Highest (ready to convert) |

### 2.2 Intent Validation Process
1. Google the keyword in an incognito window.
2. Examine the top 5 organic results.
3. What page type dominates? (blog = informational, product pages = transactional, comparison posts = commercial)
4. Are there SERP features? (PAA = informational, shopping results = transactional, local pack = local intent)
5. If the SERP shows mixed intent, the keyword may serve multiple intents — pick the dominant one or create content that addresses both.

### 2.3 Mixed Intent Handling
Some keywords have genuinely mixed intent (e.g., "CRM software" could be informational or commercial). Rules:
- If 3+ of the top 5 results are the same type, classify as that type.
- If split 50/50, classify as the higher-value intent (commercial > informational).
- Create separate pages only if the keyword has sufficient volume (1,000+ monthly searches) to justify two pages targeting different intents.

---

## 3. Keyword Clustering by Intent

### 3.1 Clustering Rules
Group keywords into clusters where each cluster = one page on the site. Cluster by INTENT first, then by topic.

**Same Cluster (one page):**
- Keywords with identical SERP overlap (3+ of the same URLs in top 10).
- Singular vs plural variants ("project management tool" / "project management tools").
- Close synonyms with same intent ("email marketing software" / "email marketing platform").
- A head term and its long-tail children if the same page can satisfy both.

**Separate Clusters (different pages):**
- Keywords with different dominant intent (even if topically related).
- Keywords where the SERPs show completely different pages in the top 10.
- Keywords where combining them would create an unfocused, diluted page.
- Geo-modified vs non-geo versions if local and national SERPs differ.

### 3.2 Clustering Process
1. Export all keyword candidates into a spreadsheet.
2. Sort by search volume descending.
3. Take the highest-volume keyword — this is Cluster 1's primary keyword.
4. For each remaining keyword, check SERP overlap with Cluster 1's primary keyword.
5. If 3+ URLs overlap in the top 10, add to Cluster 1.
6. If not, start a new cluster.
7. Repeat until all keywords are assigned.
8. Name each cluster after its primary (highest volume) keyword.

---

## 4. Volume / KD / CPC Evaluation Framework

### 4.1 Metrics Definitions
| Metric | What It Tells You | Reliable Source |
|--------|-------------------|-----------------|
| **Search Volume** | Monthly search demand (usually national) | Ahrefs, Semrush, Google Keyword Planner |
| **Keyword Difficulty (KD)** | How hard it is to rank on page 1 (scale 0-100) | Ahrefs (most trusted), Semrush |
| **CPC** | What advertisers pay per click — proxy for commercial value | Google Keyword Planner |
| **Traffic Potential** | Estimated total traffic the #1 page gets (often 2-5x the primary keyword volume) | Ahrefs |
| **SERP Features** | Whether organic clicks are reduced by featured snippets, ads, etc. | Manual SERP check |

### 4.2 Volume Thresholds (General Guidance)
| Category | Monthly Volume | Notes |
|----------|---------------|-------|
| High volume | 10,000+ | Competitive, usually head terms |
| Medium volume | 1,000-10,000 | Sweet spot for most sites |
| Low volume | 100-1,000 | Long-tail, high conversion potential |
| Very low volume | <100 | Only pursue if very high business value or part of a cluster |

### 4.3 KD Interpretation
| KD Range | Meaning | Site Authority Needed |
|----------|---------|----------------------|
| 0-20 | Easy | New sites can rank with good content |
| 21-40 | Medium | Sites with some authority (DR 20-40) |
| 41-60 | Hard | Established sites (DR 40-60) with backlinks |
| 61-80 | Very hard | High-authority sites (DR 60+) with strong link profiles |
| 81-100 | Extremely hard | Only top-tier domains compete here |

---

## 5. Keyword Prioritization Matrix

Score each keyword cluster on three dimensions (1-5 scale each), then multiply for a composite score (max 125).

### 5.1 Business Value (1-5)
| Score | Criteria |
|-------|----------|
| 5 | Directly describes your product/service; transactional intent; high CPC ($5+) |
| 4 | Commercial investigation intent; searcher is evaluating solutions you offer |
| 3 | Related to your category; informational but with clear path to conversion |
| 2 | Tangentially related; top-of-funnel awareness content |
| 1 | Only loosely related; traffic with minimal conversion potential |

### 5.2 Search Demand (1-5)
| Score | Criteria |
|-------|----------|
| 5 | Cluster total volume 10,000+ monthly |
| 4 | Cluster total volume 5,000-10,000 |
| 3 | Cluster total volume 1,000-5,000 |
| 2 | Cluster total volume 300-1,000 |
| 1 | Cluster total volume <300 |

### 5.3 Competitive Feasibility (1-5)
| Score | Criteria |
|-------|----------|
| 5 | KD <20; top results are weak/thin content; few quality backlinks needed |
| 4 | KD 20-35; some weak competitors; can outperform with better content |
| 3 | KD 35-50; moderate competition; needs solid content + some links |
| 2 | KD 50-70; strong competition; needs excellent content + link building |
| 1 | KD 70+; dominated by major brands; long-term play only |

### 5.4 Priority Tiers
| Composite Score | Priority | Action |
|----------------|----------|--------|
| 75-125 | P1 — Do First | Create content within 30 days |
| 40-74 | P2 — Do Next | Create content within 60 days |
| 15-39 | P3 — Backlog | Create when P1/P2 are covered |
| 1-14 | P4 — Skip/Defer | Revisit in 6 months or drop |

---

## 6. City / Geo Modifier Handling Rules

### 6.1 When to Create Geo Pages
- The business serves specific locations (service-area business, multi-location, local delivery).
- The keyword + city combination has measurable volume (50+ monthly) OR the business has a physical presence there.
- The SERPs for "[keyword] + [city]" show local/map results or city-specific pages ranking.

### 6.2 When NOT to Create Geo Pages
- The product is purely digital/SaaS with no location relevance.
- The geo keyword has zero volume and no local SERP features.
- Creating the page would result in thin, duplicate content with only the city name swapped.

### 6.3 Geo Page Quality Rules
- Each city page must have at least 40% unique content (not just city name swapped).
- Include city-specific information: local stats, local case studies, nearby landmarks, service area details.
- Use unique title tags, meta descriptions, and H1s per city.
- Implement LocalBusiness schema with correct address data per location.
- Do not create pages for cities you do not actually serve.

### 6.4 Geo Keyword Tiers
| Tier | Example | Volume Expectation |
|------|---------|-------------------|
| State/Country | "plumber California" | Higher volume, more competitive |
| Major City | "plumber Los Angeles" | Medium-high volume |
| Suburb/Neighborhood | "plumber Santa Monica" | Lower volume, less competitive, higher conversion |
| "Near Me" | "plumber near me" | High volume, but requires local SEO signals (GMB, NAP) not just content |

---

## 7. Long-Tail vs Head Term Strategy

### 7.1 Definitions
| Type | Example | Volume | Competition | Conversion |
|------|---------|--------|-------------|------------|
| Head term | "CRM" | Very high | Very high | Low |
| Mid-tail | "CRM for small business" | Medium | Medium | Medium |
| Long-tail | "best CRM for real estate agents under $50/month" | Low | Low | High |

### 7.2 Strategy by Site Maturity
| Site Stage | DR Range | Focus |
|-----------|----------|-------|
| New (0-6 months) | 0-20 | 80% long-tail, 20% mid-tail. Build topical authority. |
| Growing (6-18 months) | 20-40 | 50% mid-tail, 30% long-tail, 20% head terms. |
| Established (18+ months) | 40+ | 40% head terms, 40% mid-tail, 20% long-tail. |

### 7.3 Content Hub Strategy
- Create a pillar page targeting the head term.
- Create cluster pages targeting mid-tail and long-tail variants.
- Interlink cluster pages to the pillar page and to each other.
- The pillar page accumulates authority from cluster pages over time.

---

## 8. Keyword Cannibalization Detection and Resolution

### 8.1 Detection Methods
1. **Google Search Console:** Export all queries. If two or more URLs appear for the same query with fluctuating positions, cannibalization is likely.
2. **Site Search:** Run `site:yourdomain.com "keyword"` in Google. If multiple pages appear, check if they compete.
3. **Rank Tracking:** If position for a keyword oscillates between two URLs week to week, they are cannibalizing.
4. **Ahrefs/Semrush:** Check "Competing Pages" report for URLs ranking for the same keywords.

### 8.2 Resolution Options
| Scenario | Solution |
|----------|----------|
| Two pages target the same keyword with similar content | Merge into one comprehensive page; 301 redirect the weaker one |
| Two pages target the same keyword but serve different intents | Differentiate the title tags, H1s, and content focus; add canonical if needed |
| A blog post competes with a product/money page | Add internal links from the blog post to the money page; de-optimize the blog post for that keyword; potentially noindex the blog post |
| Category page competes with a subcategory page | Clarify the hierarchy; make the subcategory page more specific; internal link upward |

### 8.3 Prevention Rules
- Before creating any new page, check if an existing page already targets that keyword cluster.
- Maintain a keyword-to-URL mapping document (single source of truth).
- Each keyword cluster should map to exactly one URL.

---

## 9. When to Merge vs Keep Separate Keyword Variants

### 9.1 Merge Into One Page When:
- SERP overlap is 3+ URLs in the top 10 for both variants.
- The variants are synonyms or singular/plural forms.
- Combined content would be stronger and more comprehensive than two thin pages.
- The intent is identical.

### 9.2 Keep Separate Pages When:
- SERPs show different results for each variant (different intent).
- Each variant has enough volume (500+) to justify a standalone page.
- The subtopics are distinct enough that a combined page would be unfocused.
- Different page types are needed (e.g., one is a tool/calculator, the other is a guide).

### 9.3 Decision Checklist
- [ ] Check SERP overlap (3+ shared URLs = merge).
- [ ] Check intent match (same intent = lean toward merge).
- [ ] Check combined volume benefit (does merging create a stronger page?).
- [ ] Check content depth (can one page cover both without being bloated?).
- [ ] Check existing pages (is there already a page for one variant?).

---

## 10. Output Format: Standardized Keyword Research CSV Schema

Every keyword research deliverable should use this schema for consistency and portability.

```
Column A: keyword (the exact keyword phrase)
Column B: search_volume (monthly search volume, national)
Column C: keyword_difficulty (KD score 0-100)
Column D: cpc (cost per click in USD)
Column E: search_intent (informational | navigational | commercial | transactional)
Column F: cluster_id (numeric ID grouping related keywords)
Column G: cluster_name (human-readable name for the cluster, usually the primary keyword)
Column H: primary_keyword (TRUE/FALSE — is this the primary keyword for the cluster?)
Column I: target_url (the URL this keyword maps to, or "NEW" if a page needs to be created)
Column J: priority_score (composite score from the prioritization matrix, 1-125)
Column K: priority_tier (P1 | P2 | P3 | P4)
Column L: business_value_score (1-5)
Column M: search_demand_score (1-5)
Column N: competitive_feasibility_score (1-5)
Column O: page_type (homepage | category | product | comparison | blog | landing | tool)
Column P: geo_modifier (city or region if applicable, blank if not)
Column Q: notes (any special considerations)
```

### Example Rows
```
keyword,search_volume,keyword_difficulty,cpc,search_intent,cluster_id,cluster_name,primary_keyword,target_url,priority_score,priority_tier,business_value_score,search_demand_score,competitive_feasibility_score,page_type,geo_modifier,notes
project management software,33100,72,12.50,commercial,1,project management software,TRUE,/project-management-software,40,P2,5,5,2,category,,High competition - long term play
best project management tools,12100,65,8.20,commercial,1,project management software,FALSE,/project-management-software,40,P2,5,4,2,category,,Secondary keyword in cluster
project management software for small business,2400,38,6.80,commercial,2,pm software small business,TRUE,NEW,75,P1,5,3,4,category,,Good opportunity - create new page
how to manage projects effectively,1900,22,1.20,informational,3,project management guide,TRUE,/blog/project-management-guide,36,P3,2,3,5,blog,,Top of funnel content
```

---

## 11. Process Checklist

Use this checklist for every keyword research engagement:

- [ ] Define seed keywords (5-15) based on the business offering.
- [ ] Run competitor keyword analysis (3-5 competitors, top 100 keywords each).
- [ ] Expand seeds using autocomplete, PAA, related searches, and modifier lists.
- [ ] Deduplicate the raw keyword list.
- [ ] Classify each keyword by search intent.
- [ ] Cluster keywords by SERP overlap and intent.
- [ ] Assign a primary keyword to each cluster.
- [ ] Score each cluster on Business Value, Search Demand, Competitive Feasibility.
- [ ] Calculate composite priority score and assign tier (P1-P4).
- [ ] Map each cluster to an existing URL or flag as "NEW."
- [ ] Check for cannibalization against existing pages.
- [ ] Apply geo modifier rules if the business has local relevance.
- [ ] Export to the standardized CSV schema.
- [ ] Review with stakeholders and finalize priorities.

# Programmatic SEO — General SEO Skill

> Reusable programmatic SEO methodology for scaling pages from structured data.

---

## 1. When Programmatic SEO Makes Sense

Programmatic SEO works when there's a repeatable pattern of search queries that can be satisfied with templatized pages populated from structured data.

### Good Candidates

| Pattern | Example | Data Requirement |
|---------|---------|-----------------|
| Location variants | "best coffee shops in [city]" | City database + business listings |
| Comparison matrices | "[Product A] vs [Product B]" | Product feature database |
| Directory/listings | "[profession] in [location]" | Professional profiles database |
| Glossary/definitions | "what is [term]" | Term definitions database |
| Tool pages | "[keyword] calculator/generator" | Algorithm + user input |
| Data pages | "[topic] statistics [year]" | Statistics database |
| Template galleries | "[category] templates" | Template library |
| Integration pages | "[product] + [integration]" | Integration metadata |

### Bad Candidates (Avoid)

- Queries that require unique editorial insight (opinion pieces, reviews)
- Queries with < 10 monthly searches per variant
- Categories where you can't provide unique value per page
- Topics where a single comprehensive page would serve better
- Queries that require real-time data you can't maintain

### Decision Framework

Answer YES to all before proceeding:
1. Is there a clear, repeatable query pattern with provable search volume?
2. Can you provide genuinely unique, useful content per page (not just swapped variables)?
3. Do you have (or can you build) a reliable data source?
4. Can you maintain data accuracy at scale?
5. Would users actually find these pages helpful (not just search engines)?

---

## 2. Template Design

### Template Components

Every programmatic page template needs:

| Component | Purpose | Example |
|-----------|---------|---------|
| Static frame | Consistent structure across all pages | Navigation, header layout, CTA placement |
| Dynamic primary content | Unique data per page | City-specific data, product specs, definitions |
| Dynamic supporting content | Context that varies by page | Related items, FAQs specific to this entity |
| Unique editorial content | Human-quality content per page or category | Category-level descriptions, expert commentary |
| Internal linking | Connects to parent/sibling pages | Breadcrumbs, related pages, category navigation |
| Schema markup | Structured data per page type | LocalBusiness, Product, FAQPage |

### Minimum Unique Content Rules

| Content Type | Minimum Unique Content per Page |
|-------------|-------------------------------|
| Data pages | 200+ unique data points or 300+ unique words |
| Comparison pages | Unique feature comparison table + 200+ words analysis |
| Location pages | 300+ words unique to this location + local data |
| Directory listings | 5+ unique listings per page + category description |
| Glossary pages | 200+ words unique definition + examples |
| Tool pages | Unique output based on user input + explanation |

**Rule of thumb:** If you removed all the templatized/repeated content, each page should still have enough unique substance to justify its existence.

---

## 3. Data Source Requirements

### Data Quality Checklist

- [ ] **Completeness:** Data exists for every page you plan to create (no empty pages)
- [ ] **Accuracy:** Data is verified and current (not scraped from unreliable sources)
- [ ] **Uniqueness:** Each page has meaningfully different data (not trivial variations)
- [ ] **Updatability:** You have a process to refresh data regularly
- [ ] **Enrichability:** You can add more data fields over time to improve pages
- [ ] **Attribution:** You have rights to use the data (no copyright issues)

### Data Sources by Pattern

| Pattern | Good Data Sources |
|---------|------------------|
| Location pages | Government databases, Google Places API, census data, your own user data |
| Product comparisons | Product APIs, manufacturer specs, your own testing |
| Directory listings | User-submitted profiles, API integrations, partnerships |
| Glossary | Original definitions (NOT copied from Wikipedia/competitors) |
| Statistics | Primary research, government data, industry reports (with permission) |

---

## 4. URL Structure for Programmatic Pages

### Patterns

| Structure | When to Use | Example |
|-----------|------------|---------|
| Flat | < 500 pages, single dimension | `/digital-business-card-[city]` |
| Hierarchical | Multi-dimensional, natural hierarchy | `/[category]/[subcategory]/[item]` |
| Hub-spoke | Category pages linking to detail pages | `/cities/` → `/cities/mumbai/` |

### Rules

- Keep URLs human-readable and keyword-rich
- Maximum 3 levels deep
- Use hyphens, not underscores
- Include the primary variable in the URL (city name, product name, etc.)
- Avoid URL parameters for programmatic pages (use clean URLs)
- Ensure every URL is unique (no duplicates from data issues)

---

## 5. Internal Linking for Programmatic Sets

### Hierarchy

```
Index/Hub Page (e.g., /cities/)
├── Category Pages (e.g., /cities/maharashtra/)
│   ├── Detail Pages (e.g., /cities/mumbai/)
│   ├── Detail Pages (e.g., /cities/pune/)
│   └── ...
├── Category Pages (e.g., /cities/karnataka/)
│   ├── Detail Pages
│   └── ...
└── ...
```

### Linking Rules

| From → To | Link Type | Implementation |
|-----------|-----------|---------------|
| Hub → Categories | Navigation links | Listed on hub page |
| Category → Details | List links | All items in category listed |
| Detail → Category | Breadcrumb + contextual | "More in [Category]" |
| Detail → Sibling Details | "Related" section | 3-5 related pages |
| Detail → Hub | Breadcrumb | Navigation path |
| Non-programmatic → Hub | Contextual links from blog/main site | |

### Pagination

- For categories with > 20-30 items: paginate
- Use `rel="next"` and `rel="prev"` (still helpful for some crawlers)
- Ensure all pages are reachable within 3 clicks from the hub
- Include a "View All" option if total items < 200

---

## 6. Quality Thresholds

### Launch Gate Checklist

Before launching any programmatic page set:

- [ ] Every page has unique title tag containing the primary variable
- [ ] Every page has unique meta description
- [ ] Every page has unique H1
- [ ] Every page has minimum unique content (see table in section 2)
- [ ] No two pages are > 80% similar (deduplicate or differentiate)
- [ ] All data fields are populated (no empty sections)
- [ ] Internal links are functional (no broken links)
- [ ] Schema markup is valid on all pages (test 5% sample)
- [ ] Pages load in < 3 seconds (test 5% sample)
- [ ] Mobile rendering is correct (test 5% sample)
- [ ] Canonical tags are self-referencing on all pages

### Ongoing Quality Monitoring

| Check | Frequency | Threshold |
|-------|-----------|-----------|
| Thin content scan | Monthly | Flag pages with < minimum unique content |
| Duplicate content scan | Monthly | Flag pages with > 80% similarity |
| Broken data check | Weekly | Flag pages with empty/missing data fields |
| Index coverage | Weekly | All intended pages indexed |
| Traffic per page | Monthly | Flag pages with 0 traffic after 90 days |

---

## 7. Index Management

### Controlling What Gets Indexed

| Scenario | Action |
|----------|--------|
| All pages have unique value | Index all |
| Some pages are thin/low-quality | Noindex thin pages, index quality pages |
| Too many pages for crawl budget | Prioritize high-value pages in sitemap, noindex low-value |
| Seasonal pages | Index during season, noindex off-season |

### Sitemap Strategy for Large Sets

- Separate sitemap for programmatic pages: `/sitemap-programmatic.xml`
- Split into multiple sitemaps if > 10,000 URLs (max 50,000 per file)
- Include only indexable pages in sitemap
- Update `<lastmod>` when page data changes
- Submit sitemap to Search Console

### Crawl Budget Optimization

For sets with > 10,000 pages:
1. Ensure fast server response time (< 200ms TTFB)
2. Use efficient pagination (don't force deep crawling)
3. Minimize redirect chains
4. Eliminate duplicate content
5. Use `robots.txt` to block irrelevant parameters
6. Monitor crawl stats in Search Console

---

## 8. Avoiding Google Penalties

### Thin Content

- **Risk:** Pages with little unique value get flagged as thin content
- **Prevention:** Ensure minimum unique content per page, add editorial enrichment
- **Detection:** Search Console "Excluded" pages increasing, manual actions

### Doorway Pages

- **Risk:** Pages designed solely to rank for variations with no user value
- **Prevention:** Each page must provide genuinely useful, unique information
- **Detection:** Manual action in Search Console

### Duplicate Content

- **Risk:** Pages too similar to each other
- **Prevention:** Deduplicate data, ensure unique content sections, canonical tags
- **Detection:** Screaming Frog duplicate content report

### Spam

- **Risk:** Auto-generated content that's nonsensical or AI-generated without quality control
- **Prevention:** Human review of sample pages, quality scoring automation
- **Detection:** Sudden ranking drops, manual actions

---

## 9. Testing and Rollout Strategy

### Phase 1: Proof of Concept (Week 1-2)

1. Create 10-20 pages from the template
2. Ensure all quality thresholds pass
3. Submit to Search Console
4. Wait 2-4 weeks for indexing and initial ranking signals

### Phase 2: Validation (Week 3-6)

1. Monitor index coverage (are pages getting indexed?)
2. Monitor rankings (are pages appearing for target keywords?)
3. Monitor traffic (any organic visits?)
4. Assess quality feedback (bounce rate, time on page)
5. **Decision gate:** If > 50% indexed and some ranking signals → proceed. If not → diagnose and fix.

### Phase 3: Scale (Week 7+)

1. Launch remaining pages in batches (100-500 per week for large sets)
2. Monitor index coverage and quality metrics with each batch
3. Pause if quality metrics decline
4. Iterate on template based on performance data

### Phase 4: Optimize (Ongoing)

1. Identify top-performing programmatic pages — what makes them work?
2. Apply learnings to underperformers
3. Add more unique content to high-potential pages
4. Prune zero-traffic pages after 90 days
5. Expand to new dimensions (e.g., add profession variants after location variants succeed)

---

## 10. Common Programmatic SEO Patterns

### City/Location Pages

```
Template: /[service]-in-[city]
Data: city name, population, local data points, nearby cities
Unique content: local market context, city-specific statistics
Internal links: state/region hub → city pages → related cities
```

### Comparison Pages

```
Template: /[product-a]-vs-[product-b]
Data: feature matrices, pricing, ratings for both products
Unique content: analysis paragraph, recommendation, use-case guidance
Internal links: category hub → comparison pages → product pages
```

### Glossary/Definition Pages

```
Template: /glossary/[term]
Data: term, definition, related terms, examples
Unique content: in-depth explanation, use cases, visual aids
Internal links: glossary index → term pages → related terms
```

---

## 11. Output Format: Programmatic SEO Specification

```markdown
## Programmatic SEO Spec: [Pattern Name]

### Query Pattern
[Example queries with search volume]

### URL Structure
[URL template with variables]

### Data Source
[Where data comes from, update frequency]

### Template Sections
[List each section with static vs dynamic content]

### Unique Content Strategy
[How each page will be unique — minimum content rules]

### Estimated Page Count
[Total pages to create]

### Internal Linking Plan
[Hub → category → detail linking structure]

### Schema Markup
[Which schema types per page]

### Launch Plan
[Phase 1 count, Phase 2 count, timeline]

### Quality Gates
[Metrics that must pass before scaling]
```

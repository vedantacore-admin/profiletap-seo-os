# Rank Tracking and SEO Analytics

## Skill Metadata
- **Command**: `/rank-tracking-analytics`
- **Purpose**: Set up SEO measurement frameworks, rank tracking, reporting dashboards, and analytics workflows
- **Output**: Measurement plan, reporting templates, and dashboard specifications

---

## 1. KPI Framework

### Primary SEO KPIs

| KPI | What It Measures | Source | Target Cadence |
|---|---|---|---|
| **Organic Sessions** | Total visits from organic search | GA4 | Weekly |
| **Organic Impressions** | How often your pages appear in search results | Google Search Console | Weekly |
| **Organic Clicks** | How many searchers click through to your site | Google Search Console | Weekly |
| **Average CTR** | Click-through rate from SERPs | Google Search Console | Monthly |
| **Average Position** | Mean ranking position across tracked keywords | GSC / Rank Tracker | Weekly |
| **Keyword Rankings** | Positions for specific target keywords | Rank Tracker | Weekly |
| **Keyword Visibility Score** | Aggregate ranking strength across all keywords | SEMrush / Ahrefs | Monthly |
| **Organic Conversions** | Goal completions or transactions from organic traffic | GA4 | Monthly |
| **Organic Conversion Rate** | Percentage of organic visitors who convert | GA4 | Monthly |
| **Organic Revenue** | Revenue attributed to organic traffic | GA4 | Monthly |
| **Backlink Count** | Total referring domains and backlinks | Ahrefs / SEMrush | Monthly |
| **Domain Authority/Rating** | Overall site authority score | Ahrefs DR / Moz DA | Monthly |
| **Indexed Pages** | Number of pages in Google's index | GSC Coverage Report | Monthly |
| **Core Web Vitals** | LCP, INP, CLS performance scores | GSC CWV Report / PageSpeed Insights | Monthly |
| **Crawl Errors** | Pages Google cannot access or index | GSC Coverage Report | Weekly |

### Secondary SEO KPIs

| KPI | What It Measures | Source |
|---|---|---|
| Pages per session (organic) | Content engagement depth | GA4 |
| Average engagement time (organic) | Time spent on site | GA4 |
| Bounce rate (organic) | Single-page sessions | GA4 |
| New vs returning organic visitors | Audience growth | GA4 |
| Featured snippet count | SERP feature ownership | Rank Tracker |
| PAA appearances | "People Also Ask" visibility | Rank Tracker |
| Brand vs non-brand organic split | Brand awareness growth | GSC |
| Page speed scores (mobile/desktop) | Technical performance | PageSpeed Insights |
| Internal link equity distribution | Information architecture health | Screaming Frog / Sitebulb |

---

## 2. Tool Selection Guide

### Free/Essential Tools (Every Site Needs These)

**Google Search Console (GSC)**
- Purpose: Keyword performance, indexing status, crawl health, Core Web Vitals
- Setup: Verify site ownership via DNS, HTML tag, or GA4 property
- Key reports: Performance, Coverage, Core Web Vitals, Links, Sitemaps
- Limitation: Only shows data for your own site, 16-month data retention, sampled data for high-volume sites

**Google Analytics 4 (GA4)**
- Purpose: User behavior, conversions, traffic sources, landing page performance
- Setup: Install GA4 tag via Google Tag Manager or direct snippet
- Key reports: Traffic acquisition (organic filter), Landing pages, Conversions, User behavior
- Limitation: Organic keyword data is "(not provided)" — use GSC for keyword-level data

**Google PageSpeed Insights**
- Purpose: Core Web Vitals measurement, performance diagnostics
- Use: Test key landing pages monthly and after any site changes

### Paid Tools (Choose Based on Needs and Budget)

**Rank Tracking Tools**
| Tool | Strength | Best For | Starting Price |
|---|---|---|---|
| SEMrush | All-in-one SEO suite, competitive analysis | Teams needing one platform for everything | $130/mo |
| Ahrefs | Best backlink database, content explorer | Link building and competitive research | $100/mo |
| Ubersuggest | Budget-friendly keyword research | Small businesses and solopreneurs | $30/mo |
| SE Ranking | Affordable rank tracking with white-label | Agencies tracking many clients | $50/mo |
| AccuRanker | Fastest rank updates, on-demand checks | Sites needing daily rank monitoring | $130/mo |
| Wincher | Simple, affordable daily rank tracking | Small sites focused only on rankings | $30/mo |

**Technical SEO Audit Tools**
| Tool | Purpose | Starting Price |
|---|---|---|
| Screaming Frog | Website crawling and technical audit | Free (up to 500 URLs) |
| Sitebulb | Visual technical audit with prioritized issues | $35/mo |
| ContentKing | Real-time SEO monitoring and alerting | $50/mo |

### Tool Stack Recommendations by Budget

**Minimal Budget ($0/mo):**
Google Search Console + GA4 + Screaming Frog Free + Google Sheets for tracking

**Small Budget ($30-50/mo):**
Above + Ubersuggest or Wincher for keyword tracking

**Medium Budget ($100-200/mo):**
GSC + GA4 + Ahrefs or SEMrush + Screaming Frog Paid

**Full Budget ($300+/mo):**
GSC + GA4 + Ahrefs + SEMrush + AccuRanker + Screaming Frog Paid + ContentKing

---

## 3. Keyword Grouping for Tracking

### Grouping Dimensions

**By Page**
Group keywords by the page they are assigned to. Every target keyword maps to exactly one page.
```
/product-page        → "product name", "product name review", "buy product name"
/how-to-guide        → "how to do X", "X tutorial", "X step by step"
/comparison-page     → "X vs Y", "X alternatives", "best X tools"
```

**By Search Intent**
```
Informational  → "what is X", "how to X", "X guide", "X explained"
Navigational   → "brand name", "brand login", "brand pricing"
Commercial     → "best X", "X reviews", "X comparison", "top X tools"
Transactional  → "buy X", "X pricing", "X free trial", "X signup"
```

**By Topic Hub / Category**
Group keywords by the topic cluster or content hub they belong to.
```
Hub: Email Marketing
  → "email marketing strategy", "email subject lines", "email automation", "email deliverability"
Hub: SEO
  → "keyword research", "on-page SEO", "link building", "technical SEO"
```

**By Priority Tier**
```
Tier 1 (Critical)   → Top 10-20 keywords with highest business value and search volume
Tier 2 (Important)  → Next 30-50 keywords with moderate volume or high conversion potential
Tier 3 (Monitor)    → Long-tail keywords, low volume but collectively significant
Tier 4 (Watch)      → Aspirational keywords you cannot rank for yet but want to track
```

**By Funnel Stage**
```
Awareness    → Broad informational queries, "what is" queries
Consideration → Comparison queries, "best" queries, "how to choose"
Decision     → Brand queries, pricing queries, "vs" queries with your brand
Retention    → Support queries, "how to use" queries, feature queries
```

### Keyword Tracking Sheet Format
```
| Keyword | Page URL | Intent | Hub | Tier | Funnel | Volume | Current Rank | Previous Rank | Change | Target Rank |
```

---

## 4. Reporting Cadence Framework

### Daily Monitoring (Automated Alerts Only)
No manual daily reports. Set up automated alerts for:
- Ranking drops greater than 10 positions for Tier 1 keywords
- Organic traffic drops greater than 30% day-over-day (compared to same day previous week)
- Crawl error spikes (5+ new errors in a day)
- Site downtime or server errors (5xx spike)
- Manual action notifications in GSC

### Weekly Status Report
**Time to produce**: 15-30 minutes
**Audience**: SEO team, content team

Contents:
1. Organic traffic this week vs last week vs same week last year
2. Tier 1 keyword ranking movements (up/down/stable)
3. New content published this week and initial indexing status
4. Crawl errors or technical issues flagged
5. Top 5 gaining pages and top 5 declining pages
6. Action items for next week

### Monthly Deep Review
**Time to produce**: 2-4 hours
**Audience**: Marketing leadership, stakeholders

Contents:
1. Executive summary (3-5 key takeaways)
2. Organic traffic trend (month-over-month and year-over-year)
3. Full keyword ranking report across all tiers
4. Conversion and revenue from organic traffic
5. Backlink growth and new referring domains
6. Content performance (top pages, declining pages, new content impact)
7. Technical health summary (Core Web Vitals, crawl stats, indexing)
8. Competitive landscape changes
9. Progress against quarterly goals
10. Recommendations and priorities for next month

### Quarterly Strategy Review
**Time to produce**: 1-2 days
**Audience**: Executive team, cross-functional stakeholders

Contents:
1. Quarter performance vs goals (did we hit targets?)
2. ROI calculation (organic traffic value, conversion attribution, revenue)
3. Competitive position changes
4. Content audit results and refresh priorities
5. Technical SEO audit findings
6. Backlink profile analysis
7. Strategy adjustments for next quarter
8. Resource requirements and budget recommendations
9. Updated keyword targets and content roadmap
10. Risk assessment (algorithm update exposure, competitive threats)

---

## 5. Alert Threshold Definitions

### Ranking Alerts

| Condition | Severity | Response |
|---|---|---|
| Tier 1 keyword drops 3+ positions | Warning | Investigate within 48 hours |
| Tier 1 keyword drops 10+ positions | Critical | Investigate immediately |
| Tier 1 keyword exits page 1 (position 11+) | Critical | Same-day investigation |
| Multiple Tier 1 keywords drop simultaneously | Emergency | Check for algorithm update or technical issue |
| Tier 2 keyword drops 5+ positions | Warning | Review within 1 week |
| New keyword enters top 10 | Positive | Document and monitor for consolidation |

### Traffic Alerts

| Condition | Severity | Response |
|---|---|---|
| Organic traffic drops 15%+ week-over-week | Warning | Check for seasonality, then investigate |
| Organic traffic drops 30%+ week-over-week | Critical | Immediate investigation |
| Organic traffic drops 50%+ day-over-day | Emergency | Check for site outage or deindexing |
| Single page traffic drops 40%+ month-over-month | Warning | Check rankings, SERP changes |

### Technical Alerts

| Condition | Severity | Response |
|---|---|---|
| 5+ new crawl errors in a day | Warning | Review within 24 hours |
| 50+ new crawl errors in a day | Critical | Immediate investigation |
| Core Web Vital regresses from "Good" to "Needs Improvement" | Warning | Investigate within 1 week |
| Core Web Vital regresses to "Poor" | Critical | Prioritize fix within 48 hours |
| Indexed page count drops 10%+ | Critical | Check for noindex issues, robots.txt changes |
| Manual action in GSC | Emergency | Address immediately |

---

## 6. Baseline Measurement Process

Before making any significant SEO changes, capture a complete baseline.

### What to Capture

**Traffic Baseline (GA4)**
- Total organic sessions (last 30 days, last 90 days, last 12 months)
- Organic sessions by landing page (top 50 pages)
- Organic conversion rate and conversion count
- Organic revenue (if applicable)
- Organic bounce rate and engagement time

**Ranking Baseline**
- Current positions for all tracked keywords (export full ranking report)
- Number of keywords ranking on page 1, page 2, page 3+
- Featured snippet ownership count
- Keyword visibility score

**Search Console Baseline**
- Total impressions, clicks, CTR, average position (last 28 days and last 3 months)
- Top 100 queries by clicks
- Top 50 pages by clicks
- Crawl stats (pages crawled per day, download size, response time)
- Index coverage (valid, excluded, error counts)

**Backlink Baseline**
- Total backlinks and referring domains
- Domain Rating / Domain Authority
- Top linking domains
- Anchor text distribution

**Technical Baseline**
- Core Web Vitals scores (LCP, INP, CLS) for mobile and desktop
- Page speed scores for key landing pages
- Total pages in sitemap vs total indexed pages
- Crawl error count by type

### Baseline Documentation Format
```
=== SEO BASELINE SNAPSHOT ===
Date: [Date]
Captured By: [Name]
Reason: [What change is being planned]

Organic Traffic (Last 30 Days): [Number]
Organic Conversions (Last 30 Days): [Number]
Keywords on Page 1: [Number]
Keywords on Page 2: [Number]
Domain Rating: [Number]
Referring Domains: [Number]
Indexed Pages: [Number]
Core Web Vitals Status: [Good/Needs Improvement/Poor]

[Attach full exports from GSC, GA4, and rank tracker]
```

---

## 7. ROI Calculation Methodology

### Organic Traffic Value
Calculate what your organic traffic would cost if you had to buy it via PPC.

```
Organic Traffic Value = SUM(keyword_monthly_organic_clicks * keyword_CPC)
```

For each keyword you rank for:
1. Get the estimated monthly organic clicks (from rank tracker or GSC)
2. Get the CPC for that keyword (from Google Ads Keyword Planner or SEMrush)
3. Multiply clicks by CPC
4. Sum across all keywords

### Conversion Attribution
```
Organic SEO Revenue = Organic Conversions * Average Conversion Value
```

For lead-gen businesses:
```
Organic SEO Revenue = Organic Leads * Lead-to-Customer Rate * Average Customer Value
```

### SEO ROI Formula
```
SEO ROI = (Organic Revenue - SEO Investment) / SEO Investment * 100

SEO Investment = Content costs + Tool costs + Agency/team costs + Technical implementation costs
```

### Payback Period
```
Monthly SEO Cost = Total SEO Investment / Number of Months
Monthly Organic Value = Monthly Organic Traffic Value + Monthly Organic Revenue
Payback Period = Total SEO Investment / Monthly Organic Value
```

### Attribution Models for Organic
- **Last-click**: Credit goes to organic only if it was the final touchpoint before conversion. Simplest but undervalues organic's role in awareness.
- **First-click**: Credit goes to organic if it was the first touchpoint. Better captures organic's discovery role.
- **Data-driven (GA4)**: GA4's machine learning model distributes credit across touchpoints. Most accurate but requires sufficient conversion data.
- **Recommended approach**: Use data-driven attribution in GA4 and supplement with first-click analysis to show organic's full-funnel impact.

---

## 8. Dashboard Design

### Executive Dashboard (Monthly View)
Show on a single screen:
1. Organic traffic trend (12-month line chart, with year-over-year comparison)
2. Organic conversions and revenue (12-month bar chart)
3. Top 10 keywords with rank and change (table)
4. Organic traffic value in dollars (single metric with month-over-month change)
5. Domain rating trend (6-month line)
6. Core Web Vitals status (pass/fail indicator)

### SEO Team Dashboard (Weekly View)
Show:
1. Organic sessions this week vs last week (number with percentage change)
2. Tier 1 keyword rankings (table with sparkline trends)
3. Top 10 gaining pages and top 10 declining pages (tables)
4. New backlinks this week (count + top referring domains)
5. Crawl errors (count with trend)
6. Content pipeline status (published, in review, in progress counts)
7. Alerts triggered this week (list)

### Content Performance Dashboard
Show:
1. Top 20 pages by organic traffic (table with trend)
2. Pages with declining traffic (table, sorted by magnitude of decline)
3. New content performance (pages published in last 90 days with traffic, rankings, impressions)
4. Content gap opportunities (keywords with impressions but low CTR)
5. Pages with high impressions but low clicks (CTR optimization opportunities)

### Tool Recommendations for Dashboards
- **Google Looker Studio** (free): Connect GSC and GA4 directly. Best for most teams.
- **Google Sheets**: Manual but flexible. Good for small teams or custom calculations.
- **Databox**: Automated multi-source dashboards with alerts. Good for agencies.
- **SEMrush / Ahrefs built-in reports**: Use when you already have these tools.

---

## 9. Competitive Benchmarking Setup

### Competitor Identification
1. **SERP competitors**: Who ranks on page 1 for your top 20 target keywords? These are your true SEO competitors (may differ from business competitors).
2. **Domain overlap competitors**: Use SEMrush or Ahrefs "competing domains" report to find sites with the highest keyword overlap.
3. Select 3-5 primary competitors to track consistently.

### What to Benchmark

| Metric | Tool | Cadence |
|---|---|---|
| Domain Rating / Authority | Ahrefs / SEMrush | Monthly |
| Total organic traffic estimate | SEMrush / Ahrefs | Monthly |
| Number of ranking keywords | SEMrush / Ahrefs | Monthly |
| Keywords on page 1 | SEMrush / Ahrefs | Monthly |
| Referring domains count | Ahrefs | Monthly |
| Content volume (total indexed pages) | site:competitor.com in Google | Quarterly |
| Core Web Vitals scores | PageSpeed Insights | Quarterly |
| New content published | Monitor their blog/sitemap | Monthly |
| SERP feature ownership (snippets, PAA) | Rank tracker | Monthly |

### Competitive Gap Analysis
1. Export your keyword rankings and competitor keyword rankings
2. Identify keywords where competitors rank on page 1 and you rank on page 2+ (or do not rank)
3. Prioritize gaps by search volume and business relevance
4. Create content or optimize existing pages to close the top gaps
5. Repeat quarterly

---

## 10. Search Console Data Analysis

### Key GSC Analyses to Run Regularly

**Query Analysis**
- Sort by impressions to find high-impression, low-click queries (CTR optimization opportunities)
- Filter by queries where average position is 4-15 (striking distance — push to top 3)
- Compare date ranges (last 28 days vs previous 28 days) to spot trending queries
- Filter brand vs non-brand queries to isolate organic growth from brand awareness

**Page Analysis**
- Identify top pages by clicks — these are your most valuable organic assets
- Find pages with declining clicks (compare 3-month periods) — candidates for content refresh
- Identify pages ranking for unexpected queries — opportunities to optimize or create dedicated pages
- Find pages with high impressions but position 10-20 — best candidates for optimization ROI

**Device Analysis**
- Compare mobile vs desktop performance (CTR and position)
- Identify pages performing significantly worse on mobile — prioritize mobile optimization

**Country/Region Analysis**
- Identify unexpected traffic from non-target countries
- Find country-specific ranking opportunities
- Validate geo-targeting settings

### GSC Data Export Process
1. Go to Performance report
2. Set date range (last 3 months recommended for analysis)
3. Export queries report and pages report as CSV
4. Import into Google Sheets or your analysis tool
5. Add formulas for CTR benchmarks by position, identify outliers
6. Cross-reference with GA4 data for conversion context

---

## 11. GA4 Organic Traffic Analysis

### Essential GA4 Reports for SEO

**Traffic Acquisition Report**
- Filter by Session default channel group = "Organic Search"
- Metrics: Sessions, Users, Engaged sessions, Engagement rate, Conversions, Revenue

**Landing Page Report**
- Filter organic traffic only
- Metrics: Sessions, Users, Engagement rate, Average engagement time, Conversions
- Sort by sessions to find top organic landing pages
- Sort by conversions to find highest-converting organic pages

**User Behavior Flow**
- Filter organic entry sessions
- Analyze: What pages do organic visitors go to after landing?
- Identify drop-off points and navigation patterns
- Find opportunities to improve internal linking and conversion paths

### GA4 Segments for SEO Analysis
Create these custom segments:
1. **Organic non-brand**: Exclude sessions where landing page is homepage or contains brand terms
2. **Organic converters**: Organic sessions that completed a conversion event
3. **High-engagement organic**: Organic sessions with engagement time above average
4. **Organic blog traffic**: Organic sessions landing on blog content
5. **Organic product/service traffic**: Organic sessions landing on money pages

### GA4 + GSC Integration
Link GSC to GA4 for the "Search Console" reports within GA4:
1. In GA4, go to Admin > Product Links > Search Console Links
2. Associate your GSC property
3. Access reports at Reports > Search Console > Queries and Google organic search traffic
4. This lets you see GSC query data alongside GA4 engagement data

---

## 12. Output Format: Measurement Plan Template

```
=== SEO MEASUREMENT PLAN ===

Business: [Name]
Website: [URL]
Plan Date: [Date]
Plan Owner: [Name]

--- GOALS ---
Quarterly Goal 1: [e.g., Increase organic traffic by 25% YoY]
Quarterly Goal 2: [e.g., Rank in top 3 for 10 Tier 1 keywords]
Quarterly Goal 3: [e.g., Generate 50 organic conversions per month]
Annual Goal: [e.g., Achieve $X in organic traffic value]

--- TRACKED KEYWORDS ---
Total keywords tracked: [Number]
Tier 1 (Critical): [Number] keywords — [list or link to sheet]
Tier 2 (Important): [Number] keywords
Tier 3 (Monitor): [Number] keywords
Tier 4 (Watch): [Number] keywords

--- TOOLS IN USE ---
| Tool | Purpose | Owner | Cost |
|---|---|---|---|
| Google Search Console | Rankings, indexing, CWV | [Name] | Free |
| GA4 | Traffic, conversions, behavior | [Name] | Free |
| [Rank Tracker] | Daily keyword tracking | [Name] | $X/mo |
| [SEO Tool] | Backlinks, competitive analysis | [Name] | $X/mo |
| [Crawl Tool] | Technical audits | [Name] | $X/mo |

--- REPORTING SCHEDULE ---
| Report | Cadence | Audience | Owner | Delivery |
|---|---|---|---|---|
| Alert monitoring | Daily (automated) | SEO team | [Name] | Email/Slack |
| Weekly status | Every Monday | SEO + Content team | [Name] | Slack/Email |
| Monthly review | First week of month | Marketing leadership | [Name] | Slide deck |
| Quarterly review | First 2 weeks of quarter | Executive team | [Name] | Presentation |

--- ALERT THRESHOLDS ---
[Copy relevant thresholds from Section 5 and customize values]

--- BASELINE SNAPSHOT ---
Date captured: [Date]
Organic monthly sessions: [Number]
Keywords on page 1: [Number]
Domain Rating: [Number]
Referring domains: [Number]
Monthly organic conversions: [Number]
Organic traffic value: $[Number]

--- DASHBOARD LINKS ---
Executive dashboard: [URL]
SEO team dashboard: [URL]
Content performance dashboard: [URL]

--- COMPETITIVE SET ---
Competitor 1: [Domain] — DR [Number], Est. organic traffic [Number]
Competitor 2: [Domain] — DR [Number], Est. organic traffic [Number]
Competitor 3: [Domain] — DR [Number], Est. organic traffic [Number]
```

### Measurement Plan Checklist
- [ ] GSC is set up and verified
- [ ] GA4 is installed with conversion events configured
- [ ] GSC and GA4 are linked
- [ ] Rank tracking tool is configured with all target keywords
- [ ] Keywords are grouped by page, intent, hub, tier, and funnel stage
- [ ] Baseline snapshot is captured and documented
- [ ] Alert thresholds are configured in monitoring tools
- [ ] Dashboard is built and shared with stakeholders
- [ ] Reporting schedule is agreed upon and calendar invites are sent
- [ ] Competitive set is defined and benchmarking is configured
- [ ] Quarterly review dates are scheduled for the year

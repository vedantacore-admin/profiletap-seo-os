# SEO Measurement Plan — ProfileTap

## Purpose

Define KPIs, tools, reporting cadence, alert thresholds, and baseline measurement processes for tracking ProfileTap's organic search performance.

---

## 1. KPI Framework

### Primary KPIs (Business Impact)

| KPI | Definition | Target (Launch +90d) | Target (Launch +180d) |
|-----|-----------|---------------------|----------------------|
| Organic create_profile conversions | Sign-ups from organic traffic | 50/month | 200/month |
| Organic traffic | Total sessions from organic search | 2,000/month | 10,000/month |
| P1 keyword rankings (top 10) | % of P1 keywords in top 10 positions | 30% | 60% |

### Secondary KPIs (Leading Indicators)

| KPI | Definition | Target |
|-----|-----------|--------|
| Indexed pages | Pages successfully indexed in Google | 100% of published pages |
| Average position (P1 keywords) | Mean ranking for P1 keyword set | < 20 by +90d, < 10 by +180d |
| CTR (Search Console) | Click-through rate from search results | > 3% average |
| Backlinks acquired | New referring domains per month | 5-10/month |
| Content published | Pages published per month | 4-8/month |
| Blog-to-money-page CTR | Click-through from blog to commercial pages | > 5% |
| Hub traffic by segment | Sessions per hub | Business > Creator > Pet > Others |
| Comparison page switch rate | Sign-ups from comparison pages | > 3% conversion |

### Health Metrics (Operational)

| Metric | Healthy Range |
|--------|--------------|
| Core Web Vitals pass rate | > 90% of pages passing |
| Crawl errors | 0 for published pages |
| Index coverage | 100% of intended pages indexed |
| Broken internal links | 0 |
| Page load time (median) | < 3 seconds |

---

## 2. Tool Stack

| Tool | Purpose | Setup Priority |
|------|---------|:---:|
| Google Search Console | Keyword rankings, impressions, CTR, index coverage, Core Web Vitals | P1 — set up before launch |
| Google Analytics 4 (GA4) | Traffic, user behavior, conversions, attribution | P1 — set up before launch |
| Ubersuggest | Keyword research, volume/KD data, competitor tracking | P1 — already in use |
| PageSpeed Insights | Core Web Vitals testing per page | P2 — test before each publish |
| Google Rich Results Test | Schema markup validation | P2 — test before each publish |
| Screaming Frog (or similar) | Site audit, crawl simulation, broken links | P3 — monthly audits |

### Search Console Setup

1. Verify property (DNS or HTML tag method)
2. Submit sitemap.xml
3. Set preferred country (India) in International Targeting
4. Monitor Coverage report weekly
5. Check Performance report for keyword/page data

### GA4 Setup

1. Create property and data stream
2. Set up organic traffic segment
3. Create conversion event for `create_profile` action
4. Create custom report: organic landing pages × conversions
5. Set up audiences: organic visitors by hub (using page path grouping)

---

## 3. Keyword Tracking Groups

### By Priority Tier

| Group | Keywords | Tracking Frequency |
|-------|----------|-------------------|
| P1 Critical | smart identity platform, digital business card india, nfc business card india, qr business card, hihello alternative india, popl alternative india, tapmo alternative, digital business card for doctors, digital business card for real estate agents, digital business card for freelancers | Daily |
| P2 Growth | personal branding platform india, pet id tag qr code, digital business card for creators, linktree alternative for creators, profiletap vs hihello, profiletap vs tapmo, ai review management, google review management, emergency qr code, lost and found qr tag, blinq alternative, taponn alternative | Weekly |
| P3 Support | family safety profile, travel qr code, vehicle qr code, vehicle qr code sticker, qr luggage tag, all blog keywords | Monthly |

### By Hub

| Hub | Primary Keywords to Track |
|-----|--------------------------|
| Platform | smart identity platform |
| Business | digital business card india, nfc business card india, qr business card, + all profession + comparison keywords |
| Creator | personal branding platform india, digital business card for creators, linktree alternative for creators |
| Family Safety | family safety profile, emergency qr code |
| Pet | pet id tag qr code, lost and found qr tag |
| Travel | travel qr code, qr luggage tag |
| Vehicle | vehicle qr code, vehicle qr code sticker |

---

## 4. Reporting Cadence

### Weekly Status (Every Monday)

**Time:** 15 minutes
**Source:** Google Search Console + GA4

Checklist:
- [ ] P1 keyword ranking changes (any drop > 3 positions?)
- [ ] Organic traffic trend (WoW change)
- [ ] New pages indexed this week
- [ ] Any crawl errors or index issues
- [ ] Content published this week
- [ ] Backlinks acquired this week

### Monthly Deep Review (First week of month)

**Time:** 1 hour
**Source:** All tools

Report sections:
1. **Traffic summary**: organic sessions, users, new users (MoM and YoY)
2. **Keyword rankings**: P1 average position trend, new top-10 rankings, lost top-10 rankings
3. **Content performance**: traffic and conversions by page, best/worst performers
4. **Hub performance**: traffic split by hub segment
5. **Conversion performance**: create_profile conversions from organic, conversion rate by page type
6. **Backlink progress**: new referring domains, prospect pipeline status
7. **Technical health**: Core Web Vitals, crawl errors, index coverage
8. **Action items**: specific next steps based on data

### Quarterly Strategy Review (First week of quarter)

**Time:** 2-3 hours

Review:
1. KPI progress vs targets
2. Keyword portfolio expansion opportunities
3. Content gap analysis (what competitors rank for that we don't)
4. Hub expansion decisions (which segments to invest more in)
5. Backlink strategy effectiveness
6. India vs global traffic split analysis
7. Priority re-ranking based on actual performance data
8. Next quarter goals and targets

---

## 5. Alert Thresholds

| Signal | Threshold | Action |
|--------|-----------|--------|
| P1 keyword drops > 5 positions | Within 48 hours | Investigate: content change? algorithm update? competitor move? |
| Organic traffic drops > 20% WoW | Immediate | Check Search Console for manual actions, crawl errors |
| Page deindexed | Immediate | Check robots.txt, noindex tags, canonical tags |
| Core Web Vitals failure | Within 1 week | Diagnose and fix (LCP, INP, or CLS regression) |
| New crawl errors | Within 3 days | Fix broken URLs, server errors, redirect issues |
| Conversion rate drops > 30% | Within 1 week | Check landing page changes, CTA changes, technical issues |
| Competitor launches new page targeting our P1 keyword | Within 1 week | Assess threat, consider content refresh or expansion |

---

## 6. Baseline Measurement Process

Before any major change (new page launch, content refresh, site migration):

### Capture Baseline

1. **Rankings**: Current position for all target keywords (Search Console, past 28 days)
2. **Traffic**: Organic sessions to affected pages (GA4, past 28 days)
3. **Impressions**: Search impressions for target keywords (Search Console, past 28 days)
4. **CTR**: Click-through rate for target keywords
5. **Conversions**: create_profile events from affected pages
6. **Backlinks**: Current referring domains to affected pages
7. **Core Web Vitals**: Current scores for affected pages

### Post-Change Measurement

- Compare same metrics at +7 days, +14 days, +30 days, +60 days
- Allow 2-4 weeks for Google to recrawl and reassess
- Document changes and results in monthly report

---

## 7. India vs Global Traffic Segmentation

### GA4 Setup

Create two segments:
1. **India organic**: Country = India AND Medium = organic
2. **Global organic**: Country ≠ India AND Medium = organic

### Reporting Split

Track separately:
- India organic traffic (primary market)
- Global organic traffic (secondary market)
- India conversion rate vs global conversion rate
- India keyword rankings vs global keyword rankings

### Decision Framework

| Signal | Action |
|--------|--------|
| India traffic growing, global flat | Stay the course — India-first strategy working |
| Global traffic growing faster than India | Investigate: are we ranking for global keywords? Consider geo-specific content |
| India conversion > global conversion | Invest more in India-specific pages and keywords |
| India conversion < global conversion | Review India landing pages for conversion optimization |

---

## 8. Competitive Benchmarking

Track competitor visibility for shared keywords:

### Competitors to Monitor

| Competitor | Priority | Check Frequency |
|-----------|:---:|:---:|
| HiHello | P1 | Monthly |
| Popl | P1 | Monthly |
| TapMo | P1 | Monthly |
| TapOnn | P1 | Monthly |
| Blinq | P2 | Quarterly |
| Linktree | P2 | Quarterly |

### What to Track

- Their ranking positions for our P1 keywords
- New pages they publish targeting our keywords
- Their backlink growth rate
- Their SERP features (featured snippets, PAA, etc.)

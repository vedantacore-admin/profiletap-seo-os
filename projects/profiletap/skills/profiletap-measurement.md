# ProfileTap SEO Measurement

## ProfileTap-Specific KPIs

### Primary KPI
**create_profile conversions from organic search**
This is the single most important metric. Every page in the system exists to drive profile creation or assist another page in driving profile creation.

Measurement:
- Track `create_profile` conversion events attributed to organic traffic
- Segment by landing page to identify which pages convert best
- Segment by hub to understand which segments drive the most value
- Segment by market (India vs global) to validate the India-first strategy

### Secondary KPIs

| KPI | Definition | Target Pages |
| --- | --- | --- |
| Hub traffic by segment | Organic sessions to each hub and its children | All 6 hubs + homepage |
| Comparison page switch rate | % of comparison page visitors who click CTA to create profile | `/hihello-alternative-india`, `/popl-alternative-india`, `/taponn-alternative`, `/tapmo-alternative`, `/blinq-alternative`, `/linktree-alternative-for-creators` |
| Blog-to-money-page click-through | % of blog readers who click through to a commercial parent page | All `/blog/...` pages |
| Category page conversion rate | % of category page visitors who create a profile | `/digital-business-card-india`, `/nfc-business-card-india`, `/qr-business-card` |
| Use-case page conversion rate | % of use-case visitors who create a profile | `/digital-business-card-for-doctors`, `/digital-business-card-for-real-estate-agents`, `/digital-business-card-for-freelancers`, `/digital-business-card-for-creators` |
| Keyword rankings by priority | Position tracking for P1 and P2 keywords | All execution master keywords |
| Backlink acquisition rate | New referring domains per month | Site-wide |

## Priority Keyword Groups to Track

### By Hub

#### Platform (homepage)
- smart identity platform
- identity management platform
- digital identity platform
- digital profile management system

#### Business Hub
Core category keywords:
- digital business card india (P1)
- nfc business card india (P1)
- qr business card (P1)
- business identity management platform (P1)
- ai review management (P2)
- google review management (P2)

Profession keywords:
- digital business card for doctors (P1)
- digital business card for real estate agents (P1)
- digital business card for freelancers (P1)

Comparison keywords:
- hihello alternative india (P1)
- popl alternative india (P1)
- tapmo alternative (P1)
- taponn alternative (P1)
- blinq alternative (P2)
- profiletap vs hihello (P2)
- profiletap vs tapmo (P2)

#### Creator Hub
- personal branding platform india (P2)
- digital business card for creators (P2)
- linktree alternative for creators (P2)

#### Family Safety Hub
- family safety profile (P3)
- emergency qr code (P2)

#### Pet Hub
- pet id tag qr code (P2)
- lost and found qr tag (P2)

#### Travel Hub
- travel qr code (P3)
- qr luggage tag (P3)

#### Vehicle Hub
- vehicle qr code (P3)
- vehicle qr code sticker (P2)

### By Wave

Launch wave keywords (7 families):
- smart identity platform
- business identity management platform
- personal branding platform india
- family safety profile
- pet id tag qr code
- travel qr code
- vehicle qr code

Post-launch Q1 keywords (8 families):
- digital business card india
- nfc business card india
- qr business card
- digital business card for creators
- hihello alternative india
- popl alternative india
- tapmo alternative
- taponn alternative

Post-launch Q2 keywords (12 families):
- digital business card for doctors
- digital business card for real estate agents
- digital business card for freelancers
- ai review management
- google review management
- blinq alternative
- profiletap vs hihello
- profiletap vs tapmo
- linktree alternative for creators
- emergency qr code
- lost and found qr tag
- vehicle qr code sticker

Later wave keywords (5 families):
- qr luggage tag
- nfc business card vs qr code
- paper business card vs digital business card
- best digital business card for doctors in india
- how to create a digital business card for your business

### By Priority Tier

P1 keywords requiring daily monitoring (13 families):
1. smart identity platform -> `/`
2. business identity management platform -> `/business-identity`
3. digital business card india -> `/digital-business-card-india`
4. nfc business card india -> `/nfc-business-card-india`
5. qr business card -> `/qr-business-card`
6. digital business card for doctors -> `/digital-business-card-for-doctors`
7. digital business card for real estate agents -> `/digital-business-card-for-real-estate-agents`
8. digital business card for freelancers -> `/digital-business-card-for-freelancers`
9. hihello alternative india -> `/hihello-alternative-india`
10. popl alternative india -> `/popl-alternative-india`
11. tapmo alternative -> `/tapmo-alternative`
12. taponn alternative -> `/taponn-alternative`

P2 keywords requiring weekly monitoring (13 families):
- personal branding platform india, digital business card for creators, linktree alternative for creators, pet id tag qr code, lost and found qr tag, emergency qr code, vehicle qr code sticker, ai review management, google review management, blinq alternative, profiletap vs hihello, profiletap vs tapmo

P3 keywords requiring monthly monitoring (7 families):
- family safety profile, travel qr code, vehicle qr code, qr luggage tag, nfc business card vs qr code, paper business card vs digital business card, best digital business card for doctors in india, how to create a digital business card for your business

## Reporting Structure

### Tier 1: Launch Core (monitor from day 1)
Pages to watch first:
- `/` -- homepage organic traffic and conversion
- `/business-identity` -- business hub traffic
- `/creator-identity` -- creator hub traffic
- `/family-safety-profile` -- family hub traffic
- `/pet-id-profile` -- pet hub traffic
- `/travel-profile` -- travel hub traffic
- `/vehicle-profile` -- vehicle hub traffic

Metrics: sessions, bounce rate, create_profile conversions, keyword rankings

### Tier 2: Launch Secondary (monitor from post_launch_q1)
- `/digital-business-card-india` -- highest-volume commercial page
- `/nfc-business-card-india` -- NFC category page
- `/qr-business-card` -- QR category page
- `/hihello-alternative-india` -- top comparison page
- `/popl-alternative-india`, `/tapmo-alternative`, `/taponn-alternative` -- comparison pages

Metrics: sessions, conversion rate, comparison page switch rate, keyword rankings

### Tier 3: Extended Pages (monitor from post_launch_q2)
- Profession use-case pages (doctors, real estate, freelancers, creators)
- Additional comparison pages (blinq, vs pages)
- Utility child pages (emergency qr, lost-and-found, vehicle sticker)

Metrics: sessions, conversion rate, keyword rankings, internal click-through

### Tier 4: Support Content (monitor monthly)
- All blog pages
- Blog-to-money-page click-through rate
- Blog keyword rankings
- Blog contribution to parent page authority

## India vs Global Traffic Segmentation

### Segmentation Rules
- Use Google Analytics geo filter to separate India vs non-India traffic
- India traffic is the primary success metric for all pages with `market=IN`
- Global traffic is a bonus metric, not the primary goal, for India-first pages
- Pages with `market=IN+GLOBAL` should track both segments separately

### India-Specific Metrics
- India organic sessions as % of total organic
- India conversion rate vs global conversion rate
- India keyword rankings (track in Google Search Console with country filter)
- India-specific comparison page performance (pages with `-india` suffix)

### Target Segmentation
- Launch phase: aim for 60%+ India organic traffic on IN-targeted pages
- Post-launch: monitor global traffic growth on IN+GLOBAL pages
- If India traffic drops below 50% on IN pages, investigate keyword targeting and content

## Baseline Targets

### Launch Wave Targets (first 90 days after launch)
- Homepage: 500+ organic sessions/month from India
- Business hub: 300+ organic sessions/month
- Other hubs: 50-100 organic sessions/month each
- Total organic: 1,000+ sessions/month
- create_profile conversions: 2-5% conversion rate on commercial pages

### Post-Launch Q1 Targets (90-180 days)
- Category pages: 200+ sessions/month each (digital business card india should lead)
- Comparison pages: 50-100 sessions/month each
- Total organic: 3,000+ sessions/month
- create_profile conversions: 3-5% on category pages, 5-8% on comparison pages

### Post-Launch Q2 Targets (180-360 days)
- Use-case pages: 100-200 sessions/month each
- Blog pages: 50-100 sessions/month each
- Total organic: 8,000+ sessions/month
- Blog-to-money-page CTR: 10-15%
- Backlink domains: 20+ referring domains

## Content Performance Scoring

### By Page Type

| Page Type | Primary Metric | Target | Secondary Metric |
| --- | --- | --- | --- |
| Homepage | Organic sessions | 500+/month | create_profile conversion rate > 3% |
| Solution hub | Organic sessions | 200+/month | create_profile conversion rate > 3% |
| Category | Organic sessions | 200+/month | create_profile conversion rate > 4% |
| Use case | Organic sessions | 100+/month | create_profile conversion rate > 5% |
| Comparison | Organic sessions | 50+/month | Switch rate (CTA click) > 8% |
| Blog | Organic sessions | 50+/month | Blog-to-money CTR > 10% |

### Content Health Scoring
- Green: meeting or exceeding targets
- Yellow: 50-99% of target
- Red: below 50% of target
- Gray: not yet published or insufficient data (less than 30 days)

### Refresh Triggers
- Keyword ranking drops 5+ positions for primary keyword
- Organic traffic declines 30%+ month-over-month
- Conversion rate drops below 50% of target
- Content is 6+ months old without update
- Competitor launches a competing page targeting the same keyword

## Backlink Acquisition Targets by Phase

| Phase | Target New Referring Domains | Focus |
| --- | --- | --- |
| Launch (0-90 days) | 5-8 | Founder story, homepage brand links |
| Post-launch Q1 (90-180 days) | 8-12 | Category page links, comparison roundups |
| Post-launch Q2 (180-360 days) | 12-20 | Use-case pages, guest posts, expert roundups |
| Ongoing (12+ months) | 5-10/quarter | Maintenance, new hubs, product catalog |

Current backlink prospect inventory: 12 qualified prospects across 6 target pages.

## Search Console Setup Recommendations

### Property Verification
- Verify both `profiletap.com` and `www.profiletap.com` (if applicable)
- Use domain-level verification for complete data
- Add India-specific property view for geo-filtered reporting

### URL Parameter Handling
- Configure URL parameters in Search Console to avoid duplicate content signals
- Exclude tracking parameters (utm_source, utm_medium, utm_campaign, etc.)
- Monitor for crawl errors on planned but not-yet-published pages

### Key Search Console Reports
- Performance by page: track impressions, clicks, CTR, position for each page_slug
- Performance by query: track primary and secondary keywords
- Coverage: monitor indexing status for all published pages
- Core Web Vitals: ensure all pages pass CWV thresholds

### Recommended Search Console Filters
- Country: India (primary view)
- Country: All countries (secondary view)
- Search type: Web (primary)
- Device: Mobile (India traffic is heavily mobile)

## Competitive Ranking Benchmarks

### Competitors to Track

| Competitor | Primary Keywords to Compare | Key Pages |
| --- | --- | --- |
| HiHello | digital business card, nfc business card, digital business card india | hihello.me |
| Popl | nfc business card, digital business card, popl card | popl.co |
| Blinq | digital business card, blinq card | blinq.me |
| TapMo | nfc business card india, digital business card india | tapmo.in |
| TapOnn | nfc business card india, digital visiting card | taponn.com |
| Linktree | link in bio, linktree alternative | linktr.ee |

### Competitive Tracking Cadence
- Weekly: check rankings for P1 keywords vs top 3 direct competitors
- Monthly: full competitive audit across all P1 and P2 keywords
- Quarterly: competitive content gap analysis, new competitor identification

### Target Competitive Position
- Launch phase: appear in top 20 for 50% of P1 keywords
- Post-launch Q1: appear in top 10 for 30% of P1 keywords
- Post-launch Q2: appear in top 5 for 20% of P1 keywords, top 10 for 50%
- 12 months: top 3 for "digital business card india" and "nfc business card india"

### India-Specific Competitive Advantage Metrics
- Track whether ProfileTap ranks above TapOnn and TapMo for India keywords
- Track whether ProfileTap appears in India SERPs for comparison keywords
- Monitor competitor new page launches for keyword overlap
- Track competitor backlink acquisition in India media

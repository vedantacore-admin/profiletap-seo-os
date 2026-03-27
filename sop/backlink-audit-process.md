# SOP: Backlink Audit Process

## Purpose

Qualify backlink prospects, score them systematically, manage outreach execution, and audit acquired links for quality.

---

## 1. Prospect Qualification

### Step 1: Source Prospects

| Source | Method |
|--------|--------|
| Competitor backlink analysis | Pull referring domains for HiHello, Popl, TapMo, TapOnn, Blinq via Ubersuggest/Ahrefs |
| Content-based search | Google: `"[keyword] resources"`, `"[keyword] tools list"`, `"write for us [niche]"` |
| HARO / Connectively | Monitor journalist requests in startup, tech, business categories |
| Industry directories | Identify relevant directories for digital tools, SaaS, NFC/QR |
| Event/conference sites | Find India tech events, startup conferences |

### Step 2: Score Each Prospect

Use the scoring matrix in `backlink_targets.csv`:

| Factor | Weight | Score 1-5 |
|--------|:---:|-----------|
| DA Score | 25% | 1: <20, 2: 20-35, 3: 35-50, 4: 50-70, 5: 70+ |
| Monthly Traffic | 15% | 1: <1K, 2: 1-10K, 3: 10-50K, 4: 50-200K, 5: 200K+ |
| Topical Relevance | 30% | 1: Unrelated, 2: Tangential, 3: Same industry, 4: Same niche, 5: Exact topic |
| Editorial Quality | 15% | 1: Spammy, 2: Low quality, 3: Average, 4: Good, 5: Premium |
| Link Placement Potential | 15% | 1: Footer, 2: Bio, 3: Resource section, 4: In-content, 5: Featured |

**Minimum qualifying score:** 3.0 weighted average
**Priority levels:** P1 (score > 4.0), P2 (3.5-4.0), P3 (3.0-3.5)

### Step 3: Record in CSV

Add qualified prospects to `data/backlinks/backlink_targets.csv` with:
- `domain`, `site_type`, `da_score`, `monthly_traffic`
- `target_page_slug` (which ProfileTap page we want the link to)
- `target_keyword`, `suggested_anchor`, `anchor_type`
- `target_market`, `link_angle`, `priority`, `status`

---

## 2. Outreach Angles (ProfileTap-Specific)

| Angle | Description | Best For | Example Pitch |
|-------|-------------|----------|--------------|
| `founder_story` | ProfileTap founding story, India market insight | Startup media (YourStory, Inc42) | "Building the identity layer for India's digital economy" |
| `data_backed_category` | Digital business card market growth, NFC adoption data | Business media (BusinessWorld) | "India's digital business card market: trends and growth" |
| `creator_marketing` | Creator economy trends, personal branding tools | Marketing media (Exchange4Media, SocialSamosa) | "How creators are replacing Linktree with identity platforms" |
| `comparison_roundup` | Alternative/comparison article contribution | Tech blogs, comparison sites | "Include ProfileTap in your digital business card roundup" |
| `expert_roundup` | Networking/branding expert quotes | Industry blogs | "Expert quote on professional networking trends in India" |
| `guest_post` | Original content for relevant publications | Any relevant publication | "I'd like to contribute an article on [topic] for your readers" |
| `resource_page` | Request inclusion on tools/resource lists | Resource aggregators | "ProfileTap would be a great addition to your digital tools list" |
| `doctor_networking` | Healthcare professional digital tools | Healthcare media (ExpressHealthcare) | "How doctors are adopting digital business cards in India" |
| `real_estate_branding` | Real estate agent digital tools | Real estate media (Housing.com) | "Digital identity tools for real estate professionals" |

---

## 3. Outreach Execution

### Step 1: Find Contact

For each qualified prospect:
1. Check the site's "Contact", "About", or "Write for Us" page
2. Find editor/journalist name and email
3. Verify email (use Hunter.io or similar)
4. Record in `data/backlinks/outreach_tracker.csv`

### Step 2: Send Initial Pitch

Use angle-appropriate template. Key rules:
- Reference specific content on their site (show you've read it)
- Explain value for their audience (not for you)
- Don't ask for a link in the first email
- Keep under 150 words
- Personalize every email (no mass templates)

### Step 3: Follow-Up Sequence

| Day | Action |
|:---:|--------|
| 0 | Initial pitch sent → `status=contacted` |
| 3 | Follow-up 1 (brief, value-focused) → `status=follow_up_1` |
| 7 | Follow-up 2 (new angle or additional value) → `status=follow_up_2` |
| 14 | Break-up email (polite close) → `status=break_up` |

### Step 4: Track Outcomes

Update `outreach_tracker.csv`:
- `outcome`: won, rejected, no_response, pending
- `live_url`: URL where the link appears (if won)
- Document what worked/didn't work in `notes`

---

## 4. Monthly Backlink Audit

**When:** Last week of each month
**Time:** 1-2 hours

### New Links Review

1. Pull new referring domains from Search Console (Links report) or Ahrefs
2. For each new link:
   - Is it from a legitimate site? (Check for spam signals)
   - Is the anchor text appropriate? (Check against our anchor text strategy)
   - Is the link follow or nofollow?
   - Which page does it point to?
3. Flag any suspicious links for potential disavow

### Pipeline Status Review

1. Review `outreach_tracker.csv`:
   - How many prospects contacted this month?
   - What's the response rate?
   - What's the conversion rate (links won / emails sent)?
2. Review `backlink_targets.csv`:
   - How many prospects remain in pipeline?
   - Do we need to source more prospects?
   - Are we covering all hubs (not just business)?

### Toxic Link Detection

Check for:
- Links from DA < 10 sites with no organic traffic
- Links from unrelated foreign-language sites with spammy anchors
- Sudden batches of links from the same network
- Links from known PBNs or link farms

If toxic links found → add to disavow file and submit via Search Console.

---

## 5. Anchor Text Audit

**When:** Quarterly (during keyword refresh cycle)

1. Export all backlinks with anchor text
2. Calculate anchor text distribution:
   - Branded: target 30-40%
   - Partial match: target 20-25%
   - Exact match: target 5-10%
   - Naked URL: target 10-15%
   - Generic/contextual: target 15-20%
3. If any category is significantly over/under target:
   - Adjust future outreach anchor suggestions
   - For guest posts, specifically request anchor type needed for balance

---

## 6. Prospect Pipeline Targets

| Phase | Minimum Prospects in Pipeline | Target Links/Month |
|-------|:---:|:---:|
| Launch (first 3 months) | 40 | 5-8 |
| Growth (months 4-12) | 60 | 8-15 |
| Maintenance (12+ months) | 30 | 5-10 |

### Hub Coverage Target

Ensure prospects cover all hubs, not just business:

| Hub | Min Prospects | Example Targets |
|-----|:---:|----------------|
| Platform / Homepage | 5 | Startup media, tech press |
| Business | 15 | Business media, SaaS directories |
| Creator | 5 | Marketing blogs, creator tool lists |
| Family Safety | 3 | Parenting blogs, safety publications |
| Pet | 3 | Pet blogs, veterinary publications |
| Travel | 3 | Travel blogs, travel tech sites |
| Vehicle | 3 | Automotive blogs, parking solution sites |

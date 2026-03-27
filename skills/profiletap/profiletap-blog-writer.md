# ProfileTap Blog Writer — Full Draft Generation

> Claude Code Skill: Generate complete, publish-ready blog drafts for ProfileTap pages.
> References: `skills/general-seo/blog-writer.md` for structure, this file for ProfileTap-specific voice, features, and domain rules.

---

## How to Use

Invoke with a page_slug:

```
/profiletap-blog-writer /blog/parking-contact-qr-code-guide
```

Or with a brief already in context:

```
/profiletap-blog-writer [paste brief or reference brief file]
```

---

## Step 1: Load Context

Before writing, read these files:

1. `data/pages/page_master.csv` — get page_type, hub, feature_set, parent_page_slug, primary_keyword
2. `data/keywords/execution_seo_master.csv` — get secondary_keywords, search_intent, funnel_stage, market
3. `data/content/content_calendar.csv` — get content_role, cluster_name, primary_internal_link_target, secondary_internal_link_targets
4. Check if a brief exists in `briefs/` for this page_slug

If no brief exists, generate one first using `/profiletap-brief` before writing.

---

## Step 2: Determine Blog Parameters

From the CSV data, determine:

| Parameter | Source |
|---|---|
| Primary keyword | execution_seo_master.csv → primary_keyword |
| Secondary keywords | execution_seo_master.csv → secondary_keywords |
| Content role | content_calendar.csv → content_role |
| Hub | page_master.csv → hub |
| Feature set | page_master.csv → feature_set (translate tokens to labels) |
| Parent money page | content_calendar.csv → primary_internal_link_target |
| Secondary link targets | content_calendar.csv → secondary_internal_link_targets |
| Target market | page_master.csv → target_market |
| Funnel stage | execution_seo_master.csv → funnel_stage |

---

## Step 3: Apply ProfileTap Voice Rules

### Brand Positioning
- ProfileTap is a **smart identity management platform** — not just an NFC card company
- Frame every blog around **identity**, **smart profiles**, and **digital-first workflows**
- India-first perspective for IN market pages; global framing for IN+GLOBAL pages

### Tone
- Professional but approachable — like a knowledgeable friend, not a corporate brochure
- Direct and actionable — every section should help the reader do something
- Confident without being salesy — show expertise through specifics, not superlatives
- India-market content: use Indian business context (GST, UPI, Indian cities, local business culture)

### What to Avoid
- Never position ProfileTap as "just" an NFC card or digital business card
- Never use "In today's digital world..." or similar generic openings
- Never mention competitor names outside of comparison pages
- Never expose raw feature tokens (write "QR sharing" not `qr_sharing`)
- Never claim features ProfileTap doesn't have
- Never frame safety/emergency features as trivial or gimmicky

---

## Step 4: Feature Translation Table

When the brief's feature_set includes these tokens, use the human labels in copy:

| Token | In Blog Copy | Example Usage |
|---|---|---|
| `digital_profiles` | digital profiles | "Create digital profiles that work across every touchpoint" |
| `nfc_sharing` | NFC sharing / tap-to-share | "Share your profile with a single tap using NFC sharing" |
| `qr_sharing` | QR code sharing | "Scan the QR code to instantly access the full profile" |
| `ai_review_assist` | AI-powered review tools | "Collect and manage reviews with AI-powered review tools" |
| `business_ai` | Business AI tools | "Use ProfileTap Business AI to automate tasks and get smart insights" |
| `analytics` | profile analytics | "Track who viewed your profile and when with built-in analytics" |
| `account_collaborators` | team collaboration | "Add collaborators to manage your business profiles together" |
| `multi_account_team_management` | multi-account management | "Manage multiple business accounts from one dashboard" |
| `multi_profile_type_profiles` | multi-type profiles | "Create different profiles for different needs — business, personal, pet, vehicle" |
| `call_masking` | call privacy / call masking | "Keep your personal number private with call masking" |
| `whatsapp_masking` | WhatsApp privacy | "Share WhatsApp access without exposing your real number" |
| `theme_library` | customizable themes | "Choose from a wide range of themes to match your brand" |
| `advanced_creator_analytics` | creator analytics | "Track follower engagement and link clicks with creator analytics" |

### Feature Mention Rules
- Only mention features listed in the page's `feature_set` — never all 12
- Weave features into the narrative naturally — don't list dump
- Show the benefit, not just the feature name: "call masking keeps your personal number private" > "ProfileTap has call masking"
- For plan-sensitive features (check `pricing_visibility`), mention the feature exists without making false promises about free access

---

## Step 5: Hub-Specific Writing Angles

### Business Hub
- Emphasis: professional networking, client acquisition, team management, review collection
- Audience: Indian SMBs, freelancers, professionals, sales teams
- Proof points: NFC + QR dual sharing, team management, AI review tools
- India angle: reference Indian business practices, cities, industries

### Creator Hub
- Emphasis: personal branding, link-in-bio replacement, audience engagement, analytics
- Audience: influencers, YouTubers, bloggers, freelance creators
- Proof points: multi-profile types, creator analytics, theme customization
- Tone: slightly more energetic, creator-community language

### Family Safety Hub
- Emphasis: child safety, emergency access, privacy-first sharing
- Audience: parents, caregivers, schools
- Proof points: QR emergency profiles, call/WhatsApp masking for privacy
- Tone: serious and trustworthy — safety content demands authority
- NEVER trivialize safety features or use casual language about emergencies

### Pet Hub
- Emphasis: pet identification, lost pet recovery, quick contact for finders
- Audience: pet owners, veterinary practices, pet communities
- Proof points: QR pet profiles, multi-profile types (multiple pets), instant contact
- Tone: warm and relatable — pet owners care deeply about their animals

### Travel Hub
- Emphasis: travel safety, luggage tracking, emergency contact abroad
- Audience: frequent travelers, backpackers, families traveling with kids
- Proof points: QR profiles for luggage, emergency medical info, call masking abroad
- Tone: practical and safety-conscious

### Vehicle Hub
- Emphasis: parking contact, emergency info, vehicle identification
- Audience: car/bike owners, fleet managers, parking-hassle sufferers
- Proof points: QR stickers, call masking for privacy, instant contact
- India angle: wrong-parking culture in Indian cities, two-wheeler ownership

---

## Step 6: Internal Linking Strategy for Blogs

### Mandatory Links
1. **Parent money page** — link within the first 300 words using a contextual anchor
2. **Hub page** — link once in a relevant context
3. **Related blog in same cluster** — link once if another published blog exists in the same cluster

### Anchor Text Rules
- Use descriptive anchors: "digital business card for doctors" not "click here"
- Mix anchor types: 40% partial-match, 30% contextual, 20% branded, 10% exact
- Never use the same anchor text twice in one post
- For parent money page: use the primary keyword of that page as anchor (or close variant)

### Link Placement
- First link: within first 300 words → to parent money page
- Mid-content link: around the 50% mark → to hub page or related category
- Pre-CTA link: just before CTA block → to the conversion page
- FAQ links: link relevant answers to related pages

---

## Step 7: CTA Patterns by Hub

### Business Hub CTAs
- Primary: "Create your free digital business card" / "Build your business profile"
- Secondary: "See how ProfileTap works for [profession]"

### Creator Hub CTAs
- Primary: "Create your creator profile" / "Build your link-in-bio page"
- Secondary: "See how creators use ProfileTap"

### Family Safety Hub CTAs
- Primary: "Create a safety profile for your family"
- Secondary: "Learn how emergency QR profiles work"

### Pet Hub CTAs
- Primary: "Create a pet ID profile" / "Get your pet's QR tag"
- Secondary: "See how pet QR tags work"

### Travel Hub CTAs
- Primary: "Create your travel safety profile"
- Secondary: "See how QR luggage tags work"

### Vehicle Hub CTAs
- Primary: "Create your vehicle QR profile"
- Secondary: "Get your parking contact QR sticker"

---

## Step 8: Draft Output Format

Generate the full draft in this order:

```markdown
---
title_tag: "{Primary Keyword}: {Angle} | ProfileTap"
meta_description: "{155 chars max with primary keyword}"
url: "{page_slug}"
primary_keyword: "{keyword}"
word_count: "{target}"
content_role: "{role}"
hub: "{hub}"
schema: "{Article, FAQPage, BreadcrumbList, HowTo — as applicable}"
---

# {H1 — contains primary keyword}

{Opening — 2-3 sentences, problem-first, keyword in first 100 words}

<!-- IMAGE: Hero image | Alt: {alt text} | File: profiletap-{slug}-hero.webp -->

## {H2 Section 1 — secondary keyword if natural}

{Body content — 200-400 words}

[Internal link to parent money page with descriptive anchor]

## {H2 Section 2}

{Body content}

<!-- IMAGE: {description} | Alt: {alt text} | File: profiletap-{slug}-{desc}.webp -->

## {H2 Section 3}

{Body content}

## {Action CTA H2}

{2-3 sentences connecting topic to ProfileTap}
{Primary CTA}
{Secondary CTA}

## Frequently Asked Questions

### {Q1}
{A1 — direct answer first sentence}

### {Q2}
{A2}

### {Q3}
{A3}

## {Wrap-up H2}

{2-3 sentence summary + final CTA mention}

<!-- SCHEMA: Article -->
<!-- Headline: {H1} -->
<!-- Description: {meta description} -->
<!-- Author: ProfileTap Team -->
<!-- DatePublished: TBD -->

<!-- SCHEMA: FAQPage -->
<!-- Q1: {q} | A1: {a} -->
<!-- Q2: {q} | A2: {a} -->
<!-- Q3: {q} | A3: {a} -->

<!-- SCHEMA: BreadcrumbList -->
<!-- Home > {Hub Name} > {Blog Title} -->
```

---

## Step 9: Post-Draft Checklist

After generating the draft, verify:

- [ ] H1 contains primary keyword exactly or as close variant
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in at least one H2
- [ ] Each H2 targets a unique angle (no overlapping sections)
- [ ] Feature tokens translated to human labels (no raw tokens in output)
- [ ] Only features from page's feature_set mentioned
- [ ] Parent money page linked within first 300 words
- [ ] At least 1 internal link per 500 words
- [ ] CTA block present with hub-appropriate CTA
- [ ] FAQ section with 3-5 questions (if FAQPage schema required)
- [ ] Image placeholders present (minimum 2)
- [ ] Schema markup notes at end
- [ ] Meta description under 155 characters
- [ ] Title tag under 60 characters
- [ ] India-specific context included (for IN market pages)
- [ ] ProfileTap positioned as smart identity platform, not just NFC cards
- [ ] Word count within target range for the content role
- [ ] No generic filler openings or conclusions

---

## Step 10: Save and Update Tracking

After the draft is accepted:

1. Save the draft to `briefs/{page_slug}-draft.md` (or the agreed location)
2. Update `data/content/content_calendar.csv`:
   - `status` → `in_progress`
   - `brief_status` → `draft_ready`
3. Note any images that need to be created/sourced

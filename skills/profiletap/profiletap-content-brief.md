# ProfileTap Content Brief Generation

## Pre-Brief Checklist

Before writing any content brief, read these files:

1. `data/keywords/execution_seo_master.csv` -- confirm the keyword family and page mapping
2. `data/pages/page_master.csv` -- confirm page architecture, hub, feature_set, and status
3. `data/content/content_calendar.csv` -- confirm content_id, content_role, cluster, and parent relationships
4. `data/keywords/raw_keyword_bank.csv` -- check secondary keywords and variant coverage
5. `data/backlinks/backlink_targets.csv` -- check if backlink targets exist for the page (optional)

Verify before writing:
- The page_slug exists in page_master.csv
- The keyword family exists in execution_seo_master.csv
- The content task exists in content_calendar.csv
- No other page targets the same primary keyword

## Brief Generation Process

### Step 1: Identify the page
Look up the `page_slug` in all three CSVs. Confirm `page_type`, `hub`, `feature_set`, `primary_keyword`, `publish_wave`, and `priority`.

### Step 2: Gather keyword context
From execution_seo_master.csv: primary_keyword, secondary_keywords, search_intent, funnel_stage, market.
From raw_keyword_bank.csv: all `keep_secondary` rows for this canonical family.

### Step 3: Determine content angle
Use the hub and page_type to select the content angle (see Hub-Specific Content Angles below).

### Step 4: Translate feature tokens
Convert all `feature_set` tokens to human-facing labels using the translation table below.

### Step 5: Build the brief structure
Use the page-type-specific structure (see Recommended Structure by Page Type below).

### Step 6: Set internal linking targets
From content_calendar.csv: `primary_internal_link_target` and `secondary_internal_link_targets`.
From page_master.csv: `parent_page_slug` and sibling pages in the same hub.

### Step 7: Quality check
Run through the Quality Bar checklist at the end of this document.

## Feature Token to Human Label Translation Table

Always translate tokens before they appear in any brief or page copy.

| Token | Human Label |
| --- | --- |
| `digital_profiles` | Digital profiles |
| `nfc_sharing` | NFC sharing |
| `qr_sharing` | QR sharing |
| `ai_review_assist` | AI review assist |
| `analytics` | Analytics |
| `account_collaborators` | Manage account collaborators |
| `multi_account_team_management` | Manage multiple accounts / teams |
| `multi_profile_type_profiles` | Multi-profile / multi-type profiles |
| `call_masking` | Call masking |
| `whatsapp_masking` | WhatsApp masking |
| `theme_library` | Wide range of themes |
| `advanced_creator_analytics` | Advanced analytics for creators |

## Hub-Specific Content Angles

### Business Hub
Primary angles: professional networking, team management, client impressions, business growth
- Lead with professional credibility and first-impression impact
- Emphasize NFC + QR sharing for networking events, meetings, client visits
- Highlight AI review assist for reputation management
- Team management and collaborator features for organizations
- Call and WhatsApp masking for professional privacy
- India-specific: reference Indian business culture, networking events, industry conferences
- Relevant professions: doctors, real estate agents, freelancers
- Key competitor comparisons: HiHello, Popl, TapOnn, TapMo, Blinq

### Creator Hub
Primary angles: personal branding, audience growth, link-in-bio replacement, content monetization
- Lead with personal brand as a professional asset
- Position ProfileTap as a full identity platform, not just a link page
- Emphasize multi-profile types for separating brand from personal identity
- Advanced creator analytics for tracking engagement
- NFC cards at events, meetups, brand collaborations
- India-specific: reference Indian creator economy, YouTube India, Instagram India
- Key competitor: Linktree (link-in-bio replacement angle)

### Family Safety Hub
Primary angles: child protection, emergency access, school safety, caregiver communication
- Lead with safety and peace of mind for parents
- QR profiles for children's school bags, name tags, emergency identification
- Call masking and WhatsApp masking for protecting children's privacy
- Multi-profile types for different family members
- Emergency contact access via QR scan
- India-specific: reference Indian school systems, family safety concerns in urban India

### Pet Hub
Primary angles: pet recovery, pet identification, lost pet prevention
- Lead with the emotional angle of pet safety and reunion
- QR tags for pet collars, harnesses, and carriers
- Digital pet profiles with owner contact, vet info, medical history
- Lost-and-found QR system for quick identification
- Minimal feature set: digital profiles, QR, multi-profile types, themes
- India-specific: reference growing pet ownership in Indian cities

### Travel Hub
Primary angles: travel safety, emergency contacts abroad, luggage recovery
- Lead with safety and preparedness for travelers
- QR luggage tags for lost luggage recovery
- Emergency contact profiles accessible via QR scan
- Call and WhatsApp masking for privacy while traveling
- Digital travel profiles with medical info, emergency contacts, insurance details
- India-specific: reference Indian travelers abroad, domestic travel

### Vehicle Hub
Primary angles: parking contact, wrong parking resolution, emergency access
- Lead with convenience and safety for vehicle owners
- QR code stickers for windshields, dashboards, bikes
- Owner contact via QR scan without exposing phone number (call masking)
- Emergency contact access in case of accidents
- Wrong parking notification system
- India-specific: reference Indian parking challenges, urban vehicle density

## India-First Messaging Rules

When to emphasize India market:
- Pages with `market=IN`: Lead with India context, use INR, reference Indian businesses/cities
- Pages with `market=IN+GLOBAL`: Lead with universal value, add India proof points
- Comparison pages with `-india` suffix: Explicitly position for Indian users switching from global tools
- Blog pages: Match the parent page's market positioning

India-specific language guidelines:
- Use "visiting card" as a secondary term (Indians commonly use this phrase)
- Reference Indian networking culture (business card exchange at meetings is common)
- Mention Indian cities only in natural context, never as keyword stuffing
- Use INR pricing context on India-targeted pages
- Reference Indian professions naturally (doctors, real estate agents are strong in India)

## Comparison Page Structure

Every comparison page must include:

### 1. Alternative Framing Section
- Why users are looking for alternatives to {competitor}
- What {competitor} lacks that ProfileTap provides
- India-specific context if the page targets IN market

### 2. Feature Comparison Table
Build from the page's `feature_set`. Typical columns:

| Feature | ProfileTap | {Competitor} |
| --- | --- | --- |
| Digital profiles | Yes | Limited / Yes / No |
| NFC sharing | Yes | {varies} |
| QR sharing | Yes | {varies} |
| AI review assist | Yes | No |
| Call masking | Yes | No |
| WhatsApp masking | Yes | No |
| Multi-profile types | Yes | No |
| Team management | Yes | Limited |
| India pricing | INR plans | USD only |

### 3. Reasons to Switch
- 3-5 specific reasons with feature proof
- India market advantage where applicable
- Pricing advantage (if applicable)

### 4. FAQ Section
- "Is ProfileTap better than {competitor}?"
- "Can I import my {competitor} contacts to ProfileTap?"
- "Does ProfileTap work in India?"
- "What does ProfileTap cost compared to {competitor}?"

### 5. Switch CTA
- Primary: "Create your free ProfileTap profile"
- Secondary: "Compare plans" or "See how ProfileTap works"

## Blog Cluster Parent-Child Rules

Every blog must:
- Have one `parent_page_slug` (the commercial page it supports)
- Have one `parent_keyword_family` (the keyword family it strengthens)
- Link back to the parent page as its primary internal link target
- Use `content_role` to define its job (definition, how_to, comparison, examples, use_case_support)

Current blog-to-parent mappings:
- `/blog/nfc-business-card-vs-qr-code` -> parent: `/nfc-business-card-india`, role: comparison
- `/blog/paper-vs-digital-business-card` -> parent: `/digital-business-card-india`, role: comparison
- `/blog/best-digital-business-card-for-doctors-india` -> parent: `/digital-business-card-for-doctors`, role: use_case_support
- `/blog/how-to-create-digital-business-card` -> parent: `/digital-business-card-india`, role: how_to

Cluster sizing targets:
- Business clusters: 12-18 blogs total across all business parent pages
- Creator clusters: 6-10 blogs
- Other hubs: 3-6 blogs each

## Schema Markup Requirements by Page Type

| Page Type | Required Schema |
| --- | --- |
| `homepage` | Organization, WebSite, SiteNavigationElement |
| `solution_hub` | WebPage, BreadcrumbList, FAQPage (if FAQ present) |
| `category` | WebPage, BreadcrumbList, Product (if product features shown), FAQPage |
| `use_case` | WebPage, BreadcrumbList, FAQPage |
| `comparison` | WebPage, BreadcrumbList, FAQPage (recommended) |
| `blog` | Article, BreadcrumbList, FAQPage (if FAQ present) |
| `product_family` (future) | Product, BreadcrumbList, Offer, AggregateRating |

## Internal Linking Targets from Page Inventory

When building internal links for a page, use these priorities:

1. Parent page (from `parent_page_slug` in page_master.csv)
2. Sibling pages in the same hub
3. Related comparison pages for the same hub
4. Supporting blog posts that target the same cluster
5. Homepage (for all pages)

Example internal linking map for `/digital-business-card-india`:
- Up: `/business-identity` (parent hub)
- Siblings: `/nfc-business-card-india`, `/qr-business-card`
- Comparisons: `/hihello-alternative-india`, `/popl-alternative-india`
- Blogs: `/blog/paper-vs-digital-business-card`, `/blog/how-to-create-digital-business-card`
- Use cases: `/digital-business-card-for-doctors`, `/digital-business-card-for-freelancers`

## Quality Bar and Anti-Patterns

### Quality Requirements
- Brief must reference the actual primary keyword from execution_seo_master.csv
- Brief must include only the feature_set defined for that page (not the full 12)
- Brief must specify the conversion goal (from page_master.csv `conversion_goal`)
- Brief must include at least 2 internal link targets
- Brief must translate all feature tokens to human labels
- Brief must align with the page's funnel stage (TOFU, MOFU, BOFU)

### Anti-Patterns to Avoid
- Generic content that could apply to any digital business card platform
- Standalone feature pitches disconnected from the page's audience
- Mentioning all 12 features on a page that only has 4-6 in its feature_set
- Using raw feature tokens like `multi_profile_type_profiles` in copy
- Creating content that targets a second primary intent on the same page
- Writing comparison content on category pages (comparison intent belongs on comparison pages)
- Blog content that does not link back to its parent commercial page
- India-market pages that do not reference Indian context at all
- Feature-focused content when the page intent is audience-focused (e.g., doctors page should lead with doctor pain points, not feature lists)
- Using "just an NFC card" or "digital visiting card maker" as the primary framing

### Mandatory Brief Sections
1. Brief Metadata (from CSVs)
2. Search Context (target market, audience, searcher problem)
3. Product Angle (positioning, features, proof points)
4. SEO Requirements (title tag, H1, meta description, URL)
5. Content Goal (business outcome this page must achieve)
6. Recommended Structure (section-by-section outline)
7. Internal Linking (primary and secondary targets)
8. CTA (primary and secondary)
9. Notes For Writer (tone, framing, anti-patterns)

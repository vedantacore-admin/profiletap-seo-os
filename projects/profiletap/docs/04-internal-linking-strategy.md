# Internal Linking Strategy — ProfileTap

## Purpose

Define the internal linking structure that distributes link equity from the homepage through hubs to child pages, supports topical authority, and guides users toward conversion.

---

## 1. Link Equity Flow Model

```
Homepage (/)
  ├── Business Hub (/business-identity)
  │     ├── Categories: /digital-business-card-india, /nfc-business-card-india, /qr-business-card, /ai-review-assist, /google-review-management
  │     ├── Use Cases: /digital-business-card-for-doctors, /...-real-estate-agents, /...-freelancers
  │     ├── Comparisons: /hihello-alternative-india, /popl-alternative-india, /tapmo-alternative, /taponn-alternative, /blinq-alternative, /profiletap-vs-hihello, /profiletap-vs-tapmo
  │     └── Blogs: /blog/nfc-business-card-vs-qr-code, /blog/paper-vs-digital-business-card, etc.
  ├── Creator Hub (/creator-identity)
  │     ├── Use Cases: /digital-business-card-for-creators
  │     ├── Comparisons: /linktree-alternative-for-creators
  │     └── Blogs: (planned)
  ├── Family Safety Hub (/family-safety-profile)
  │     ├── Categories: /emergency-qr-code
  │     └── Blogs: (planned)
  ├── Pet Hub (/pet-id-profile)
  │     ├── Categories: /lost-and-found-qr-tag
  │     └── Blogs: (planned)
  ├── Travel Hub (/travel-profile)
  │     ├── Categories: /qr-luggage-tag
  │     └── Blogs: (planned)
  └── Vehicle Hub (/vehicle-profile)
        ├── Categories: /vehicle-qr-code-sticker
        └── Blogs: (planned)
```

**Flow direction:** Homepage → Hubs → Categories/Use Cases → Blogs (and back up via breadcrumbs + contextual links).

---

## 2. Linking Rules by Page Type

### Homepage → Hubs
- Link to ALL 6 solution hubs from the homepage
- Use hub-specific anchor text: "Business Identity", "Creator Identity", etc.
- Place in both navigation and body content
- Each hub link should appear at least twice on homepage (nav + body section)

### Hub → Children
- Each hub page links to ALL its direct children (categories, use cases, comparisons)
- Use primary keyword or descriptive anchor text (not "click here")
- Place in a structured section (e.g., "Solutions", "For Professionals", "Compare")
- Hub should also link back to homepage

### Category/Use Case → Hub (upward)
- Every category and use case page links back to its parent hub
- Use breadcrumb navigation: `Home > {Hub} > {Current Page}`
- Also include a contextual link in body content

### Category/Use Case → Siblings (lateral)
- Category pages link to related categories within the same hub
- Use case pages link to the parent category AND other use cases
- Example: `/digital-business-card-for-doctors` links to `/digital-business-card-india` and `/digital-business-card-for-real-estate-agents`

### Comparison → Category + Hub
- Every comparison page links to:
  - Its parent hub
  - The most relevant category page (the "switch to" landing page)
  - The sign-up/trial page (CTA)
- Example: `/hihello-alternative-india` links to `/business-identity`, `/digital-business-card-india`

### Blog → Money Pages (upward)
- Every blog post links to its `primary_internal_link_target` (from content_calendar.csv)
- Also links to `secondary_internal_link_targets`
- Place the primary link early in the content (first 200 words)
- Use keyword-rich anchor text for the primary target

### Blog → Blog (lateral)
- Blog posts within the same cluster link to each other
- Use contextual anchor text, not "related posts" widgets
- Limit to 2-3 intra-cluster links per post

### Cross-Hub Linking
- Hubs do NOT link to each other by default (to preserve topical focus)
- Exception: when a feature spans hubs (e.g., QR sharing is relevant to both pet and vehicle), a brief contextual mention with link is acceptable
- Homepage serves as the cross-hub connector

---

## 3. Anchor Text Guidelines

### Types and Target Ratios

| Anchor Type | Target Ratio | Example |
|-------------|:---:|---------|
| Exact match keyword | 15-20% | "digital business card india" |
| Partial match / variation | 30-35% | "digital business cards", "business card solution" |
| Branded | 15-20% | "ProfileTap", "ProfileTap for Business" |
| Descriptive / contextual | 20-25% | "explore our business identity platform", "learn more" |
| Naked URL | 5-10% | "profiletap.com/business-identity" |

### Rules

- Never use the same exact-match anchor text for two different target pages
- Vary anchor text across the site (don't always use the same phrase for the same target)
- Blog posts should primarily use partial-match and descriptive anchors
- Comparison pages can use competitor names as anchors when linking to comparison pages
- Never use "click here" or "read more" as the sole anchor text (combine with context)

---

## 4. Navigation and Footer Links

### Primary Navigation

```
Home | Business | Creator | Family Safety | Pet | Travel | Vehicle | Blog | Pricing
```

- All 6 hubs visible in main nav
- Blog and Pricing as top-level nav items
- Mobile: hamburger menu with same structure

### Footer Links

```
Platform
  - About ProfileTap
  - Pricing
  - Contact

Solutions
  - Business Identity
  - Creator Identity
  - Family Safety
  - Pet ID
  - Travel Profile
  - Vehicle Profile

Resources
  - Blog
  - Help Center
  - API Docs

Legal
  - Privacy Policy
  - Terms of Service
```

### Breadcrumbs

- Present on ALL pages except homepage
- Format: `Home > {Hub} > {Page Title}`
- Breadcrumbs match BreadcrumbList schema markup
- Each breadcrumb segment is a clickable link

---

## 5. Sidebar / Related Content

### Hub Pages
- Sidebar: list of child pages (categories, use cases, comparisons)
- "Popular" badge on P1 pages

### Category / Use Case Pages
- Sidebar: related pages within the same hub
- "Compare" section linking to relevant comparison pages
- CTA block linking to sign-up

### Blog Posts
- Sidebar: parent money page CTA
- "Related Posts" section (2-3 posts from same cluster)
- In-content CTA linking to parent money page

### Comparison Pages
- No sidebar (full-width for comparison table)
- Bottom: "More Comparisons" linking to sibling comparison pages

---

## 6. Internal Link Audit Checklist

Run monthly:

- [ ] Every page has at least 3 internal links pointing to it
- [ ] Every page links to at least 2 other pages
- [ ] No orphan pages (pages with zero internal links)
- [ ] Breadcrumbs present and functional on all non-homepage pages
- [ ] All hub pages linked from homepage
- [ ] All child pages linked from their parent hub
- [ ] All blog posts link to their designated money page
- [ ] No broken internal links (404s)
- [ ] Anchor text varies across links to the same target
- [ ] Cross-hub links are minimal and intentional

---

## 7. Link Priority Matrix

When a page needs more link equity (e.g., not ranking well), increase internal links using this priority:

| Source Priority | Source Type | Why |
|:---:|-----------|-----|
| 1 | Homepage | Highest authority page |
| 2 | Parent hub page | Direct topical relevance + authority |
| 3 | Sibling pages (same hub) | Topical cluster reinforcement |
| 4 | Blog posts in same cluster | Content authority flow |
| 5 | Footer / sitewide links | Broad but diluted equity |

### How to boost a page

1. Add a contextual link from its parent hub (if not already present)
2. Add contextual links from 2-3 sibling pages
3. Create a supporting blog post that links to it as the primary target
4. Add it to the homepage "Featured" section (temporarily or permanently)

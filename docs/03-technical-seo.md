# Technical SEO Plan — ProfileTap

## Purpose

Define the technical SEO foundation for all ProfileTap pages: schema markup, meta tag formulas, canonical rules, sitemap structure, Core Web Vitals targets, and multi-market handling.

---

## 1. Meta Tag Formulas

### Title Tag Templates (max 60 characters)

| Page Type | Formula | Example |
|-----------|---------|---------|
| Homepage | `{Brand} — {Positioning}` | `ProfileTap — Smart Identity Management Platform` |
| Solution Hub | `{Hub Title} \| ProfileTap` | `Business Identity Platform \| ProfileTap` |
| Category | `{Primary Keyword} \| ProfileTap` | `Digital Business Card India \| ProfileTap` |
| Use Case | `{Primary Keyword} \| ProfileTap` | `Digital Business Card for Doctors \| ProfileTap` |
| Comparison | `{Competitor} Alternative in India \| ProfileTap` | `HiHello Alternative in India \| ProfileTap` |
| Blog | `{Post Title} \| ProfileTap Blog` | `NFC vs QR Business Card: Which Converts Better? \| ProfileTap Blog` |
| Product Family | `{Product Name} \| ProfileTap Store` | `Metal Business Cards \| ProfileTap Store` |

### Meta Description Templates (max 155 characters)

| Page Type | Formula |
|-----------|---------|
| Homepage | `{Brand} is a {positioning}. {Key benefit}. {CTA}.` |
| Solution Hub | `{Hub positioning}. Features: {top 3 features}. {CTA}.` |
| Category | `{Primary keyword} with {key differentiator}. {Benefit}. {CTA}.` |
| Use Case | `{Primary keyword} designed for {audience}. {Key benefit}. {CTA}.` |
| Comparison | `Looking for a {competitor} alternative? {Key differentiator}. {CTA}.` |
| Blog | `{Question or hook}. {Brief answer}. Read the full guide.` |

### H1 Rules

- Every page has exactly ONE H1
- H1 must contain the primary keyword (exact or close variant)
- H1 ≠ title tag (H1 can be longer and more descriptive)
- Homepage H1: brand positioning statement
- Hub H1: hub-specific value proposition
- Category/Use Case H1: primary keyword + benefit
- Comparison H1: "{Brand} vs {Competitor}" or "Best {Competitor} Alternative"
- Blog H1: question or declarative statement matching search intent

---

## 2. URL Structure

### Rules

- All lowercase, hyphens only (no underscores, no trailing slashes)
- No date-based URLs for evergreen content
- Maximum 3 levels deep: `/{hub-child}` or `/blog/{post-slug}`
- Canonical URL = self-referencing on every page
- No URL parameters for content pages (reserved for app/tracking)

### Hierarchy

```
/                                          → homepage
/business-identity                         → solution hub
  /digital-business-card-india             → category (child of business)
  /digital-business-card-for-doctors       → use case (child of business)
  /hihello-alternative-india               → comparison (child of business)
/creator-identity                          → solution hub
  /digital-business-card-for-creators      → use case (child of creator)
  /linktree-alternative-for-creators       → comparison (child of creator)
/family-safety-profile                     → solution hub
  /emergency-qr-code                       → category (child of family)
/pet-id-profile                            → solution hub
  /lost-and-found-qr-tag                   → category (child of pet)
/travel-profile                            → solution hub
  /qr-luggage-tag                          → category (child of travel)
/vehicle-profile                           → solution hub
  /vehicle-qr-code-sticker                 → category (child of vehicle)
/blog/{post-slug}                          → blog posts
/products/{product-slug}                   → product family (future)
```

---

## 3. Canonical URL Rules

- Every page includes `<link rel="canonical" href="{self-URL}" />`
- No `www` vs non-`www` conflicts — pick one and redirect the other
- HTTPS enforced everywhere — HTTP → HTTPS redirect
- Trailing slashes: choose one convention and enforce via redirect
- Paginated content: `rel="canonical"` points to page 1 OR use `rel="next"/"prev"` (deprecated but still useful for Googlebot)
- URL parameters (`?utm_source=...`) do NOT change the canonical

---

## 4. Schema Markup (JSON-LD)

### Organization (site-wide, on homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "ProfileTap",
  "url": "https://profiletap.com",
  "logo": "https://profiletap.com/logo.png",
  "description": "Smart identity management platform for digital business cards, NFC sharing, QR profiles, and more.",
  "sameAs": [
    "https://twitter.com/profiletap",
    "https://linkedin.com/company/profiletap",
    "https://instagram.com/profiletap"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "availableLanguage": ["English", "Hindi"]
  }
}
```

### WebSite (homepage only)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "ProfileTap",
  "url": "https://profiletap.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://profiletap.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### BreadcrumbList (all pages except homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://profiletap.com"},
    {"@type": "ListItem", "position": 2, "name": "{Hub Name}", "item": "https://profiletap.com/{hub-slug}"},
    {"@type": "ListItem", "position": 3, "name": "{Page Name}", "item": "https://profiletap.com/{page-slug}"}
  ]
}
```

### FAQ (category, use case, comparison pages with FAQ sections)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{Question text}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{Answer text}"
      }
    }
  ]
}
```

### Product (future product family pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{Product Name}",
  "description": "{Product description}",
  "brand": {"@type": "Brand", "name": "ProfileTap"},
  "offers": {
    "@type": "Offer",
    "price": "{price}",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  }
}
```

### Article (blog posts)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{Blog Title}",
  "author": {"@type": "Organization", "name": "ProfileTap"},
  "publisher": {"@type": "Organization", "name": "ProfileTap", "logo": {"@type": "ImageObject", "url": "https://profiletap.com/logo.png"}},
  "datePublished": "{ISO date}",
  "dateModified": "{ISO date}",
  "description": "{Meta description}",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "{canonical URL}"}
}
```

### Schema by Page Type Matrix

| Page Type | Organization | WebSite | Breadcrumb | FAQ | Product | Article | HowTo |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Homepage | Y | Y | - | - | - | - | - |
| Solution Hub | - | - | Y | Optional | - | - | - |
| Category | - | - | Y | Y | - | - | - |
| Use Case | - | - | Y | Y | - | - | - |
| Comparison | - | - | Y | Y | - | - | - |
| Blog | - | - | Y | Optional | - | Y | Optional |
| Product Family | - | - | Y | Optional | Y | - | - |

---

## 5. XML Sitemap

### Structure

```
/sitemap.xml                → sitemap index
/sitemap-pages.xml          → all static pages (homepage, hubs, categories, use cases, comparisons)
/sitemap-blog.xml           → all blog posts
/sitemap-products.xml       → product family pages (when activated)
/sitemap-images.xml         → image sitemap (optional but recommended)
```

### Rules

- Submit sitemap index to Google Search Console
- Include only canonical, indexable URLs (200 status, no noindex)
- Update `<lastmod>` when content is meaningfully changed
- Maximum 50,000 URLs per sitemap file
- Regenerate automatically on publish/update

---

## 6. robots.txt

```
User-agent: *
Allow: /
Disallow: /app/
Disallow: /api/
Disallow: /admin/
Disallow: /search?
Disallow: /_next/
Sitemap: https://profiletap.com/sitemap.xml
```

---

## 7. Core Web Vitals Targets

| Metric | Target | What It Measures |
|--------|--------|-----------------|
| LCP (Largest Contentful Paint) | < 2.5s | Loading performance |
| INP (Interaction to Next Paint) | < 200ms | Interactivity responsiveness |
| CLS (Cumulative Layout Shift) | < 0.1 | Visual stability |

### Optimization Priorities

1. **LCP**: Optimize hero images (WebP, lazy loading below fold, preload above fold), minimize render-blocking CSS/JS, use CDN
2. **INP**: Minimize main thread blocking, defer non-critical JS, use web workers for heavy computation
3. **CLS**: Set explicit width/height on images/embeds, avoid dynamically injected content above the fold, use `font-display: swap`

---

## 8. Hreflang (Multi-Market)

Currently India-first with global English. When global pages are added:

```html
<!-- On India-specific pages -->
<link rel="alternate" hreflang="en-IN" href="https://profiletap.com/digital-business-card-india" />
<link rel="alternate" hreflang="en" href="https://profiletap.com/digital-business-card" />
<link rel="alternate" hreflang="x-default" href="https://profiletap.com/digital-business-card" />

<!-- On global pages -->
<link rel="alternate" hreflang="en" href="https://profiletap.com/digital-business-card" />
<link rel="alternate" hreflang="en-IN" href="https://profiletap.com/digital-business-card-india" />
<link rel="alternate" hreflang="x-default" href="https://profiletap.com/digital-business-card" />
```

### Rules

- Only add hreflang when both India-specific and global versions of a page exist
- `x-default` points to the global version
- Every hreflang must be reciprocal (page A references B, page B references A)
- Include self-referencing hreflang on each page

---

## 9. Mobile-First Indexing Checklist

- [ ] Same content on mobile and desktop (no hidden content)
- [ ] Same structured data on mobile and desktop
- [ ] Same meta tags (title, description, robots) on mobile and desktop
- [ ] Responsive design (no separate m.* domain)
- [ ] Tap targets minimum 48x48px with 8px spacing
- [ ] Font size minimum 16px for body text
- [ ] Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] No horizontal scrolling on mobile
- [ ] Images scale to viewport width
- [ ] Interstitials/popups do not block content on mobile

---

## 10. Redirect Rules

| Scenario | Redirect Type | Rule |
|----------|:---:|-------|
| HTTP → HTTPS | 301 | Always |
| www → non-www (or vice versa) | 301 | Pick one, enforce globally |
| Trailing slash normalization | 301 | Pick one convention |
| Old URL → new URL | 301 | When permanently moving content |
| Temporary redirect | 302 | Only for genuinely temporary moves |
| Redirect chain | Fix | Maximum 1 hop (no chains) |

---

## 11. Index Coverage Monitoring

### Google Search Console Checks (Weekly)

- [ ] No increase in "Excluded" pages
- [ ] No new "Error" pages (server errors, redirect errors)
- [ ] "Valid" count matches expected indexed page count
- [ ] No unexpected "Noindex" pages
- [ ] No "Crawled - currently not indexed" for important pages

### Action Triggers

| Signal | Action |
|--------|--------|
| Important page not indexed after 7 days | Request indexing via URL Inspection |
| Page showing as "Discovered - not yet crawled" | Check crawl budget, add internal links |
| Unexpected noindex | Check meta robots tag, check X-Robots-Tag header |
| Soft 404 | Fix page content or add proper 404/redirect |

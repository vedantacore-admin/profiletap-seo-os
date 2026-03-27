# Technical SEO Audit & Planning

> Claude Code Skill: Complete technical SEO audit framework for any website.
> Use this as a systematic checklist when performing technical audits, planning site launches, or diagnosing ranking issues.

---

## 1. Crawlability Assessment

### 1.1 Robots.txt Audit
**Location:** Always at `https://domain.com/robots.txt`

**Checklist:**
- [ ] Robots.txt exists and is accessible (200 status code).
- [ ] Not accidentally blocking important pages or directories.
- [ ] Not blocking CSS/JS files that Googlebot needs for rendering.
- [ ] Sitemap location is declared: `Sitemap: https://domain.com/sitemap.xml`
- [ ] No conflicting directives between User-agent rules.
- [ ] Staging/dev environments use `Disallow: /` to prevent indexing.
- [ ] Production uses targeted disallow rules, not blanket blocks.

**Common Robots.txt Mistakes:**
| Mistake | Impact | Fix |
|---------|--------|-----|
| `Disallow: /` on production | Entire site deindexed | Remove or change to specific paths |
| Blocking `/wp-admin/` but also `/wp-admin/admin-ajax.php` | Breaks AJAX-dependent content | Allow admin-ajax specifically |
| Blocking `/search/` or `/filter/` not done | Crawl budget wasted on infinite parameter URLs | Add Disallow for search/filter paths |
| No sitemap declaration | Googlebot relies on other discovery methods | Add Sitemap directive |

### 1.2 XML Sitemap Audit
**Checklist:**
- [ ] Sitemap exists at `/sitemap.xml` or declared in robots.txt.
- [ ] Sitemap is submitted in Google Search Console.
- [ ] Contains only indexable, canonical URLs (no noindex, no redirects, no 404s).
- [ ] Uses proper XML format with `<urlset>` and `<url>` tags.
- [ ] Includes `<lastmod>` dates that reflect actual content changes (not auto-generated daily).
- [ ] Does not exceed 50,000 URLs per sitemap file.
- [ ] Does not exceed 50MB uncompressed per sitemap file.
- [ ] Uses a sitemap index file if multiple sitemaps are needed.
- [ ] All important pages are included (cross-reference with site structure).
- [ ] No orphan pages missing from the sitemap.

### 1.3 Crawl Budget Optimization
Crawl budget matters primarily for large sites (10,000+ pages). For smaller sites, focus on crawlability rather than budget.

**Crawl Budget Wasters:**
- Faceted navigation generating thousands of parameter URLs.
- Internal search results pages being crawled.
- Infinite calendar or pagination URLs.
- Duplicate content accessible at multiple URLs.
- Soft 404 pages (200 status but no real content).

**Solutions:**
| Problem | Solution |
|---------|----------|
| Faceted navigation | Use `robots.txt` Disallow, canonical tags, or `noindex` on filter pages |
| Search result pages | Block in `robots.txt` |
| Pagination bloat | Use `rel="next"/"prev"` (though Google says they ignore it, it still helps other engines), limit pagination depth |
| Parameter URLs | Set parameter handling in GSC, use canonical tags |
| Duplicate content | Implement canonical tags, 301 redirects, or consolidate |

---

## 2. Core Web Vitals Targets and Optimization

### 2.1 Metric Targets
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤2.5s | 2.5s-4.0s | >4.0s |
| **INP** (Interaction to Next Paint) | ≤200ms | 200ms-500ms | >500ms |
| **CLS** (Cumulative Layout Shift) | ≤0.1 | 0.1-0.25 | >0.25 |

### 2.2 LCP Optimization Priorities
1. **Optimize the LCP element** (usually hero image or H1 text).
   - Preload the hero image: `<link rel="preload" as="image" href="hero.webp">`
   - Use appropriate image format and compression.
   - Set explicit dimensions (width/height).
2. **Reduce server response time** (TTFB target: <800ms).
   - Use a CDN.
   - Implement server-side caching.
   - Optimize database queries.
3. **Eliminate render-blocking resources.**
   - Defer non-critical CSS.
   - Async or defer JavaScript.
   - Inline critical CSS.
4. **Avoid lazy loading above-the-fold images.** LCP images must load eagerly.

### 2.3 INP Optimization Priorities
1. **Reduce JavaScript execution time.**
   - Code-split and lazy-load non-critical JS.
   - Remove unused JavaScript.
   - Use web workers for heavy computation.
2. **Minimize main thread blocking.**
   - Break long tasks (>50ms) into smaller chunks.
   - Use `requestIdleCallback` for non-urgent work.
3. **Optimize event handlers.**
   - Debounce rapid-fire events (scroll, resize).
   - Use passive event listeners where possible.

### 2.4 CLS Optimization Priorities
1. **Set explicit dimensions on all media** (images, videos, iframes, ads).
2. **Reserve space for dynamic content** (ad slots, embedded widgets).
3. **Avoid inserting content above existing content** (no banners that push content down).
4. **Use `font-display: swap`** or `optional` and preload fonts to prevent layout shift from font loading.
5. **Avoid CSS that causes late reflows** (e.g., late-loading stylesheets changing layout).

### 2.5 Measurement Tools
| Tool | Lab/Field | Best For |
|------|-----------|----------|
| Google PageSpeed Insights | Both | Quick checks, field data from CrUX |
| Chrome DevTools Performance tab | Lab | Debugging specific issues |
| Chrome User Experience Report (CrUX) | Field | Real user data at origin level |
| Web Vitals Chrome Extension | Lab | Real-time monitoring during development |
| Google Search Console Core Web Vitals report | Field | Site-wide assessment, page grouping |
| Lighthouse | Lab | Comprehensive audit with recommendations |
| WebPageTest | Lab | Detailed waterfall analysis, filmstrip view |

---

## 3. Schema Markup Selection Guide

### 3.1 Schema by Page Type
| Page Type | Primary Schema | Additional Schema |
|-----------|---------------|-------------------|
| Homepage | Organization, WebSite (with SearchAction) | BreadcrumbList |
| About page | Organization or Person | BreadcrumbList |
| Blog post | Article or BlogPosting | BreadcrumbList, FAQPage (if applicable) |
| Product page | Product (with Offer, AggregateRating) | BreadcrumbList, FAQPage |
| Category page | CollectionPage or ItemList | BreadcrumbList |
| Service page | Service | BreadcrumbList, FAQPage |
| Contact page | LocalBusiness or Organization (with ContactPoint) | BreadcrumbList |
| How-to guide | HowTo | BreadcrumbList, Article |
| FAQ page | FAQPage | BreadcrumbList |
| Comparison page | Article or WebPage | BreadcrumbList, FAQPage |
| Event page | Event | BreadcrumbList |
| Recipe page | Recipe | BreadcrumbList |
| Local business page | LocalBusiness | BreadcrumbList, FAQPage |
| Multi-location page | LocalBusiness (one per location) | BreadcrumbList |

### 3.2 JSON-LD Implementation Patterns

**Organization (Homepage):**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://www.example.com",
  "logo": "https://www.example.com/logo.png",
  "sameAs": [
    "https://www.linkedin.com/company/example",
    "https://twitter.com/example",
    "https://www.facebook.com/example"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-800-555-0123",
    "contactType": "customer service"
  }
}
```

**WebSite with SearchAction (Homepage):**
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Site Name",
  "url": "https://www.example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.example.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

**BreadcrumbList (All Pages):**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.example.com/"},
    {"@type": "ListItem", "position": 2, "name": "Category", "item": "https://www.example.com/category/"},
    {"@type": "ListItem", "position": 3, "name": "Page Title"}
  ]
}
```

**Article (Blog Post):**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title (max 110 chars)",
  "author": {"@type": "Person", "name": "Author Name", "url": "https://www.example.com/author/name"},
  "datePublished": "2026-01-15",
  "dateModified": "2026-03-20",
  "publisher": {"@type": "Organization", "name": "Publisher Name", "logo": {"@type": "ImageObject", "url": "https://www.example.com/logo.png"}},
  "image": "https://www.example.com/images/article-hero.webp",
  "description": "Meta description of the article."
}
```

**Product (Product Page):**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": "https://www.example.com/product.webp",
  "description": "Product description.",
  "brand": {"@type": "Brand", "name": "Brand Name"},
  "offers": {
    "@type": "Offer",
    "price": "99.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://www.example.com/product/"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "127"
  }
}
```

**LocalBusiness:**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "ST",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "telephone": "+1-555-555-0123",
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "17:00"}
  ],
  "geo": {"@type": "GeoCoordinates", "latitude": "40.7128", "longitude": "-74.0060"}
}
```

### 3.3 Schema Validation
- Validate all schema using Google Rich Results Test: https://search.google.com/test/rich-results
- Check for warnings (not just errors) — warnings can prevent rich results.
- Monitor the Enhancements section in Google Search Console for ongoing issues.
- Schema must match visible page content exactly — no hidden or misleading data.

---

## 4. Canonical URL Strategy

### 4.1 Rules
- Every indexable page must have a self-referencing canonical tag: `<link rel="canonical" href="https://www.example.com/page/">`
- The canonical URL must be the absolute URL (not relative).
- The canonical URL must match the URL you want indexed (including www/non-www, http/https, trailing slash).
- Canonical tags go in the `<head>` section.

### 4.2 When to Use Canonical Tags
| Scenario | Canonical Points To |
|----------|-------------------|
| Duplicate content at multiple URLs (parameters, sorting) | The clean, preferred URL |
| www vs non-www versions | The chosen canonical domain |
| HTTP vs HTTPS versions | The HTTPS version (always) |
| Paginated content (page 2, 3, etc.) | Self-referencing (each page canonicalizes to itself) |
| Syndicated content published on another site | The original URL on your site |
| AMP pages | The canonical (non-AMP) version |
| Print-friendly versions | The standard page URL |

### 4.3 Canonical Tag Mistakes
- Do not canonical a page to a completely different, unrelated page.
- Do not canonical noindex pages (conflicting signals).
- Do not chain canonicals (A canonicals to B, B canonicals to C).
- Do not use canonical tags as a substitute for 301 redirects when permanently moving content.

---

## 5. Hreflang for Multi-Market / Multi-Language Sites

### 5.1 When Hreflang Is Needed
- The site serves content in multiple languages.
- The site has country-specific versions (e.g., /en-us/ and /en-gb/).
- The same language is used across different country versions with different content.

### 5.2 Implementation Rules
- Every page in the set must reference all other versions AND itself.
- Use ISO 639-1 language codes and ISO 3166-1 alpha-2 country codes.
- Include an `x-default` tag pointing to the most generic version or a language selector page.
- Hreflang can be implemented in: HTML `<head>`, HTTP headers, or XML sitemap (pick one method and be consistent).

### 5.3 Hreflang HTML Example
```html
<link rel="alternate" hreflang="en-us" href="https://www.example.com/en-us/page/" />
<link rel="alternate" hreflang="en-gb" href="https://www.example.com/en-gb/page/" />
<link rel="alternate" hreflang="es" href="https://www.example.com/es/page/" />
<link rel="alternate" hreflang="x-default" href="https://www.example.com/page/" />
```

### 5.4 Common Hreflang Errors
- Missing return tags (page A references page B, but page B does not reference page A).
- Using incorrect language or country codes.
- Hreflang pointing to non-canonical URLs.
- Hreflang pointing to redirected or noindex pages.
- Missing x-default tag.

---

## 6. Mobile-First Indexing Checklist

Google indexes the mobile version of your site. Ensure mobile parity.

- [ ] Mobile and desktop versions have identical content (text, images, videos).
- [ ] Mobile version has the same structured data as desktop.
- [ ] Mobile version has the same meta tags (title, description, robots) as desktop.
- [ ] Mobile version has the same internal links as desktop.
- [ ] Mobile version does not lazy-load primary content behind user interaction (tabs, accordions).
- [ ] Mobile viewport is set: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Text is readable without zooming (minimum 16px font size).
- [ ] Tap targets are appropriately sized (minimum 48x48px with 8px spacing).
- [ ] No horizontal scrolling required.
- [ ] Mobile page speed meets Core Web Vitals thresholds.
- [ ] No intrusive interstitials on mobile (popups covering content).

---

## 7. Page Speed Optimization Priorities

Ordered by typical impact (highest first):

1. **Reduce server response time** — CDN, caching, optimized hosting.
2. **Optimize images** — Compression, next-gen formats, responsive sizing, lazy loading.
3. **Eliminate render-blocking resources** — Defer/async JS, critical CSS inlining.
4. **Minify CSS and JavaScript** — Remove whitespace, comments, unused code.
5. **Enable compression** — Gzip or Brotli for text-based resources.
6. **Leverage browser caching** — Set long cache-control headers for static assets.
7. **Reduce third-party script impact** — Audit and defer analytics, chat widgets, ad scripts.
8. **Preconnect to required origins** — `<link rel="preconnect" href="https://fonts.googleapis.com">`
9. **Reduce DOM size** — Target under 1,500 DOM nodes.
10. **Use HTTP/2 or HTTP/3** — Multiplexed connections for faster parallel loading.

---

## 8. Redirect Management Rules

### 8.1 Redirect Types
| Type | When to Use | SEO Impact |
|------|-------------|------------|
| **301 (Permanent)** | Page permanently moved, content merged, URL structure changed | Passes ~95-99% of link equity |
| **302 (Temporary)** | A/B testing, temporary maintenance, geo-redirects | Does not pass link equity long-term |
| **307 (Temporary)** | Same as 302 but preserves HTTP method | Same as 302 for SEO |
| **Meta refresh** | Never use for SEO purposes | Poor UX, partial link equity |
| **JavaScript redirect** | Never use for SEO purposes | Googlebot may not follow reliably |

### 8.2 Redirect Rules
- Always use 301 for permanent URL changes.
- Redirect to the most relevant replacement page, not just the homepage.
- Eliminate redirect chains (A→B→C). Every redirect should go directly to the final destination.
- Eliminate redirect loops (A→B→A).
- Keep total redirects under 1,000 if possible. Implement at the server level for performance.
- After migration, monitor 404 errors in GSC for 6 months and add redirects as needed.
- Remove redirects only after 1+ year (once Google has updated its index).

### 8.3 Redirect Audit Checklist
- [ ] No redirect chains longer than 1 hop.
- [ ] No redirect loops.
- [ ] All 301s point to live, indexable pages.
- [ ] No 302s that should be 301s (temporary redirects that have been in place for months).
- [ ] Old sitemap URLs are not redirecting (update the sitemap instead).
- [ ] HTTPS redirects are in place for all HTTP URLs.
- [ ] WWW/non-WWW redirects are consistent.

---

## 9. Index Coverage Analysis (Google Search Console)

### 9.1 Key Reports to Monitor
| Status | Meaning | Action |
|--------|---------|--------|
| **Valid** | Indexed and no issues | Monitor for drops |
| **Valid with warnings** | Indexed but has issues | Investigate and fix warnings |
| **Excluded** | Not indexed | Review exclusion reasons |
| **Error** | Attempted to index but failed | Fix immediately |

### 9.2 Common Exclusion Reasons and Fixes
| Exclusion Reason | Likely Cause | Fix |
|-----------------|-------------|-----|
| "Crawled - currently not indexed" | Low quality or thin content | Improve content quality, add internal links, earn backlinks |
| "Discovered - currently not indexed" | Google discovered but chose not to crawl | Improve site authority, add internal links, submit in sitemap |
| "Excluded by noindex tag" | Intentional or accidental noindex | Verify it is intentional; remove noindex if not |
| "Duplicate without user-selected canonical" | Google chose a different canonical | Check canonical tags, consolidate duplicate content |
| "Alternate page with proper canonical tag" | Expected for pages with canonical pointing elsewhere | No action if intentional |
| "Blocked by robots.txt" | Robots.txt disallowing crawling | Remove block if the page should be indexed |
| "Soft 404" | Page returns 200 but has no/thin content | Add real content or return a proper 404/410 |

---

## 10. Log File Analysis Methodology

### 10.1 What to Analyze
Server access logs reveal how search engine bots actually crawl your site (versus what tools simulate).

**Key Data Points:**
- Which pages Googlebot crawls most frequently.
- Which pages Googlebot never crawls.
- Crawl frequency trends over time.
- Status codes Googlebot encounters.
- Crawl budget distribution across page types.

### 10.2 Analysis Process
1. Export 30 days of server access logs.
2. Filter to only Googlebot requests (verify via DNS reverse lookup).
3. Categorize URLs by page type (product, category, blog, etc.).
4. Calculate crawl frequency per page type.
5. Identify pages with zero crawls (orphan or low-priority pages).
6. Identify pages with excessive crawls (crawl traps, parameter URLs).
7. Check for high rates of 4xx or 5xx responses to Googlebot.

### 10.3 Tools for Log Analysis
- Screaming Frog Log File Analyser
- Oncrawl
- JetOctopus
- Custom analysis with Python/Pandas or ELK stack

---

## 11. Site Architecture and URL Hierarchy

### 11.1 Architecture Principles
- Every important page should be reachable within 3 clicks from the homepage.
- Use a flat-ish hierarchy: Homepage → Category → Page (not deeper than 4 levels).
- Navigation should expose all major sections.
- Breadcrumbs should reflect the URL hierarchy.
- Avoid orphan pages (pages with no internal links pointing to them).

### 11.2 Architecture Audit
- [ ] All important pages are linked from the main navigation or footer.
- [ ] Click depth for key pages is 3 or fewer from homepage.
- [ ] No orphan pages (use Screaming Frog crawl to detect).
- [ ] Breadcrumbs are implemented and match the URL structure.
- [ ] Internal link distribution is balanced (not all links pointing to the homepage).
- [ ] Category pages link to all child pages.
- [ ] Related content links exist between sibling pages.

---

## 12. Pagination and Infinite Scroll Handling

### 12.1 Pagination Best Practices
- Each paginated page should have a unique, crawlable URL (e.g., `/category/?page=2`).
- Each paginated page should have a self-referencing canonical tag.
- Do not noindex paginated pages — they need to be crawled for Google to discover products/articles.
- Include `rel="next"` and `rel="prev"` (still useful for Bing and other engines).
- Provide a "View All" page if the total items are under 100 and the page loads quickly.
- Link to the first and last pages of the series for faster crawling.

### 12.2 Infinite Scroll SEO Requirements
Infinite scroll is invisible to search engine crawlers. You must provide:
- A paginated fallback accessible at distinct URLs (e.g., `/category/?page=2`).
- Each paginated component page must be crawlable without JavaScript.
- The paginated URLs must be discoverable via internal links or sitemap.

---

## 13. Output Format: Technical SEO Audit Report Template

### Section 1: Executive Summary
- Overall site health score (Critical / Needs Work / Good / Excellent).
- Top 3 critical issues requiring immediate attention.
- Top 3 opportunities for improvement.

### Section 2: Crawlability & Indexability
- Robots.txt status and issues.
- XML sitemap status and issues.
- Index coverage summary (indexed vs excluded pages).
- Crawl budget assessment (for large sites).

### Section 3: Core Web Vitals
- LCP, INP, CLS scores (field data from CrUX if available).
- Page-level breakdown for key templates.
- Specific optimization recommendations prioritized by impact.

### Section 4: On-Page Technical Elements
- Canonical tag audit results.
- Hreflang audit results (if applicable).
- Schema markup audit results.
- Mobile-friendliness assessment.

### Section 5: Site Architecture
- Click depth analysis.
- Orphan page count.
- Internal linking distribution.
- URL structure assessment.

### Section 6: Redirects & Errors
- Redirect chain/loop count.
- 4xx error page count.
- 5xx error page count.
- Soft 404 count.

### Section 7: Page Speed
- PageSpeed Insights scores for key page templates.
- Top speed optimization opportunities.

### Section 8: Prioritized Action Items
| Priority | Issue | Impact | Effort | Recommendation |
|----------|-------|--------|--------|----------------|
| P1 | [Description] | High | [Hours/Days] | [Specific action] |
| P2 | [Description] | Medium | [Hours/Days] | [Specific action] |
| P3 | [Description] | Low | [Hours/Days] | [Specific action] |

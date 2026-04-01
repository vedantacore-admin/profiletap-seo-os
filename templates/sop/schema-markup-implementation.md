# SOP: Schema Markup Implementation

## Purpose

Define which JSON-LD schema types to implement on each [PROJECT_NAME] page type, provide copy-ready templates, and establish testing/monitoring processes.

---

## 1. Schema by Page Type

| Page Type | Organization | WebSite | BreadcrumbList | FAQ | Article | Product | HowTo |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Homepage | Y | Y | - | - | - | - | - |
| Solution Hub | - | - | Y | Optional | - | - | - |
| Category | - | - | Y | Y | - | - | - |
| Use Case | - | - | Y | Y | - | - | - |
| Comparison | - | - | Y | Y | - | - | - |
| Blog | - | - | Y | Optional | Y | - | Optional |
| Product Family | - | - | Y | Optional | - | Y | - |

**Rules:**
- FAQ schema: required if page has an FAQ section with 4+ questions
- HowTo schema: only if blog post is a step-by-step guide
- Organization: only on homepage (site-wide signal)
- WebSite: only on homepage (with SearchAction if site search exists)

---

## 2. JSON-LD Templates

### Organization (Homepage)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[PROJECT_NAME]",
  "url": "https://[SITE_URL]",
  "logo": "https://[SITE_URL]/images/profiletap-logo.png",
  "description": "Smart identity management platform for digital business cards, NFC sharing, QR profiles, and more.",
  "foundingDate": "2024",
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
</script>
```

### WebSite (Homepage)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "[PROJECT_NAME]",
  "url": "https://[SITE_URL]",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://[SITE_URL]/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>
```

Note: Only include SearchAction if the site has a search function. Remove if not applicable.

### BreadcrumbList (All pages except homepage)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://[SITE_URL]"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "PARENT_PAGE_TITLE",
      "item": "https://[SITE_URL]/PARENT_SLUG"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "CURRENT_PAGE_TITLE",
      "item": "https://[SITE_URL]/CURRENT_SLUG"
    }
  ]
}
</script>
```

Replace `PARENT_PAGE_TITLE`, `PARENT_SLUG`, `CURRENT_PAGE_TITLE`, `CURRENT_SLUG` with actual values from `page_master.csv`.

### FAQPage (Category, Use Case, Comparison pages with FAQ)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "QUESTION_1",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER_1"
      }
    },
    {
      "@type": "Question",
      "name": "QUESTION_2",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER_2"
      }
    }
  ]
}
</script>
```

- Include 4-8 FAQs per page
- Questions should match People Also Ask when possible
- Answers should be concise (2-3 sentences) in the schema, even if the on-page answer is longer
- HTML is allowed in answer `text` (links, bold, lists)

### Article (Blog posts)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "BLOG_TITLE",
  "description": "META_DESCRIPTION",
  "author": {
    "@type": "Organization",
    "name": "[PROJECT_NAME]",
    "url": "https://[SITE_URL]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[PROJECT_NAME]",
    "logo": {
      "@type": "ImageObject",
      "url": "https://[SITE_URL]/images/profiletap-logo.png"
    }
  },
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "CANONICAL_URL"
  },
  "image": "OG_IMAGE_URL"
}
</script>
```

### Product (Future product family pages)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "PRODUCT_NAME",
  "description": "PRODUCT_DESCRIPTION",
  "brand": {
    "@type": "Brand",
    "name": "[PROJECT_NAME]"
  },
  "image": "PRODUCT_IMAGE_URL",
  "offers": {
    "@type": "Offer",
    "price": "PRICE",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "url": "PRODUCT_PAGE_URL"
  }
}
</script>
```

### HowTo (Blog posts with step-by-step instructions)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "HOW_TO_TITLE",
  "description": "HOW_TO_DESCRIPTION",
  "step": [
    {
      "@type": "HowToStep",
      "name": "STEP_1_TITLE",
      "text": "STEP_1_DESCRIPTION"
    },
    {
      "@type": "HowToStep",
      "name": "STEP_2_TITLE",
      "text": "STEP_2_DESCRIPTION"
    }
  ]
}
</script>
```

---

## 3. Implementation Process

### For Each New Page

1. Determine which schema types apply (use Section 1 matrix)
2. Copy the relevant template(s) from Section 2
3. Replace placeholder values with actual page data
4. Add JSON-LD `<script>` tags to the page's `<head>` section
5. Test with Google Rich Results Test before publishing
6. Verify in Google Search Console after indexing

### For Existing Pages

1. Audit which pages have schema and which don't
2. Prioritize: P1 pages first, then P2, then P3
3. Add missing schema following the same process
4. Test and verify

---

## 4. Testing

### Before Publish

1. Copy the JSON-LD code
2. Go to Google Rich Results Test (https://search.google.com/test/rich-results)
3. Paste the code OR enter the page URL (if accessible)
4. Verify: no errors, no warnings
5. Check that all required fields are populated

### Common Errors

| Error | Fix |
|-------|-----|
| Missing required field | Add the field to the JSON-LD |
| Invalid date format | Use ISO 8601: `YYYY-MM-DD` |
| URL not accessible | Ensure the URL is live and not behind auth |
| Image URL 404 | Fix the image path |
| Duplicate schema types | Only one of each type per page |

---

## 5. Monitoring

### Weekly

- Check Google Search Console > Enhancements for schema errors/warnings
- Fix any new errors within 3 days

### Monthly

- Review Rich Results report in Search Console
- Check which pages have valid rich results vs errors
- Track: number of FAQ rich results, Article rich results showing in SERPs

### After Algorithm Updates

- Check if rich result eligibility criteria have changed
- Update schema if Google deprecates or modifies requirements

---

## 6. Schema Maintenance Rules

- When page content changes, update schema to match (especially FAQ, dates, prices)
- When `dateModified` changes on a blog, update Article schema's `dateModified`
- When prices change on product pages, update Product schema's `offers.price`
- Never add schema for content that doesn't exist on the visible page
- Schema must accurately reflect on-page content (Google penalizes mismatches)

---

## 7. AI Visibility

### Why This Matters

Google AI Overviews, ChatGPT Browse, Perplexity, and other AI models extract structured content to answer queries directly. FAQPage schema is a primary signal for AI-surfaced answers. Blocking AI crawlers in `robots.txt` silently removes [PROJECT_NAME] from AI-generated responses.

### robots.txt Rules for AI Crawlers

Add the following to `robots.txt` on the live site. Blocking any of these removes [PROJECT_NAME] content from that AI product's answers:

```
# Allow all AI crawlers (required for AI Overviews and LLM visibility)
User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Anthropic-AI
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: Claude-Web
Allow: /
```

### FAQPage Optimization for AI Overviews

FAQPage schema is how Google AI Overviews and Perplexity pull [PROJECT_NAME] answers into generated responses. Rules:

- Keep answer text in schema `≤ 300 characters` — AI extraction favors concise, self-contained answers
- Questions must be natural-language, conversational phrasing (match voice search intent)
- Answers must be self-contained — no "see above" or "as mentioned earlier" references
- Use 4–8 Q&A pairs per page; prioritize the most common search queries
- Schema answers can differ from on-page answers — schema can be shorter summaries

### Speakable Schema (Blogs and Solution Hubs)

Add `speakable` to `Article` or `WebPage` schema when the page has a clear introductory summary paragraph or FAQ answers suited for voice/AI extraction:

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".page-summary", "h1", ".faq-answer"]
  }
}
</script>
```

Implement the CSS classes `.page-summary` and `.faq-answer` in the frontend for this to activate.

### Additional Structured Data for AI Disambiguation

Add these fields to the existing Organization schema on the homepage:

```json
{
  "@type": "Organization",
  "name": "[PROJECT_NAME]",
  "url": "https://[SITE_URL]",
  "areaServed": {
    "@type": "Country",
    "name": "India"
  },
  "inLanguage": "en-IN"
}
```

Add to Article schema on all blog posts:

```json
{
  "inLanguage": "en-IN",
  "about": {
    "@type": "Thing",
    "name": "Digital Business Cards"
  }
}
```

These fields help AI models correctly associate [PROJECT_NAME] content with India-market queries and avoid entity confusion with similar global products.

### Developer Validation Headers

Every content file in `content/pages/`, `content/blogs/`, and `content/products/` has a `<!-- DEVELOPER VALIDATION -->` block immediately after its frontmatter. This block lists required schema types, the BreadcrumbList path, and the AI visibility checklist.

To regenerate or add headers to new files:

```bash
python scripts/add_dev_headers.py
```

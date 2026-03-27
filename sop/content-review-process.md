# SOP: Content Review Process

## Purpose

Ensure every page goes through a consistent quality review from brief to publish — covering SEO alignment, brand accuracy, anti-cannibalization, schema, and technical readiness.

---

## 1. Brief Approval Checklist

Before a brief moves to content writing:

- [ ] Page exists in `page_master.csv` with correct slug, type, hub, and parent
- [ ] Page exists in `execution_seo_master.csv` with matching primary keyword
- [ ] Page exists in `content_calendar.csv` with correct content_id
- [ ] Primary keyword does NOT duplicate any other page's primary keyword
- [ ] `feature_set` matches the hub's canonical feature subset
- [ ] `search_intent` matches SERP reality (validated via SERP analysis if P1)
- [ ] Brief follows `briefs/templates/page-brief-template.md` structure
- [ ] All 9 brief sections are populated (metadata, search context, product angle, SEO requirements, content goal, recommended structure, internal linking, CTA, writer notes)
- [ ] Feature tokens are translated to human labels
- [ ] Internal linking targets are valid page slugs

**Status after approval:** Update `brief_status` to `approved` in `content_calendar.csv`.

---

## 2. Content QA Checklist

After content is written, before publish:

### SEO Elements

- [ ] Title tag follows formula from `docs/03-technical-seo.md` (max 60 chars, contains primary keyword)
- [ ] Meta description follows formula (max 155 chars, contains primary keyword, includes CTA)
- [ ] H1 contains primary keyword (different from title tag)
- [ ] H2/H3 hierarchy is logical (no skipped levels)
- [ ] Primary keyword appears in first 100 words
- [ ] Secondary keywords appear naturally throughout
- [ ] URL matches `page_slug` from `page_master.csv`
- [ ] Canonical tag is self-referencing

### Content Quality

- [ ] Content matches the approved brief's structure and goals
- [ ] Content is original (not copied from competitor pages)
- [ ] Feature tokens are displayed as human labels (e.g., "QR sharing" not "qr_sharing")
- [ ] ProfileTap is positioned as "smart identity platform" (not just "NFC card tool")
- [ ] India-first messaging is present for IN-market pages
- [ ] Comparison pages include a feature comparison table
- [ ] FAQ section includes 4-6 questions (matching PAA where possible)
- [ ] Content length meets minimum for page type:
  - Homepage: 1500+ words
  - Hub: 1200+ words
  - Category: 1500+ words
  - Use case: 1200+ words
  - Comparison: 1500+ words
  - Blog: 1000+ words

### Internal Linking

- [ ] Links to parent hub page (via breadcrumb + in-content)
- [ ] Links to `primary_internal_link_target` (for blogs)
- [ ] Links to `secondary_internal_link_targets` (for blogs)
- [ ] Links to 2-3 sibling pages within the same hub
- [ ] Anchor text follows guidelines from `docs/04-internal-linking-strategy.md`
- [ ] No broken internal links

### Schema Markup

- [ ] BreadcrumbList JSON-LD present (all pages except homepage)
- [ ] FAQ schema present (if page has FAQ section)
- [ ] Article schema present (blog posts)
- [ ] Schema validates via Google Rich Results Test

### Images

- [ ] All images have alt text following the formula from `docs/08-image-seo-guidelines.md`
- [ ] Image file names follow naming convention
- [ ] Images compressed within size targets
- [ ] WebP format with fallback
- [ ] `width` and `height` attributes set
- [ ] OG image created (1200x630)

### Technical

- [ ] Page loads in < 3 seconds
- [ ] Mobile rendering is correct (responsive)
- [ ] No horizontal scroll on mobile
- [ ] Core Web Vitals pass (LCP < 2.5s, INP < 200ms, CLS < 0.1)
- [ ] OG tags and Twitter Card tags present

---

## 3. Anti-Cannibalization Final Check

Before publish, verify:

- [ ] No other published page targets the same primary keyword
- [ ] This page's secondary keywords don't overlap significantly with another page's primary keyword
- [ ] The page's content role (money page, comparison, blog, etc.) is distinct from overlapping pages
- [ ] Internal links from this page don't compete with its own ranking target

---

## 4. Publish Readiness Criteria

All of the following must be true:

1. Brief was approved (Section 1 checklist complete)
2. Content QA passed (Section 2 checklist complete)
3. Anti-cannibalization verified (Section 3)
4. Page status updated to `in_progress` in `page_master.csv`
5. Owner assigned in `content_calendar.csv`

---

## 5. Post-Publish Verification

Within 24 hours of publishing:

- [ ] Page accessible and rendering correctly
- [ ] URL submitted to Google Search Console for indexing
- [ ] Page appears in XML sitemap
- [ ] Social distribution started (per `docs/07-content-distribution.md`)
- [ ] Internal links from 3+ existing pages point to the new page

Within 7 days:

- [ ] Page is indexed in Google (check Search Console)
- [ ] No crawl errors for this URL
- [ ] Initial impressions visible in Search Console

After 30 days:

- [ ] Record baseline metrics: ranking, traffic, impressions, CTR
- [ ] Update `status` to `published` in `page_master.csv`
- [ ] Update `status` to `published` and `brief_status` to `published` in `content_calendar.csv`
- [ ] Set `publish_date` and `last_updated` in `page_master.csv`

---

## 6. Workflow Summary

```
Brief Created → Brief Approved → Content Written → Content QA → Anti-Cannib Check → Publish → Post-Publish Verify → Baseline Captured
```

Status transitions in `content_calendar.csv`:
```
brief_pending → in_draft → ready_for_review → approved → published
```

Status transitions in `page_master.csv`:
```
planned → in_progress → published → refresh_needed
```

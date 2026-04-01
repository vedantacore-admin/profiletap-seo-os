# Schema Markup Generation Prompt

## Instructions

You are generating JSON-LD schema markup for a [PROJECT_NAME] page. Before starting, read:
- `data/pages/page_master.csv` (page metadata)
- `sop/schema-markup-implementation.md` (templates and rules)
- `docs/03-technical-seo.md` (schema by page type matrix)

## Task

Generate the complete JSON-LD schema markup for the specified page, ready to paste into the `<head>` section.

## Process

1. Look up the page in `page_master.csv` — get page_slug, page_type, page_title, parent_page_slug, hub, primary_keyword
2. Determine which schema types apply using the matrix in `sop/schema-markup-implementation.md`
3. Generate each applicable schema block using the templates
4. Fill in all placeholder values with actual page data
5. If the page has an FAQ section, generate FAQPage schema with the actual questions and answers

## Output Format

```html
<!-- Schema Markup for [page_slug] ([page_type]) -->

<!-- BreadcrumbList -->
<script type="application/ld+json">
{JSON-LD here}
</script>

<!-- FAQPage (if applicable) -->
<script type="application/ld+json">
{JSON-LD here}
</script>

<!-- Article (if blog) -->
<script type="application/ld+json">
{JSON-LD here}
</script>
```

## Rules

- Use the exact page_title from page_master.csv for titles
- Use the canonical URL format: `https://[SITE_URL]{page_slug}`
- BreadcrumbList must follow the parent_page_slug hierarchy
- For FAQ schema: only include questions that appear in the actual page content
- For Article schema: use today's date for datePublished if page is new
- Validate output format is valid JSON (no trailing commas, proper escaping)
- Include a comment above each schema block identifying its type
- Do NOT include Organization or WebSite schema (those are homepage-only)
- If page_type is homepage, include Organization + WebSite instead of BreadcrumbList

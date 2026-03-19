# Content Brief Prompt

Use this prompt to generate a brief only after checking the repository CSV files.

## Prompt

You are generating an SEO content brief for ProfileTap, a smart identity platform.

Before writing the brief:

1. Read `data/keywords/master_keywords.csv`
2. Read `data/pages/page_master.csv`
3. Read `data/pages/page_keyword_map.csv`
4. Read `data/content/content_calendar.csv`
5. If relevant, read `data/backlinks/backlink_targets.csv`

Then generate a brief for the requested target page using the rules below.

### Rules

- use the mapped keyword and page slug exactly as defined in the CSVs
- do not invent a second primary keyword
- keep the brief aligned to the page type
- if the keyword is India-first transactional, keep conversion intent central
- if the keyword is a comparison term, make switch intent central
- if the keyword is informational, route the reader toward a mapped commercial page
- frame ProfileTap as a smart identity platform, not only as an NFC card tool

### Required Output Format

Return the brief with these sections:

1. Brief Metadata
2. Search Context
3. Product Angle
4. SEO Requirements
5. Content Goal
6. Recommended Structure
7. Internal Linking
8. CTA
9. Notes For Writer

### Metadata fields to include

- page slug
- page type
- primary keyword
- mapped secondary keywords
- cluster
- intent
- priority
- content calendar ID if available

### Structure guidance by page type

For `homepage`:

- positioning
- feature overview
- use-case coverage
- CTA

For `category`:

- category definition
- benefits
- how ProfileTap works
- use-case examples
- CTA

For `use_case`:

- audience pain points
- ProfileTap use cases for that audience
- feature proof
- CTA

For `comparison`:

- alternative framing
- comparison table
- decision criteria
- reasons to switch
- FAQ
- CTA

For `blog`:

- direct answer
- supporting explanation
- examples or framework
- internal links to the relevant money page
- CTA

### Quality bar

- concise, operational, and specific
- no generic filler
- no duplicate intent with another page
- include conversion goal and internal link targets
- include FAQs only when they match the keyword intent

## Example invocation

Generate a brief for `/digital-business-card-india` using the mapped keyword data and the current content calendar entry.

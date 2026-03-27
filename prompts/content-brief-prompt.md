# Content Brief Prompt

Use this prompt to generate a brief only after checking the repository CSV files.

## Prompt

You are generating an SEO content brief for ProfileTap, a smart identity management platform.

Before writing the brief:

1. Read `data/keywords/raw_keyword_bank.csv`
2. Read `data/pages/page_master.csv`
3. Read `data/keywords/execution_seo_master.csv`
4. Read `data/content/content_calendar.csv`
5. If relevant, read `data/backlinks/backlink_targets.csv`

Then generate a brief for the requested target page using the rules below.

### Rules

- use the canonical keyword family and page slug exactly as defined in the CSVs
- if `target_keyword` is blank, use the page's architecture role and `primary_intent` from `page_master.csv`
- do not invent a second primary keyword
- keep the brief aligned to the page type
- treat features as embedded modules from `feature_set`, not as standalone page intent
- translate internal feature tokens into human-facing labels in the brief
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
- page group
- parent page slug
- hub
- primary keyword
- mapped secondary keywords
- search intent
- priority
- content calendar ID if available
- feature set
- pricing visibility

### Structure guidance by page type

For `homepage`:

- positioning
- full feature inventory
- feature overview
- use-case coverage
- CTA

For `solution_hub`:

- hub-specific positioning
- relevant feature subset
- use cases or workflows for that hub
- CTA

For `category`:

- category definition
- benefits
- how ProfileTap works in that hub context
- use-case examples
- CTA

For `use_case`:

- audience pain points
- ProfileTap use cases for that audience
- feature proof inherited from the hub
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
- do not create standalone feature-page framing unless the page inventory explicitly requires it
- do not expose raw token names like `multi_profile_type_profiles` in final brief output without translating them

## Example invocation

Generate a brief for `/business-identity` using the current page inventory and content calendar entry.

# Page Mapping SOP

## Purpose

Map every keyword in `data/keywords/master_keywords.csv` to exactly one canonical page in `data/pages/page_master.csv`, then record that decision in `data/pages/page_keyword_map.csv`.

This SOP exists to prevent cannibalization and keep content production tied to commercial outcomes.

## Required Inputs

- `data/keywords/master_keywords.csv`
- `data/pages/page_master.csv`
- `data/pages/page_keyword_map.csv`
- `data/content/content_calendar.csv`

## Output Rule

Each keyword must end in one of these states:

- mapped to an existing page
- mapped to a newly created page entry in `page_master.csv`
- held back because its intent is already covered by an existing page

## Mapping Hierarchy

Use this order when deciding the canonical page:

1. intent
2. market modifier
3. audience or use case
4. competitor or comparison angle
5. format specificity

If two keywords express the same underlying intent, they belong to one page.

## Page-Type Rules

### Homepage

Use only for broad brand or category-defining commercial positioning.

Current example:

- `smart identity platform` -> `/`

### Category page

Use for broad transactional product demand where the user is looking for a solution category.

Current examples:

- `digital business card india` -> `/digital-business-card-india`
- `digital visiting card india` -> `/digital-business-card-india`
- `nfc business card india` -> `/nfc-business-card-india`
- `qr business card` -> `/qr-business-card`

### Use-case page

Use when the keyword includes a professional segment, vertical, or audience-specific workflow.

Current examples:

- `digital business card for doctors` -> `/digital-business-card-for-doctors`
- `digital business card for real estate agents` -> `/digital-business-card-for-real-estate-agents`
- `digital business card for freelancers` -> `/digital-business-card-for-freelancers`

### Comparison page

Use when the keyword includes a competitor or explicit alternative intent.

Current examples:

- `hihello alternative india` -> `/hihello-alternative-india`
- `popl alternative india` -> `/popl-alternative-india`
- `taponn alternative` -> `/taponn-alternative`

### Blog page

Use only when the searcher intent is educational, comparative, or early stage and should support a commercial page.

Current examples:

- `nfc business card vs qr code` -> `/blog/nfc-business-card-vs-qr-code`
- `paper business card vs digital business card` -> `/blog/paper-vs-digital-business-card`

## Anti-Cannibalization Tests

Before creating a new page, answer these checks:

1. Does a page already target the same solution with minor wording changes?
2. Is the market modifier the only difference, and is the current page already built for that market?
3. Is the audience modifier strong enough to justify a dedicated use-case page?
4. Is this a comparison keyword that should live on a competitor page instead of a category page?
5. Is the query informational and better handled as a support article instead of a new commercial landing page?

If the answer to the first question is yes, map the keyword to the existing page and mark `is_primary=no`.

## Mapping Workflow

1. Review the keyword and assign `cluster`, `intent`, and `target_page_type` in `master_keywords.csv`.
2. Search `page_keyword_map.csv` for overlapping intent.
3. If an existing page already covers the intent, append the keyword there with `is_primary=no`.
4. If no page covers the intent, create a new row in `page_master.csv`.
5. Add the canonical mapping row in `page_keyword_map.csv`.
6. Add exactly one matching production row in `content_calendar.csv`.

## Examples From Current Data

### Example 1: variation mapping

Keyword:

- `digital visiting card india`

Decision:

- map to `/digital-business-card-india`

Reason:

- same transactional intent as `digital business card india`
- only wording variation changes, not page intent

### Example 2: new use-case page

Keyword:

- `digital business card for doctors`

Decision:

- create and map to `/digital-business-card-for-doctors`

Reason:

- strong vertical intent
- dedicated proof, CTA, and examples are required

### Example 3: comparison isolation

Keyword:

- `hihello alternative india`

Decision:

- map to `/hihello-alternative-india`

Reason:

- switch intent differs from generic category demand
- comparison content should not be merged into the category page

## Status Conventions

Recommended status values:

- `master_keywords.csv`: `new`, `mapped`, `deferred`
- `page_master.csv`: `planned`, `in_progress`, `published`
- `content_calendar.csv`: `brief_pending`, `writing`, `review`, `published`

## Failure Cases To Avoid

- creating separate pages for `digital business card india` and `digital visiting card india`
- turning every keyword variation into a blog post
- mapping comparison keywords into category pages
- adding blog topics that do not point back to a commercial page
- creating backlinks for pages that do not exist in `page_master.csv`

## Done Criteria

A mapping task is complete only when:

- the keyword exists in `master_keywords.csv`
- the canonical page exists in `page_master.csv`
- the keyword is mapped once in `page_keyword_map.csv`
- the content task exists in `content_calendar.csv`
- the chosen page does not conflict with another page's primary intent

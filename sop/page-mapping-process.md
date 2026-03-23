# Page Mapping SOP

## Purpose

Map every approved keyword family in `data/keywords/execution_seo_master.csv` to exactly one canonical page in `data/pages/page_keyword_map.csv`, using `data/pages/page_master.csv` as the page inventory and launch architecture source of truth.

This SOP exists to prevent cannibalization and keep content production tied to commercial outcomes.

Current architecture rule:

- homepage plus six launch solution hubs are fixed
- features are embedded into those pages via `feature_set`
- no standalone feature pages should be created unless later keyword research proves distinct intent
- future physical product pages are documented separately and should not be added to `page_master.csv` until product-intent keyword validation is complete

## Required Inputs

- `data/keywords/raw_keyword_bank.csv`
- `data/keywords/execution_seo_master.csv`
- `data/keywords/master_keywords.csv`
- `data/pages/page_master.csv`
- `data/pages/page_keyword_map.csv`
- `data/content/content_calendar.csv`

## Output Rule

Each keyword must end in one of these states:

- mapped to an existing page
- mapped to a newly created page entry in `page_master.csv`
- held back because its intent is already covered by an existing page

Before a keyword reaches page mapping, it should already have passed the raw-bank decision stage:

- `keep_primary`
- `keep_secondary`

## Mapping Hierarchy

Use this order when deciding the canonical page:

1. intent
2. hub fit
3. market modifier
4. audience or use case
5. competitor or comparison angle
6. format specificity

If two keywords express the same underlying intent, they belong to one page.

## Page-Type Rules

### Homepage

Use only for broad brand or platform-defining commercial positioning.

Current example:

- `smart identity platform` -> `/`

### Solution hub page

Use for top-level launch pages that organize the product by audience or life category before the full keyword universe is imported.

Current examples:

- `/business-identity`
- `/creator-identity`
- `/family-safety-profile`
- `/pet-id-profile`
- `/travel-profile`
- `/vehicle-profile`

Important:

- a solution hub may exist in `page_master.csv` before it has a finalized primary keyword
- solution hubs should embed relevant features rather than behave like standalone feature pages

### Category page

Use for broad transactional product demand where the user is looking for a solution category.

Current examples:

- `digital business card india` -> `/digital-business-card-india`
- `digital visiting card india` -> `/digital-business-card-india`
- `nfc business card india` -> `/nfc-business-card-india`
- `qr business card` -> `/qr-business-card`

Important:

- this rule covers solution-category demand, not future physical product-family pages
- product-family pages such as `/products/metal-business-cards` are a separate planned layer and are not active in the current page inventory

### Use-case page

Use when the keyword includes a profession, vertical, or audience-specific workflow.

Current examples:

- `digital business card for doctors` -> `/digital-business-card-for-doctors`
- `digital business card for real estate agents` -> `/digital-business-card-for-real-estate-agents`
- `digital business card for freelancers` -> `/digital-business-card-for-freelancers`
- `digital business card for creators` -> `/digital-business-card-for-creators`

### Comparison page

Use when the keyword includes a competitor or explicit alternative intent.

Current examples:

- `hihello alternative india` -> `/hihello-alternative-india`
- `popl alternative india` -> `/popl-alternative-india`
- `taponn alternative` -> `/taponn-alternative`
- `linktree alternative for creators` -> `/linktree-alternative-for-creators`

### Blog page

Use only when the searcher intent is educational, comparative, or early stage and should support a commercial page.

Current examples:

- `nfc business card vs qr code` -> `/blog/nfc-business-card-vs-qr-code`
- `paper business card vs digital business card` -> `/blog/paper-vs-digital-business-card`

### Future product-family page

Use later for physical-product buying intent once product keywords are validated.

Documented, but not yet active, examples:

- `/products/metal-business-cards`
- `/products/wooden-nfc-cards`
- `/products/pvc-business-cards`
- `/products/business-standees`
- `/products/keychains`
- `/products/pet-tags`
- `/products/google-review-cards`
- `/products/luggage-cards`
- `/products/vehicle-stickers`

Rules:

- product-family pages own physical-product purchase intent
- solution pages still own use-case and workflow intent
- colors, finishes, QR-only, NFC+QR, and similar variants stay on the family page by default
- profession-specific product pages such as `metal business card for doctors` should not be created by default

## Anti-Cannibalization Tests

Before creating a new page, answer these checks:

1. Does a page already target the same solution with minor wording changes?
2. Is the keyword better served by an existing hub or child page under the same hub?
3. Is the audience modifier strong enough to justify a dedicated use-case page?
4. Is this a comparison keyword that should live on a competitor page instead of a category or hub page?
5. Is the query informational and better handled as a support article instead of a new commercial landing page?
6. Is the idea actually a feature block that belongs inside an existing hub or child page rather than a new SEO page?
7. Is the idea really a future physical-product page that should stay documented until product keyword validation is complete?

If the answer to the first, second, sixth, or seventh question is yes, map the keyword to the existing page or hold it in documentation and mark `is_primary=no` when appropriate.

## Mapping Workflow

1. Process the raw import in `raw_keyword_bank.csv` and assign `canonical_keyword`, `canonical_page_slug`, and `keep_status`.
2. Move only approved page-worthy families into `execution_seo_master.csv`.
3. Check `page_master.csv` for the correct `hub`, `page_group`, and `feature_set` before deciding whether a new page is needed.
4. Search `page_keyword_map.csv` for overlapping intent.
5. If an existing page already covers the intent, append the keyword there with `is_primary=no`.
6. If no page covers the intent, create a new row in `page_master.csv`.
7. Add the canonical mapping row in `page_keyword_map.csv`.
8. Add exactly one matching production row in `content_calendar.csv`.

Decision rule:

- only `keep_primary` and selected `keep_secondary` families should exist in the raw bank
- only those families should reach the execution mapping layer

## Examples From Current Data

### Example 1: variation mapping

Keyword:

- `digital visiting card india`

Decision:

- map to `/digital-business-card-india`

Reason:

- same transactional intent as `digital business card india`
- only wording variation changes, not page intent
- this should stay a secondary family signal, not a separate execution row

### Example 2: new use-case page

Keyword:

- `digital business card for doctors`

Decision:

- create and map to `/digital-business-card-for-doctors`

Reason:

- strong profession-specific intent
- dedicated proof, CTA, and examples are required

### Example 3: comparison isolation

Keyword:

- `hihello alternative india`

Decision:

- map to `/hihello-alternative-india`

Reason:

- switch intent differs from generic category demand
- comparison content should not be merged into the category or hub page

### Example 4: feature containment

Idea:

- AI review assist

Decision:

- keep it inside homepage, business, creator, and relevant child pages unless feature-led keyword research later proves standalone demand

Reason:

- current architecture treats features as reusable content modules
- a standalone feature page would likely cannibalize stronger hub or child page intent

### Example 5: product-page deferral

Idea:

- `metal business card for doctors`

Decision:

- do not create a page by default

Reason:

- this mixes profession intent and physical-product intent
- the default architecture should use a solution page for doctors and, later, a separate product-family page for metal business cards
- only create the hybrid page if keyword demand and SERP behavior later prove distinct intent

## Status Conventions

Recommended status values:

- `master_keywords.csv`: `new`, `mapped`, `deferred`
- `page_master.csv`: `planned`, `in_progress`, `published`
- `content_calendar.csv`: `planned`, `in_progress`, `published`

Recommended architecture values:

- `lifecycle_stage`: `launch_core`, `launch_secondary`, `later_support`
- `publish_wave`: `launch`, `post_launch_q1`, `post_launch_q2`, `later`

## Failure Cases To Avoid

- creating separate pages for `digital business card india` and `digital visiting card india`
- using excluded keyword variants as if they were approved canonical rows
- forcing unsupported professions into a generic category page just to “map everything”
- turning every keyword variation into a blog post
- mapping comparison keywords into category or hub pages
- creating feature-only pages when the intent is already owned by a hub or child page
- adding blog topics that do not point back to a commercial page
- creating backlinks for pages that do not exist in `page_master.csv`

## Done Criteria

A mapping task is complete only when:

- the keyword exists in `master_keywords.csv`
- the canonical page exists in `page_master.csv`
- the keyword is mapped once in `page_keyword_map.csv`
- the content task exists in `content_calendar.csv`
- the chosen page does not conflict with another page's primary intent

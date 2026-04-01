# ProfileTap Page Architecture

## Fixed Launch Architecture

The launch site consists of 1 homepage + 6 solution hubs + child pages.

### Homepage
- `/` -- owns broad platform positioning, lists the full 12-feature inventory once

### 6 Solution Hubs
- `/business-identity` -- business identity management platform
- `/creator-identity` -- personal branding platform India
- `/family-safety-profile` -- family safety profile
- `/pet-id-profile` -- pet ID tag QR code
- `/travel-profile` -- travel QR code
- `/vehicle-profile` -- vehicle QR code

### Hub-to-Child Page Relationships

#### Business Hub (`/business-identity`) -- 16 child pages
Category pages:
- `/digital-business-card-india` (P1, post_launch_q1)
- `/nfc-business-card-india` (P1, post_launch_q1)
- `/qr-business-card` (P1, post_launch_q1)
- `/ai-review-assist` (P2, post_launch_q2)
- `/google-review-management` (P2, post_launch_q2)

Use-case pages:
- `/digital-business-card-for-doctors` (P1, post_launch_q2)
- `/digital-business-card-for-real-estate-agents` (P1, post_launch_q2)
- `/digital-business-card-for-freelancers` (P1, post_launch_q2)

Comparison pages:
- `/hihello-alternative-india` (P1, post_launch_q1)
- `/popl-alternative-india` (P1, post_launch_q1)
- `/taponn-alternative` (P1, post_launch_q1)
- `/tapmo-alternative` (P1, post_launch_q1)
- `/blinq-alternative` (P2, post_launch_q2)
- `/profiletap-vs-hihello` (P2, post_launch_q2)
- `/profiletap-vs-tapmo` (P2, post_launch_q2)

Blog pages:
- `/blog/nfc-business-card-vs-qr-code` (P3, later)
- `/blog/paper-vs-digital-business-card` (P3, later)
- `/blog/best-digital-business-card-for-doctors-india` (P3, later)
- `/blog/how-to-create-digital-business-card` (P3, later)

#### Creator Hub (`/creator-identity`) -- 2 child pages
- `/digital-business-card-for-creators` (P2, post_launch_q1)
- `/linktree-alternative-for-creators` (P2, post_launch_q2)

#### Family Safety Hub (`/family-safety-profile`) -- 1 child page
- `/emergency-qr-code` (P2, post_launch_q2)

#### Pet Hub (`/pet-id-profile`) -- 1 child page
- `/lost-and-found-qr-tag` (P2, post_launch_q2)

#### Travel Hub (`/travel-profile`) -- 1 child page
- `/qr-luggage-tag` (P3, later)

#### Vehicle Hub (`/vehicle-profile`) -- 1 child page
- `/vehicle-qr-code-sticker` (P2, post_launch_q2)

## Page Type Definitions

### `homepage`
- Owns broad brand or platform-defining commercial positioning
- Lists the full 12-feature inventory once
- Routes users into launch hubs
- Current: `/` with primary keyword `smart identity platform`

### `solution_hub`
- Top-level launch page organizing the product by audience or life category
- Embeds relevant feature subset only (not the full 12)
- May exist before a finalized primary keyword
- Current: 6 hub pages

### `category`
- Broad transactional product demand where the user seeks a solution category
- Examples: `/digital-business-card-india`, `/nfc-business-card-india`, `/qr-business-card`
- Covers solution-category demand, NOT physical product-family buying intent

### `use_case`
- Profession, vertical, or audience-specific workflow page
- Examples: `/digital-business-card-for-doctors`, `/digital-business-card-for-creators`
- Requires dedicated proof, CTA, and audience-specific examples

### `comparison`
- Competitor or explicit alternative/switch intent
- Two subtypes: alternative pages (`/hihello-alternative-india`) and vs pages (`/profiletap-vs-hihello`)
- Comparison keywords must NEVER be merged into category or hub pages

### `blog`
- Educational, comparative, or early-stage informational content
- Must support a commercial page (has `parent_page_slug`)
- Examples: `/blog/nfc-business-card-vs-qr-code`, `/blog/how-to-create-digital-business-card`

### `product_family` (future, not yet active)
- Physical product buying pages under `/products/...`
- Reserved page_type, not yet in `page_master.csv`

## Feature Placement Rules by Page Type

### Homepage (`/`)
Full 12-feature inventory:
`digital_profiles`, `nfc_sharing`, `qr_sharing`, `ai_review_assist`, `analytics`, `account_collaborators`, `multi_account_team_management`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library`, `advanced_creator_analytics`

### Business Hub (`/business-identity`) -- 11 features
All EXCEPT `advanced_creator_analytics`:
`digital_profiles`, `nfc_sharing`, `qr_sharing`, `ai_review_assist`, `analytics`, `account_collaborators`, `multi_account_team_management`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library`

### Creator Hub (`/creator-identity`) -- 10 features
Drops masking, adds creator analytics:
`digital_profiles`, `nfc_sharing`, `qr_sharing`, `ai_review_assist`, `analytics`, `account_collaborators`, `multi_account_team_management`, `multi_profile_type_profiles`, `theme_library`, `advanced_creator_analytics`

### Family Safety Hub (`/family-safety-profile`) -- 6 features
`digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library`

### Pet Hub (`/pet-id-profile`) -- 4 features (minimal)
`digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `theme_library`

### Travel Hub (`/travel-profile`) -- 6 features
`digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library`

### Vehicle Hub (`/vehicle-profile`) -- 6 features
`digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library`

### Child Page Inheritance
- Category pages inherit their parent hub's feature set (may drop some)
- Use-case pages inherit only features that support conversion for that audience
- Comparison pages surface only features relevant to the switch decision
- Blog pages mention features only where they support the informational intent

## Product Catalog Layer Rules

Two parallel commercial layers are planned:
1. Solution pages: hubs, categories, use cases, comparisons (active now)
2. Product pages: physical product-family buying pages (documented, not active)

Activation criteria for product pages:
- Keyword validation proves distinct physical-product buying intent
- SERP behavior shows product results, not solution results
- Product-family page can be separated from solution page by intent

Reserved fields for future product pages:
- `page_type=product_family`
- `page_group=product_catalog`
- `page_subtype`
- `variant_strategy`
- `commercial_model=physical_product`

Key overlap areas requiring intent separation:
- `pet tags` (product) vs `pet ID profile` (solution)
- `luggage card` (product) vs `qr luggage tag` (solution)
- `vehicle sticker` (product) vs `vehicle qr code sticker` (solution)
- `google review card` (product) vs `ai review assist` / `google review management` (solution)

## Anti-Cannibalization Decision Tree

Before creating any new page, answer these questions in order:

1. Does a page already target the same solution with minor wording changes?
   - YES: Map keyword to existing page as secondary variant. STOP.
2. Is the keyword better served by an existing hub or child page under the same hub?
   - YES: Add as secondary keyword on that page. STOP.
3. Is the audience modifier strong enough to justify a dedicated use-case page?
   - Only if: profession/vertical has distinct pain points, proof points, and CTA
   - Approved professions: doctors, real estate agents, freelancers, creators
   - NOT approved by default: lawyers, accountants, consultants, etc.
4. Is this a comparison keyword?
   - YES: Must live on a dedicated comparison page, never on a category or hub page.
5. Is the query informational?
   - YES: Create as blog with `parent_page_slug` pointing to commercial parent. Never as a standalone money page.
6. Is this a feature block?
   - YES: Embed inside hub or child page via `feature_set`. No standalone feature page.
7. Is this a physical-product intent?
   - YES: Document for future `/products/...` area. Do not add to `page_master.csv` yet.

## CSV File Contracts

### `page_master.csv` Column Schema
`page_slug`, `page_type`, `page_group`, `parent_page_slug`, `hub`, `page_title`, `primary_keyword`, `primary_intent`, `target_market`, `target_language`, `funnel_stage`, `conversion_goal`, `feature_set`, `pricing_visibility`, `primary_cta`, `owner`, `status`, `lifecycle_stage`, `publish_wave`, `publish_date`, `last_updated`, `next_refresh`, `notes`

### `execution_seo_master.csv` Column Schema
`page_slug`, `page_type`, `page_group`, `hub`, `primary_keyword`, `secondary_keywords`, `search_intent`, `funnel_stage`, `market`, `priority`, `publish_wave`, `feature_set`, `pricing_visibility`, `keyword_family_notes`, `status`

### `content_calendar.csv` Column Schema
`content_id`, `page_slug`, `page_group`, `hub`, `title`, `content_type`, `parent_page_slug`, `parent_keyword_family`, `content_role`, `cluster_name`, `target_keyword`, `target_market`, `target_language`, `funnel_stage`, `priority`, `feature_set`, `pricing_visibility`, `primary_internal_link_target`, `secondary_internal_link_targets`, `serp_intent_type`, `refresh_priority`, `owner`, `status`, `brief_status`, `due_date`, `publish_date`, `refresh_date`, `publish_wave`, `notes`

## Naming Conventions for Slugs

- Use lowercase with hyphens: `/digital-business-card-india`
- Include market modifier when India-specific: `-india` suffix
- Use `for-` prefix for profession/audience pages: `/digital-business-card-for-doctors`
- Comparison alternative pages: `/{competitor}-alternative` or `/{competitor}-alternative-india`
- Comparison vs pages: `/profiletap-vs-{competitor}`
- Blog pages: `/blog/{topic-slug}`
- Future product pages: `/products/{product-family-slug}`

## Page Status Lifecycle

| Status | Meaning |
| --- | --- |
| `planned` | Page mapped in architecture, no content work started |
| `in_progress` | Brief created or content being written |
| `published` | Page is live on site |
| `refresh_needed` | Page is live but requires update |
| `needs_validation` | Architecture row exists but keyword or intent needs confirmation |

Lifecycle stages for planning:
- `launch_core`: homepage + 6 solution hubs (publish_wave: `launch`)
- `launch_secondary`: category, use-case, and comparison child pages (publish_wave: `post_launch_q1` or `post_launch_q2`)
- `later_support`: blog and support content (publish_wave: `later`)

## Execution Phases

### Phase 1: Launch Architecture (wave: `launch`)
Homepage + 6 solution hubs = 7 pages

### Phase 2: Business and Creator Child Pages (wave: `post_launch_q1`)
`/digital-business-card-india`, `/nfc-business-card-india`, `/qr-business-card`, `/digital-business-card-for-creators`, `/hihello-alternative-india`, `/popl-alternative-india`, `/taponn-alternative`, `/tapmo-alternative`

### Phase 3: Deeper Child Pages (wave: `post_launch_q2`)
`/digital-business-card-for-doctors`, `/digital-business-card-for-real-estate-agents`, `/digital-business-card-for-freelancers`, `/ai-review-assist`, `/google-review-management`, `/blinq-alternative`, `/profiletap-vs-hihello`, `/profiletap-vs-tapmo`, `/linktree-alternative-for-creators`, `/emergency-qr-code`, `/lost-and-found-qr-tag`, `/vehicle-qr-code-sticker`

### Phase 4: Support Content (wave: `later`)
`/qr-luggage-tag`, `/blog/nfc-business-card-vs-qr-code`, `/blog/paper-vs-digital-business-card`, `/blog/best-digital-business-card-for-doctors-india`, `/blog/how-to-create-digital-business-card`

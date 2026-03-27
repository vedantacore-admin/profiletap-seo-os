# ProfileTap Master Context

## Product Definition

ProfileTap is a smart identity management platform. It is NOT just an NFC card tool or a link-in-bio replacement. The platform enables users to create, share, and manage digital identity profiles across multiple life contexts using NFC cards, QR codes, and smart profile pages.

Core capability areas:
- Digital business cards using NFC and QR
- Smart profile pages for business and personal identity
- Multi-use identity for creators, families, pets, travel, and vehicles
- Analytics, AI-assisted review support, and privacy features

## Canonical Feature Inventory (12 Features)

These are the only approved feature tokens. Use tokens in CSVs; use human labels in briefs and page copy.

| Token | Human Label | Description |
| --- | --- | --- |
| `digital_profiles` | Digital profiles | Broad profile creation and sharing foundation |
| `nfc_sharing` | NFC sharing | Tap-based profile sharing via NFC-enabled cards |
| `qr_sharing` | QR sharing | Scan-based profile access via QR codes |
| `ai_review_assist` | AI review assist | Review support and AI-assisted review workflows |
| `analytics` | Analytics | General engagement and interaction analytics |
| `account_collaborators` | Manage account collaborators | Multiple collaborators helping manage one account |
| `multi_account_team_management` | Manage multiple accounts / teams | Team, business, or multi-account management |
| `multi_profile_type_profiles` | Multi-profile / multi-type profiles | Different profiles for different identity needs |
| `call_masking` | Call masking | Privacy layer for phone sharing |
| `whatsapp_masking` | WhatsApp masking | Privacy layer for WhatsApp sharing |
| `theme_library` | Wide range of themes | Theme and presentation customization |
| `advanced_creator_analytics` | Advanced analytics for creators | Creator-specific deeper analytics, likely plan-sensitive |

Rules for feature tokens:
- Use canonical tokens in all CSV files
- Use human-facing labels in briefs and page copy
- Do not create new near-duplicate tokens for wording variations
- If a feature is plan-sensitive, capture that in `pricing_visibility`, not in a new feature token
- `advanced_creator_analytics` is creator-specific and likely subscription-sensitive
- Masking features are privacy tools, not separate privacy-page intents
- Collaboration and team management appear on business and creator pages, not safety-led hubs

## Market Positioning

- Primary market: India
- Secondary market: Global English demand
- Operating assumption: India transactional demand and India-focused competitor comparisons produce the fastest commercial SEO wins
- The launch architecture must already reflect the broader platform, not just the India-first commercial push

India-first messaging rules:
- Use Indian business language where natural on India-targeted pages
- Emphasize India market explicitly on pages with `market=IN` (e.g., `/digital-business-card-india`, `/hihello-alternative-india`)
- Pages with `market=IN+GLOBAL` should lead with universal value, with India proof points secondary
- Pricing and plan references should be in INR for India pages, neutral for global pages

## 6 Segments / Hubs

| Hub Slug | Hub Name | Primary Audience | Page Count |
| --- | --- | --- | --- |
| `platform` | Platform (homepage) | All users | 1 |
| `business` | Business Identity | Professionals, SMBs, enterprises | 17+ pages |
| `creator` | Creator Identity | Influencers, bloggers, YouTubers | 3+ pages |
| `family_safety` | Family Safety | Parents, schools, caregivers | 2+ pages |
| `pet` | Pet ID | Pet owners | 2+ pages |
| `travel` | Travel Profile | Travelers, tourists | 2+ pages |
| `vehicle` | Vehicle Profile | Vehicle owners, fleet managers | 2+ pages |

## Hub-to-Feature Mapping

| Hub | Feature Count | Features |
| --- | --- | --- |
| `platform` (homepage) | 12 | All 12 features |
| `business` | 11 | All except `advanced_creator_analytics` |
| `creator` | 10 | All except `call_masking` and `whatsapp_masking`; adds `advanced_creator_analytics` |
| `family_safety` | 6 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library` |
| `pet` | 4 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `theme_library` |
| `travel` | 6 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library` |
| `vehicle` | 6 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library` |

## Competitor Landscape

### Direct Competitors

| Competitor | Positioning | Market Focus | Key Comparison Page |
| --- | --- | --- | --- |
| HiHello | Digital business card app | Global, some India | `/hihello-alternative-india`, `/profiletap-vs-hihello` |
| Popl | NFC-first digital business card | Global | `/popl-alternative-india` |
| Blinq | Digital business card platform | Global | `/blinq-alternative` |
| TapOnn | NFC business card India | India | `/taponn-alternative` |
| TapMo | NFC/digital card India | India | `/tapmo-alternative`, `/profiletap-vs-tapmo` |

### Indirect Competitors

| Competitor | Positioning | Why Indirect | Key Comparison Page |
| --- | --- | --- | --- |
| Linktree | Link-in-bio tool | Creators use it for identity, but it lacks NFC/QR/identity features | `/linktree-alternative-for-creators` |
| Beacons | Creator link-in-bio + monetization | Overlaps with creator identity, but narrow | None yet |
| Carrd | Single-page website builder | Some use as digital card, but no identity features | None yet |

### Strategic Differentiation

ProfileTap differentiators vs all competitors:
- Multi-use identity across 6 life categories (not just business)
- India-first market with INR pricing and local language support
- AI review assist built into the platform
- Call masking and WhatsApp masking for privacy
- Multi-profile types (business, personal, pet, vehicle, travel, family on one account)
- Physical product ecosystem (NFC cards, QR tags, stickers, pet tags)
- Team and collaborator management for organizations

## Product Catalog Families (9 Physical Products)

These are documented but NOT yet active in `page_master.csv`. Future `/products/...` catalog area.

| Product Family | Future Slug | Related Hub |
| --- | --- | --- |
| Metal business cards | `/products/metal-business-cards` | business |
| Wooden NFC cards | `/products/wooden-nfc-cards` | business |
| PVC business cards | `/products/pvc-business-cards` | business |
| Business standees | `/products/business-standees` | business |
| Keychains | `/products/keychains` | business |
| Pet tags | `/products/pet-tags` | pet |
| Google review cards | `/products/google-review-cards` | business |
| Travel safety kit / luggage card | `/products/luggage-cards` | travel |
| Vehicle sticker | `/products/vehicle-stickers` | vehicle |

Product-intent rules:
- Product pages own buyable physical-product intent
- Solution pages own use-case, workflow, and identity intent
- Do not add product rows to `page_master.csv` until keyword validation and page decisions are finalized
- Do not create profession-specific product pages like `metal business card for doctors` by default

## Brand Voice Guidelines

- Professional but accessible: avoid jargon, but maintain authority
- Technology-forward: lead with smart platform capabilities, not just hardware
- India-market-aware: use Indian business context naturally (INR, Indian professions, Indian cities)
- Platform-first framing: always position as smart identity management platform, not "NFC card company"
- Feature-embedded: features are selling points within pages, not standalone product pitches
- Conversion-focused: every page exists to drive `create_profile` or `assist_category_conversion`
- Anti-patterns to avoid:
  - Do not reduce ProfileTap to "just an NFC card tool"
  - Do not use "digital visiting card" as the primary framing (it is a secondary keyword variant)
  - Do not promise features without checking `pricing_visibility`
  - Do not use raw feature tokens like `multi_profile_type_profiles` in customer-facing copy

## Key Repository Files

- `data/keywords/raw_keyword_bank.csv` -- retained research inventory
- `data/keywords/execution_seo_master.csv` -- canonical page-to-keyword mapping
- `data/pages/page_master.csv` -- master page inventory
- `data/content/content_calendar.csv` -- content production queue
- `data/backlinks/backlink_targets.csv` -- backlink prospect list
- `data/backlinks/outreach_tracker.csv` -- outreach execution tracker
- `docs/02-seo-strategy.md` -- high-level SEO strategy
- `sop/page-mapping-process.md` -- page mapping rules and anti-cannibalization
- `briefs/templates/page-brief-template.md` -- brief template
- `prompts/content-brief-prompt.md` -- prompt for generating briefs

## Operating Guardrails

1. One keyword intent maps to one page only
2. No new page is created without checking existing mapped intent
3. No content item is added without a target keyword or planned architecture row
4. Every backlink target must support an existing page slug
5. India commercial demand outranks global top-of-funnel traffic until core pages are live
6. Comparisons and blogs strengthen commercial pages, never cannibalize them
7. No standalone feature pages unless keyword research proves distinct intent
8. Features are embedded modules, not standalone SEO pages
9. Product-family pages stay documented until keyword validation is complete
10. Frame ProfileTap as a smart identity platform in all copy and briefs

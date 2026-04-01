# Segment Feature Matrix

This extraction treats "segments" as the canonical `hub` values in `data/keywords/execution_seo_master.csv`.

Source of truth used:

- `data/keywords/execution_seo_master.csv` for current page-to-segment feature coverage
- `docs/02-seo-strategy.md` and `README.md` for canonical feature labels

## Canonical Feature Inventory

| Token | Label |
| --- | --- |
| `digital_profiles` | Digital profiles |
| `nfc_sharing` | NFC sharing |
| `qr_sharing` | QR sharing |
| `ai_review_assist` | AI review assist |
| `analytics` | Analytics |
| `account_collaborators` | Manage account collaborators |
| `multi_account_team_management` | Manage multiple accounts / teams |
| `multi_profile_type_profiles` | Multi-profile / multi-type profiles |
| `call_masking` | Call masking |
| `whatsapp_masking` | WhatsApp masking |
| `theme_library` | Wide range of themes |
| `advanced_creator_analytics` | Advanced analytics for creators |

## Segment Summary

| Segment | Feature count | Feature tokens |
| --- | ---: | --- |
| `platform` | 12 | `digital_profiles`, `nfc_sharing`, `qr_sharing`, `ai_review_assist`, `analytics`, `account_collaborators`, `multi_account_team_management`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library`, `advanced_creator_analytics` |
| `business` | 11 | `digital_profiles`, `nfc_sharing`, `qr_sharing`, `ai_review_assist`, `analytics`, `account_collaborators`, `multi_account_team_management`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library` |
| `creator` | 10 | `digital_profiles`, `nfc_sharing`, `qr_sharing`, `ai_review_assist`, `analytics`, `account_collaborators`, `multi_account_team_management`, `multi_profile_type_profiles`, `theme_library`, `advanced_creator_analytics` |
| `family_safety` | 6 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library` |
| `pet` | 4 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `theme_library` |
| `travel` | 6 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library` |
| `vehicle` | 6 | `digital_profiles`, `qr_sharing`, `multi_profile_type_profiles`, `call_masking`, `whatsapp_masking`, `theme_library` |

## Segment Detail

### `platform`

Pages:

- `/`

Features:

- `digital_profiles`
- `nfc_sharing`
- `qr_sharing`
- `ai_review_assist`
- `analytics`
- `account_collaborators`
- `multi_account_team_management`
- `multi_profile_type_profiles`
- `call_masking`
- `whatsapp_masking`
- `theme_library`
- `advanced_creator_analytics`

### `business`

Pages:

- `/business-identity`
- `/digital-business-card-india`
- `/nfc-business-card-india`
- `/qr-business-card`
- `/digital-business-card-for-doctors`
- `/digital-business-card-for-real-estate-agents`
- `/digital-business-card-for-freelancers`
- `/hihello-alternative-india`
- `/popl-alternative-india`
- `/tapmo-alternative`
- `/profiletap-vs-hihello`
- `/profiletap-vs-tapmo`
- `/blog/what-is-digital-business-card`
- `/blog/how-nfc-business-cards-work`
- `/blog/how-qr-code-works`
- `/blog/nfc-vs-qr-business-card`
- `/blog/digital-business-card-examples`

Features used across the segment:

- `digital_profiles`
- `nfc_sharing`
- `qr_sharing`
- `ai_review_assist`
- `analytics`
- `account_collaborators`
- `multi_account_team_management`
- `multi_profile_type_profiles`
- `call_masking`
- `whatsapp_masking`
- `theme_library`

### `creator`

Pages:

- `/creator-identity`
- `/digital-business-card-for-creators`
- `/linktree-alternative-for-creators`

Features used across the segment:

- `digital_profiles`
- `nfc_sharing`
- `qr_sharing`
- `ai_review_assist`
- `analytics`
- `account_collaborators`
- `multi_account_team_management`
- `multi_profile_type_profiles`
- `theme_library`
- `advanced_creator_analytics`

### `family_safety`

Pages:

- `/family-safety-profile`
- `/emergency-qr-code`

Features used across the segment:

- `digital_profiles`
- `qr_sharing`
- `multi_profile_type_profiles`
- `call_masking`
- `whatsapp_masking`
- `theme_library`

### `pet`

Pages:

- `/pet-id-profile`
- `/lost-and-found-qr-tag`

Features used across the segment:

- `digital_profiles`
- `qr_sharing`
- `multi_profile_type_profiles`
- `theme_library`

### `travel`

Pages:

- `/travel-profile`
- `/qr-luggage-tag`

Features used across the segment:

- `digital_profiles`
- `qr_sharing`
- `multi_profile_type_profiles`
- `call_masking`
- `whatsapp_masking`
- `theme_library`

### `vehicle`

Pages:

- `/vehicle-profile`
- `/vehicle-qr-code-sticker`

Features used across the segment:

- `digital_profiles`
- `qr_sharing`
- `multi_profile_type_profiles`
- `call_masking`
- `whatsapp_masking`
- `theme_library`

## Quick Read

- Homepage/platform is the only place that carries the full 12-feature inventory.
- Business is the broadest operating segment after the homepage; it includes every feature except `advanced_creator_analytics`.
- Creator keeps most business-style capabilities, drops masking, and adds `advanced_creator_analytics`.
- Family, travel, and vehicle share the same six-feature utility/privacy bundle.
- Pet is the leanest segment and excludes masking, NFC, analytics, AI review assist, collaborators, and team management.

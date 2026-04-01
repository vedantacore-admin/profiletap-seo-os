#!/usr/bin/env python3
import csv
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_CSV = Path("/Users/hariomshah/Downloads/SEO Master Sheet - ProfileTap - SEO Master Sheet_temp.csv")
RAW_OUT = REPO_ROOT / "data/keywords/raw_keyword_bank.csv"
EXEC_OUT = REPO_ROOT / "data/keywords/execution_seo_master.csv"

CITIES = [
    "mumbai",
    "delhi",
    "bangalore",
    "bengaluru",
    "pune",
    "hyderabad",
    "chennai",
    "kolkata",
    "ahmedabad",
    "jaipur",
    "noida",
    "gurgaon",
    "gurugram",
]

XLSX_NS = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

SHEET_CATEGORY_MAP = {
    "Identity Platform": "Platform",
    "Travel Tags": "Use Case",
    "AI Assist": "AI",
    "Google reviews": "Business",
    "Pet": "Use Case",
    "Family&Child": "Use Case",
    "Vehicle": "Use Case",
}

NON_NFC_QR_FEATURES = [
    "ai review",
    "analytics",
    "call masking",
    "whatsapp masking",
]

SELECTED_PROF_TO_SLUG = OrderedDict(
    [
        ("doctors", "/digital-business-card-for-doctors"),
        ("real estate agents", "/digital-business-card-for-real-estate-agents"),
        ("freelancers", "/digital-business-card-for-freelancers"),
        ("creators", "/digital-business-card-for-creators"),
        ("influencers", "/digital-business-card-for-creators"),
        ("youtubers", "/digital-business-card-for-creators"),
        ("bloggers", "/digital-business-card-for-creators"),
    ]
)

ALL_PROFESSIONS = [
    "doctors",
    "dentists",
    "lawyers",
    "chartered accountants",
    "consultants",
    "freelancers",
    "real estate agents",
    "architects",
    "designers",
    "photographers",
    "coaches",
    "gym trainers",
    "salon owners",
    "restaurant owners",
    "insurance agents",
    "teachers",
    "influencers",
    "youtubers",
    "bloggers",
    "startup founders",
    "marketers",
    "engineers",
    "event planners",
    "travel agents",
    "financial advisors",
    "brokers",
    "interior designers",
    "builders",
    "exporters",
    "importers",
    "creators",
]

PRIMARY_BY_SLUG = {
    "/digital-business-card-for-doctors": "digital business card for doctors",
    "/digital-business-card-for-real-estate-agents": "digital business card for real estate agents",
    "/digital-business-card-for-freelancers": "digital business card for freelancers",
    "/digital-business-card-for-creators": "digital business card for creators",
}

CANON_PRIORITY = {
    "/": "P1",
    "/business-identity": "P1",
    "/creator-identity": "P2",
    "/family-safety-profile": "P3",
    "/pet-id-profile": "P2",
    "/travel-profile": "P3",
    "/vehicle-profile": "P3",
    "/digital-business-card-india": "P1",
    "/nfc-business-card-india": "P1",
    "/qr-business-card": "P1",
    "/ai-review-assist": "P2",
    "/google-review-management": "P2",
    "/digital-business-card-for-doctors": "P1",
    "/digital-business-card-for-real-estate-agents": "P1",
    "/digital-business-card-for-freelancers": "P1",
    "/digital-business-card-for-creators": "P2",
    "/hihello-alternative-india": "P1",
    "/popl-alternative-india": "P1",
    "/tapmo-alternative": "P1",
    "/profiletap-vs-hihello": "P2",
    "/profiletap-vs-tapmo": "P2",
    "/linktree-alternative-for-creators": "P2",
    "/emergency-qr-code": "P2",
    "/lost-and-found-qr-tag": "P2",
    "/vehicle-qr-code-sticker": "P2",
    "/qr-luggage-tag": "P3",
    "/blog/what-is-digital-business-card": "P3",
    "/blog/how-nfc-business-cards-work": "P3",
    "/blog/how-qr-code-works": "P3",
    "/blog/nfc-vs-qr-business-card": "P3",
    "/blog/digital-business-card-examples": "P3",
}

PAGE_DEFS = OrderedDict(
    [
        (
            "/",
            dict(
                page_type="homepage",
                page_group="homepage",
                hub="platform",
                primary_keyword="smart identity platform",
                search_intent="commercial",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="launch",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library|advanced_creator_analytics",
                pricing_visibility="contextual",
                keyword_family_notes="Platform positioning family covering identity platform and digital profile platform terms.",
                status="planned",
            ),
        ),
        (
            "/business-identity",
            dict(
                page_type="solution_hub",
                page_group="solution_hub",
                hub="business",
                primary_keyword="business identity management platform",
                search_intent="commercial",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="launch",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Architecture-led business hub seeded from business identity platform terms.",
                status="planned",
            ),
        ),
        (
            "/creator-identity",
            dict(
                page_type="solution_hub",
                page_group="solution_hub",
                hub="creator",
                primary_keyword="personal branding platform india",
                search_intent="commercial",
                funnel_stage="MOFU",
                market="IN",
                publish_wave="launch",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|multi_profile_type_profiles|theme_library|advanced_creator_analytics",
                pricing_visibility="contextual",
                keyword_family_notes="Best current creator-hub family from the raw sheet until broader creator terms are added.",
                status="planned",
            ),
        ),
        (
            "/family-safety-profile",
            dict(
                page_type="solution_hub",
                page_group="solution_hub",
                hub="family_safety",
                primary_keyword="family safety profile",
                search_intent="commercial",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="launch",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Architecture-led launch hub; current sheet mostly supports child utility intent rather than a distinct broad family keyword.",
                status="needs_validation",
            ),
        ),
        (
            "/pet-id-profile",
            dict(
                page_type="solution_hub",
                page_group="solution_hub",
                hub="pet",
                primary_keyword="pet id tag qr code",
                search_intent="transactional",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="launch",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Pet identity hub seeded from pet QR tag and pet ID tag phrasing; lost-and-found utility terms stay separate.",
                status="planned",
            ),
        ),
        (
            "/travel-profile",
            dict(
                page_type="solution_hub",
                page_group="solution_hub",
                hub="travel",
                primary_keyword="travel qr code",
                search_intent="transactional",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="launch",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Travel identity hub seeded from travel QR code and digital travel profile phrasing.",
                status="needs_validation",
            ),
        ),
        (
            "/vehicle-profile",
            dict(
                page_type="solution_hub",
                page_group="solution_hub",
                hub="vehicle",
                primary_keyword="vehicle qr code",
                search_intent="transactional",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="launch",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Vehicle identity hub seeded from vehicle QR code, RC QR code, and automotive QR phrasing.",
                status="needs_validation",
            ),
        ),
        (
            "/digital-business-card-india",
            dict(
                page_type="category",
                page_group="category",
                hub="business",
                primary_keyword="digital business card india",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q1",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Owns digital business card, digital visiting card, virtual business card, and most adjective/city variants.",
                status="planned",
            ),
        ),
        (
            "/nfc-business-card-india",
            dict(
                page_type="category",
                page_group="category",
                hub="business",
                primary_keyword="nfc business card india",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q1",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Owns NFC business card family and related adjective/city variants.",
                status="planned",
            ),
        ),
        (
            "/qr-business-card",
            dict(
                page_type="category",
                page_group="category",
                hub="business",
                primary_keyword="qr business card",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="post_launch_q1",
                feature_set="digital_profiles|qr_sharing|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Owns QR business card and QR code business card family.",
                status="planned",
            ),
        ),
        (
            "/ai-review-assist",
            dict(
                page_type="category",
                page_group="category",
                hub="business",
                primary_keyword="ai review management",
                search_intent="commercial",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Business review-assist family for AI-led review workflows and QR-driven review capture support.",
                status="planned",
            ),
        ),
        (
            "/google-review-management",
            dict(
                page_type="category",
                page_group="category",
                hub="business",
                primary_keyword="google review management",
                search_intent="commercial",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Business review-management family for Google review growth, request, and local-SEO workflow intent.",
                status="planned",
            ),
        ),
        (
            "/digital-business-card-for-doctors",
            dict(
                page_type="use_case",
                page_group="use_case",
                hub="business",
                primary_keyword="digital business card for doctors",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Doctor profession family; NFC/QR/adjective variants merge here.",
                status="planned",
            ),
        ),
        (
            "/digital-business-card-for-real-estate-agents",
            dict(
                page_type="use_case",
                page_group="use_case",
                hub="business",
                primary_keyword="digital business card for real estate agents",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Real estate profession family; NFC/QR/adjective variants merge here.",
                status="planned",
            ),
        ),
        (
            "/digital-business-card-for-freelancers",
            dict(
                page_type="use_case",
                page_group="use_case",
                hub="business",
                primary_keyword="digital business card for freelancers",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|multi_account_team_management|multi_profile_type_profiles|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Freelancer profession family; NFC/QR/adjective variants merge here.",
                status="planned",
            ),
        ),
        (
            "/digital-business-card-for-creators",
            dict(
                page_type="use_case",
                page_group="use_case",
                hub="creator",
                primary_keyword="digital business card for creators",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="post_launch_q1",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|ai_review_assist|analytics|account_collaborators|multi_account_team_management|multi_profile_type_profiles|theme_library|advanced_creator_analytics",
                pricing_visibility="contextual",
                keyword_family_notes="Creator profession family; influencer, blogger, and youtuber variants merge here.",
                status="planned",
            ),
        ),
        (
            "/hihello-alternative-india",
            dict(
                page_type="comparison",
                page_group="comparison",
                hub="business",
                primary_keyword="hihello alternative india",
                search_intent="comparison",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q1",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="India-focused HiHello switch-intent family.",
                status="planned",
            ),
        ),
        (
            "/popl-alternative-india",
            dict(
                page_type="comparison",
                page_group="comparison",
                hub="business",
                primary_keyword="popl alternative india",
                search_intent="comparison",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q1",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="India-focused Popl switch-intent family.",
                status="planned",
            ),
        ),
        (
            "/tapmo-alternative",
            dict(
                page_type="comparison",
                page_group="comparison",
                hub="business",
                primary_keyword="tapmo alternative",
                search_intent="comparison",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q1",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="TapMo alternative family.",
                status="planned",
            ),
        ),
        (
            "/profiletap-vs-hihello",
            dict(
                page_type="comparison",
                page_group="comparison",
                hub="business",
                primary_keyword="profiletap vs hihello",
                search_intent="comparison",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Head-to-head comparison family separated from alternative intent.",
                status="planned",
            ),
        ),
        (
            "/profiletap-vs-tapmo",
            dict(
                page_type="comparison",
                page_group="comparison",
                hub="business",
                primary_keyword="profiletap vs tapmo",
                search_intent="comparison",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|nfc_sharing|qr_sharing|analytics|account_collaborators|multi_account_team_management|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Head-to-head comparison family separated from alternative intent.",
                status="planned",
            ),
        ),
        (
            "/linktree-alternative-for-creators",
            dict(
                page_type="comparison",
                page_group="comparison",
                hub="creator",
                primary_keyword="linktree alternative for creators",
                search_intent="comparison",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|qr_sharing|ai_review_assist|analytics|multi_profile_type_profiles|theme_library|advanced_creator_analytics",
                pricing_visibility="contextual",
                keyword_family_notes="Creator comparison family for link-in-bio replacement intent.",
                status="planned",
            ),
        ),
        (
            "/emergency-qr-code",
            dict(
                page_type="category",
                page_group="category",
                hub="family_safety",
                primary_keyword="emergency qr code",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Family/emergency utility family covering emergency-contact and medical QR phrasing; city and adjective variants merge here.",
                status="planned",
            ),
        ),
        (
            "/lost-and-found-qr-tag",
            dict(
                page_type="category",
                page_group="category",
                hub="pet",
                primary_keyword="lost and found qr tag",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Lost-item utility family; broader pet ID intent is owned separately by the pet hub.",
                status="planned",
            ),
        ),
        (
            "/vehicle-qr-code-sticker",
            dict(
                page_type="category",
                page_group="category",
                hub="vehicle",
                primary_keyword="vehicle qr code sticker",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN",
                publish_wave="post_launch_q2",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Vehicle utility family covering car, bike, parking-contact, and owner-contact QR sticker variants.",
                status="planned",
            ),
        ),
        (
            "/qr-luggage-tag",
            dict(
                page_type="category",
                page_group="category",
                hub="travel",
                primary_keyword="qr luggage tag",
                search_intent="transactional",
                funnel_stage="BOFU",
                market="IN+GLOBAL",
                publish_wave="later",
                feature_set="digital_profiles|qr_sharing|multi_profile_type_profiles|call_masking|whatsapp_masking|theme_library",
                pricing_visibility="contextual",
                keyword_family_notes="Travel utility family covering luggage, suitcase, and bag QR tag phrasing; kept separate from travel-agent business-card intent.",
                status="needs_validation",
            ),
        ),
        (
            "/blog/what-is-digital-business-card",
            dict(
                page_type="blog",
                page_group="blog",
                hub="business",
                primary_keyword="what is digital business card",
                search_intent="informational",
                funnel_stage="TOFU",
                market="IN+GLOBAL",
                publish_wave="later",
                feature_set="digital_profiles|nfc_sharing|qr_sharing",
                pricing_visibility="all_plans",
                keyword_family_notes="Support content tied to digital business card commercial family.",
                status="planned",
            ),
        ),
        (
            "/blog/how-nfc-business-cards-work",
            dict(
                page_type="blog",
                page_group="blog",
                hub="business",
                primary_keyword="how nfc business cards work",
                search_intent="informational",
                funnel_stage="TOFU",
                market="IN+GLOBAL",
                publish_wave="later",
                feature_set="digital_profiles|nfc_sharing",
                pricing_visibility="all_plans",
                keyword_family_notes="Support content tied to NFC category family.",
                status="planned",
            ),
        ),
        (
            "/blog/how-qr-code-works",
            dict(
                page_type="blog",
                page_group="blog",
                hub="business",
                primary_keyword="how qr code works",
                search_intent="informational",
                funnel_stage="TOFU",
                market="IN+GLOBAL",
                publish_wave="later",
                feature_set="digital_profiles|qr_sharing",
                pricing_visibility="all_plans",
                keyword_family_notes="Support content tied to QR category family.",
                status="planned",
            ),
        ),
        (
            "/blog/nfc-vs-qr-business-card",
            dict(
                page_type="blog",
                page_group="blog",
                hub="business",
                primary_keyword="nfc vs qr business card",
                search_intent="informational",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="later",
                feature_set="digital_profiles|nfc_sharing|qr_sharing",
                pricing_visibility="all_plans",
                keyword_family_notes="Support comparison content for NFC vs QR education.",
                status="planned",
            ),
        ),
        (
            "/blog/digital-business-card-examples",
            dict(
                page_type="blog",
                page_group="blog",
                hub="business",
                primary_keyword="digital business card examples",
                search_intent="informational",
                funnel_stage="MOFU",
                market="IN+GLOBAL",
                publish_wave="later",
                feature_set="digital_profiles|theme_library",
                pricing_visibility="all_plans",
                keyword_family_notes="Support gallery/example content for commercial category pages.",
                status="planned",
            ),
        ),
    ]
)

INFORMATIONAL_MAP = {
    "what is digital business card": "/blog/what-is-digital-business-card",
    "how nfc business cards work": "/blog/how-nfc-business-cards-work",
    "how qr code works": "/blog/how-qr-code-works",
    "nfc vs qr business card": "/blog/nfc-vs-qr-business-card",
    "digital business card examples": "/blog/digital-business-card-examples",
}

UTILITY_KEYWORD_SETS = {
    "/emergency-qr-code": {
        "primary": "emergency qr code",
        "secondary": [
            "medical emergency qr code",
            "emergency contact qr code",
            "medical qr code",
            "medical info qr code",
            "emergency medical information qr",
            "emergency profile qr code",
            "qr code for emergency contact",
        ],
    },
    "/lost-and-found-qr-tag": {
        "primary": "lost and found qr tag",
        "secondary": [
            "lost item qr tag",
            "qr lost and found tag",
            "found item return qr tag",
            "smart lost and found tag",
            "recovery qr tag",
            "return contact qr tag",
        ],
    },
    "/pet-id-profile": {
        "primary": "pet id tag qr code",
        "secondary": [
            "pet qr tag",
            "pet id qr code",
            "qr code pet tag",
            "qr code for pet identification",
            "lost pet qr tag",
            "dog qr tag",
            "cat qr tag",
            "pet emergency qr tag",
        ],
    },
    "/vehicle-qr-code-sticker": {
        "primary": "vehicle qr code sticker",
        "secondary": [
            "car qr code sticker",
            "bike qr code tag",
            "vehicle owner contact qr",
            "car owner contact qr code",
            "parking contact qr code",
            "wrong parking qr sticker",
            "emergency contact car sticker",
        ],
    },
    "/qr-luggage-tag": {
        "primary": "qr luggage tag",
        "secondary": [
            "luggage qr tag",
            "lost luggage qr tag",
            "bag qr tag",
            "suitcase qr tag",
            "smart luggage tag",
            "travel bag qr tag",
            "airport luggage qr tag",
        ],
    },
}

TRAVEL_PROFILE_TERMS = {
    "travel qr code",
    "travel digital card",
    "tourist qr code",
    "travel contact qr code",
    "travel emergency qr code",
    "travel identity card",
    "digital travel profile",
    "travel safety qr",
}

VEHICLE_PROFILE_TERMS = {
    "vehicle qr code",
    "rc qr code",
    "vehicle verification qr code",
    "vehicle details qr code",
    "car qr code",
    "automotive qr code",
    "qr code for vehicle registration",
}

AI_RELEVANT_TERMS = {
    "ai assist reviews",
    "ai review management",
    "ai reviews for business",
    "ai review qr",
    "ai review system",
    "ai reviews app",
    "ai review online",
}

FAMILY_RELEVANT_TERMS = {
    "family safety app apk",
    "family safety app kya hai",
    "family safety tags",
    "family safety tool",
    "safety tags for children",
    "children safety tags",
    "child safety tags",
    "child safe tag",
    "kids safety name tags",
    "school bag safety tags",
}

SUPPLEMENTAL_KEYWORDS = [
    {
        "Keyword": keyword,
        "Category": "Supplemental",
        "Intent": "Transactional",
        "Notes": "Supplemental utility keyword from market-language review.",
    }
    for group in UTILITY_KEYWORD_SETS.values()
    for keyword in [group["primary"], *group["secondary"]]
]

EMERGENCY_TERMS = {
    UTILITY_KEYWORD_SETS["/emergency-qr-code"]["primary"],
    *UTILITY_KEYWORD_SETS["/emergency-qr-code"]["secondary"],
}
LOST_FOUND_TERMS = {
    UTILITY_KEYWORD_SETS["/lost-and-found-qr-tag"]["primary"],
    *UTILITY_KEYWORD_SETS["/lost-and-found-qr-tag"]["secondary"],
}
PET_ID_TERMS = {
    "pet identification",
    *[UTILITY_KEYWORD_SETS["/pet-id-profile"]["primary"]],
    *UTILITY_KEYWORD_SETS["/pet-id-profile"]["secondary"],
}
VEHICLE_TERMS = {
    UTILITY_KEYWORD_SETS["/vehicle-qr-code-sticker"]["primary"],
    *UTILITY_KEYWORD_SETS["/vehicle-qr-code-sticker"]["secondary"],
}
LUGGAGE_TERMS = {
    UTILITY_KEYWORD_SETS["/qr-luggage-tag"]["primary"],
    *UTILITY_KEYWORD_SETS["/qr-luggage-tag"]["secondary"],
}

RAW_FIELDS = [
    "keyword",
    "source_category",
    "observed_intent",
    "market",
    "modifier_type",
    "root_topic",
    "canonical_keyword",
    "canonical_page_slug",
    "keep_status",
    "merge_reason",
    "notes",
    "ubersuggest_volume",
    "ubersuggest_kd",
    "ubersuggest_cpc",
    "ubersuggest_last_checked",
]

RAW_KEEP_STATUSES = {"keep_primary", "keep_secondary"}

EXEC_FIELDS = [
    "page_slug",
    "page_type",
    "page_group",
    "hub",
    "primary_keyword",
    "secondary_keywords",
    "search_intent",
    "funnel_stage",
    "market",
    "priority",
    "publish_wave",
    "feature_set",
    "pricing_visibility",
    "keyword_family_notes",
    "status",
]


def clean_keyword(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def slug_market(text: str) -> str:
    if "india" in text or any(city in text for city in CITIES):
        return "IN"
    return "IN+GLOBAL"


def modifier_type(text: str) -> str:
    if " vs " in text or "alternative" in text:
        return "comparison"
    if "near me" in text:
        return "near_me"
    if any(city in text for city in CITIES):
        return "city"
    for token in ["best", "buy", "cheap", "premium", "custom", "online", "top"]:
        if re.search(rf"\b{re.escape(token)}\b", text):
            return token
    if "india" in text:
        return "country"
    if any(prof in text for prof in ALL_PROFESSIONS):
        return "profession"
    if any(feature in text for feature in NON_NFC_QR_FEATURES):
        return "feature"
    if "nfc" in text or "qr" in text:
        return "feature"
    return "none"


def mapped(
    root_topic: str,
    canonical_keyword: str,
    canonical_page_slug: str,
    keep_status: str,
    merge_reason: str,
    notes: str = "",
):
    return {
        "root_topic": root_topic,
        "canonical_keyword": canonical_keyword,
        "canonical_page_slug": canonical_page_slug,
        "keep_status": keep_status,
        "merge_reason": merge_reason,
        "notes": notes,
    }


def map_row(row: dict) -> dict:
    keyword = clean_keyword(row["Keyword"])
    text = keyword.lower()
    category = row["Category"].strip()
    source_sheet = row.get("Source Sheet", "").strip()
    mod = modifier_type(text)

    if source_sheet == "Google reviews" or (source_sheet != "AI Assist" and ("google review" in text or "google reviews" in text)):
        return mapped(
            "google_review_management",
            "google review management",
            "/google-review-management",
            "keep_primary" if text == "google review management" else "keep_secondary",
            "google review management family",
        )

    if source_sheet == "AI Assist" and text in AI_RELEVANT_TERMS:
        return mapped(
            "ai_review_assist",
            "ai review management",
            "/ai-review-assist",
            "keep_primary" if text == "ai review management" else "keep_secondary",
            "ai review assist family",
        )

    if category == "AI" or "ai review" in text or "review assist" in text:
        return mapped(
            "ai_review_assist",
            "ai review assist",
            "",
            "defer",
            "feature-led query deferred until standalone demand is validated",
        )

    if category == "Competitor" or "alternative" in text or " vs " in text:
        if "hihello" in text:
            if "vs" in text:
                return mapped(
                    "profiletap_vs_hihello",
                    "profiletap vs hihello",
                    "/profiletap-vs-hihello",
                    "keep_primary" if text == "profiletap vs hihello" else "keep_secondary",
                    "vs family separated from alternative intent",
                )
            return mapped(
                "hihello_alternative",
                "hihello alternative india",
                "/hihello-alternative-india",
                "keep_primary" if ("india" in text and "alternative" in text) else "keep_secondary",
                "hihello alternative family",
            )
        if "popl" in text:
            return mapped(
                "popl_alternative",
                "popl alternative india",
                "/popl-alternative-india",
                "keep_primary" if ("india" in text and "alternative" in text) else "keep_secondary",
                "popl alternative family",
            )
        if "tapmo" in text:
            if "vs" in text:
                return mapped(
                    "profiletap_vs_tapmo",
                    "profiletap vs tapmo",
                    "/profiletap-vs-tapmo",
                    "keep_primary" if text == "profiletap vs tapmo" else "keep_secondary",
                    "vs family separated from alternative intent",
                )
            return mapped(
                "tapmo_alternative",
                "tapmo alternative",
                "/tapmo-alternative",
                "keep_primary" if ("tapmo" in text and "alternative" in text and "india" not in text) else "keep_secondary",
                "tapmo alternative family",
            )
        if "linktree" in text or "link in bio alternative" in text:
            return mapped(
                "linktree_alternative_for_creators",
                "linktree alternative for creators",
                "/linktree-alternative-for-creators",
                "keep_primary" if text == "linktree alternative for creators" else "keep_secondary",
                "creator comparison family",
            )
        return mapped(
            "comparison_deferred",
            "",
            "",
            "defer",
            "competitor term outside initial canonical comparison set",
        )

    if category == "Platform":
        if "creator" in text or "personal branding" in text:
            return mapped(
                "creator_identity_platform",
                "personal branding platform india",
                "/creator-identity",
                "keep_primary" if text == "personal branding platform india" else "keep_secondary",
                "creator-hub family seed",
            )
        if "business" in text or "professional" in text:
            return mapped(
                "business_identity_management_platform",
                "business identity management platform",
                "/business-identity",
                "keep_primary" if text == "business identity management platform" else "keep_secondary",
                "business identity platform variation",
            )
        if "travel" in text:
            return mapped(
                "travel_profile",
                "travel profile",
                "/travel-profile",
                "defer",
                "broad travel hub term needs demand validation",
            )
        return mapped(
            "smart_identity_platform",
            "smart identity platform",
            "/",
            "keep_primary" if text == "smart identity platform" else "keep_secondary",
            "platform family consolidation",
        )

    if category == "Discovery" or any(token in text for token in ["what is ", "how ", " examples", "guide", "explained", "for beginners"]):
        if "nfc vs qr" in text:
            return mapped(
                "nfc_vs_qr_business_card",
                "nfc vs qr business card",
                INFORMATIONAL_MAP["nfc vs qr business card"],
                "keep_primary" if text == "nfc vs qr business card" else "merge_into_primary",
                "support content family",
            )
        if "what is digital business card" in text:
            return mapped(
                "what_is_digital_business_card",
                "what is digital business card",
                INFORMATIONAL_MAP["what is digital business card"],
                "keep_primary" if text == "what is digital business card" else "merge_into_primary",
                "support content family",
            )
        if "how nfc business" in text:
            return mapped(
                "how_nfc_business_cards_work",
                "how nfc business cards work",
                INFORMATIONAL_MAP["how nfc business cards work"],
                "keep_primary" if text == "how nfc business cards work" else "merge_into_primary",
                "support content family",
            )
        if "how qr code works" in text:
            return mapped(
                "how_qr_code_works",
                "how qr code works",
                INFORMATIONAL_MAP["how qr code works"],
                "keep_primary" if text == "how qr code works" else "merge_into_primary",
                "support content family",
            )
        if "examples" in text:
            return mapped(
                "digital_business_card_examples",
                "digital business card examples",
                INFORMATIONAL_MAP["digital business card examples"],
                "keep_primary" if text == "digital business card examples" else "merge_into_primary",
                "support content family",
            )
        return mapped(
            "informational_deferred",
            "",
            "",
            "drop" if ("beginner" in text or "explained" in text) else "defer",
            "low-signal informational variant outside current support set",
        )

    if text in EMERGENCY_TERMS or "emergency qr" in text or "medical qr" in text:
        return mapped(
            "emergency_qr_code",
            "emergency qr code",
            "/emergency-qr-code",
            "keep_primary" if text == "emergency qr code" else ("keep_secondary" if text in EMERGENCY_TERMS else "merge_into_primary"),
            "family safety utility family",
        )
    if text in LOST_FOUND_TERMS or "lost and found qr tag" in text:
        return mapped(
            "lost_and_found_qr_tag",
            "lost and found qr tag",
            "/lost-and-found-qr-tag",
            "keep_primary" if text == "lost and found qr tag" else ("keep_secondary" if text in LOST_FOUND_TERMS else "merge_into_primary"),
            "pet utility family",
        )
    if text in PET_ID_TERMS or "pet identification" in text or ("pet" in text and "qr" in text and "tag" in text):
        return mapped(
            "pet_id_profile",
            "pet id tag qr code",
            "/pet-id-profile",
            "keep_primary" if text == "pet id tag qr code" else ("keep_secondary" if text in PET_ID_TERMS else "merge_into_primary"),
            "pet identity hub family",
        )
    if ("pet" in text and "qr" in text) or text in {"pet safety tag"}:
        return mapped(
            "pet_id_profile",
            "pet id tag qr code",
            "/pet-id-profile",
            "keep_secondary" if text in {"pet safety qr", "pets qr code", "pet safety tag"} else "merge_into_primary",
            "pet identity hub family",
        )
    if source_sheet == "Family&Child" and text in FAMILY_RELEVANT_TERMS:
        return mapped(
            "family_safety_profile",
            "family safety profile",
            "/family-safety-profile",
            "keep_secondary",
            "family safety hub family",
        )
    if text in TRAVEL_PROFILE_TERMS or ("travel" in text and "qr" in text):
        return mapped(
            "travel_profile",
            "travel qr code",
            "/travel-profile",
            "keep_primary" if text == "travel qr code" else ("keep_secondary" if text in TRAVEL_PROFILE_TERMS else "merge_into_primary"),
            "travel profile utility family",
        )
    if text in VEHICLE_PROFILE_TERMS:
        return mapped(
            "vehicle_profile",
            "vehicle qr code",
            "/vehicle-profile",
            "keep_primary" if text == "vehicle qr code" else "keep_secondary",
            "vehicle profile utility family",
        )
    if text in VEHICLE_TERMS or "vehicle qr code sticker" in text or "bike qr code tag" in text or "car qr code sticker" in text:
        return mapped(
            "vehicle_qr_code_sticker",
            "vehicle qr code sticker",
            "/vehicle-qr-code-sticker",
            "keep_primary" if text == "vehicle qr code sticker" else ("keep_secondary" if text in VEHICLE_TERMS else "merge_into_primary"),
            "vehicle utility family",
        )
    if text in LUGGAGE_TERMS or "qr luggage tag" in text:
        return mapped(
            "qr_luggage_tag",
            "qr luggage tag",
            "/qr-luggage-tag",
            "keep_primary" if text == "qr luggage tag" else ("keep_secondary" if text in LUGGAGE_TERMS else "merge_into_primary"),
            "travel utility family",
        )

    if "travel agents" in text:
        return mapped(
            "travel_agents_business_card",
            "",
            "",
            "defer",
            "travel-agent business intent kept separate from travel utility and deferred until page priority is confirmed",
        )

    if category == "Use Case" and any(prof in text for prof in ALL_PROFESSIONS) and not any(prof in text for prof in SELECTED_PROF_TO_SLUG):
        return mapped(
            "use_case_deferred",
            "",
            "",
            "defer",
            "profession/use-case variant outside the initial canonical execution set",
        )

    if category in {"Business", "Use Case"}:
        for prof, slug in SELECTED_PROF_TO_SLUG.items():
            if prof not in text:
                continue
            primary = PRIMARY_BY_SLUG[slug]
            if text == primary:
                keep_status = "keep_primary"
            elif mod in {"none", "profession", "feature"} and (
                "digital business card" in text or "nfc business card" in text or "qr code profile" in text
            ):
                keep_status = "keep_secondary"
            else:
                keep_status = "merge_into_primary"
            return mapped(
                primary.replace(" ", "_"),
                primary,
                slug,
                keep_status,
                f"{prof} profession family",
            )

        if text == "nfc business card india":
            return mapped("nfc_business_card", "nfc business card india", "/nfc-business-card-india", "keep_primary", "nfc business card family")
        if text in {"nfc business card", "nfc digital business card", "nfc visiting card"}:
            return mapped("nfc_business_card", "nfc business card india", "/nfc-business-card-india", "keep_secondary", "nfc business card family")
        if text == "qr business card":
            return mapped("qr_business_card", "qr business card", "/qr-business-card", "keep_primary", "qr business card family")
        if text in {"qr code business card", "qr digital business card", "qr visiting card"}:
            return mapped("qr_business_card", "qr business card", "/qr-business-card", "keep_secondary", "qr business card family")
        if text == "digital business card india":
            return mapped("digital_business_card", "digital business card india", "/digital-business-card-india", "keep_primary", "digital business card family")
        if text in {"digital business card", "digital visiting card", "virtual business card"}:
            return mapped("digital_business_card", "digital business card india", "/digital-business-card-india", "keep_secondary", "digital business card family")

        if "digital business card" in text or "digital visiting card" in text or "virtual business card" in text:
            if "nfc" in text:
                return mapped("nfc_business_card", "nfc business card india", "/nfc-business-card-india", "merge_into_primary", "nfc business card family")
            if "qr" in text:
                return mapped("qr_business_card", "qr business card", "/qr-business-card", "merge_into_primary", "qr business card family")
            return mapped("digital_business_card", "digital business card india", "/digital-business-card-india", "merge_into_primary", "digital business card family")

        if "nfc business card" in text:
            return mapped("nfc_business_card", "nfc business card india", "/nfc-business-card-india", "merge_into_primary", "nfc business card family")
        if "qr code business card" in text or "qr business card" in text:
            return mapped("qr_business_card", "qr business card", "/qr-business-card", "merge_into_primary", "qr business card family")

        if category == "Use Case":
            return mapped(
                "use_case_deferred",
                "",
                "",
                "defer",
                "profession/use-case variant outside the initial canonical execution set",
            )

    return mapped(
        "unmapped_deferred",
        "",
        "",
        "defer",
        "outside the initial canonical page inventory; hold for Ubersuggest-driven review",
    )


def load_source_rows():
    source_csv = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_SOURCE_CSV
    if source_csv.suffix.lower() == ".xlsx":
        return load_xlsx_rows(source_csv)
    with source_csv.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def xlsx_cell_value(cell, shared_strings):
    cell_type = cell.attrib.get("t")
    value = cell.find("a:v", XLSX_NS)
    if cell_type == "inlineStr":
        inline = cell.find("a:is", XLSX_NS)
        if inline is None:
            return ""
        return "".join(text.text or "" for text in inline.iterfind(".//a:t", XLSX_NS))
    if value is None:
        return ""
    raw_value = value.text or ""
    if cell_type == "s":
        return shared_strings[int(raw_value)]
    return raw_value


def choose_first(row, keys):
    for key in keys:
        value = clean_keyword(row.get(key, ""))
        if value:
            return value
    return ""


def normalize_sheet_intent(raw_category: str, cluster: str, content_type: str) -> str:
    category = raw_category.strip().lower()
    if category in {"transactional", "informational", "navigational", "commercial", "comparison"}:
        return category
    cluster_text = cluster.strip().lower()
    content_text = content_type.strip().lower()
    if "awareness" in cluster_text or "blog" in content_text or "guide" in content_text:
        return "informational"
    if "tool" in cluster_text or "tool" in content_text:
        return "navigational"
    if "conversion" in cluster_text or "landing page" in content_text or "product" in content_text:
        return "transactional"
    return "commercial"


def normalize_xlsx_row(sheet_name: str, raw_row: dict) -> dict:
    sheet_label = sheet_name.strip()
    raw_category = clean_keyword(raw_row.get("Category", ""))
    cluster = choose_first(raw_row, ["Intent Cluster", "Cluster", "Intent Type"])
    content_type = choose_first(raw_row, ["Content Type", "Best Content Strategy"])
    suggested_page = choose_first(raw_row, ["Suggested Use/Page", "Suggested Page"])
    primary_secondary = choose_first(raw_row, ["Primary/Secondary"])
    search_volume = choose_first(raw_row, ["Search Volume"])
    notes_parts = [f"source_sheet={sheet_label}"]
    if suggested_page:
        notes_parts.append(f"suggested_page={suggested_page}")
    if primary_secondary:
        notes_parts.append(f"priority_hint={primary_secondary.lower()}")
    if search_volume:
        notes_parts.append(f"volume_hint={search_volume.lower()}")
    return {
        "Keyword": clean_keyword(raw_row.get("Keyword", "")),
        "Category": SHEET_CATEGORY_MAP.get(sheet_label, "Use Case"),
        "Intent": normalize_sheet_intent(raw_category, cluster, content_type),
        "Notes": "; ".join(notes_parts),
        "Source Sheet": sheet_label,
        "Raw Category": raw_category,
        "Cluster": cluster,
        "Content Type": content_type,
        "Suggested Page": suggested_page,
        "Primary/Secondary": primary_secondary,
        "Search Volume": search_volume,
    }


def load_xlsx_rows(source_xlsx: Path):
    sheet_rows = OrderedDict()
    with zipfile.ZipFile(source_xlsx) as workbook:
        shared_strings = []
        if "xl/sharedStrings.xml" in workbook.namelist():
            root = ET.fromstring(workbook.read("xl/sharedStrings.xml"))
            for item in root.findall("a:si", XLSX_NS):
                shared_strings.append("".join(text.text or "" for text in item.iterfind(".//a:t", XLSX_NS)))

        workbook_root = ET.fromstring(workbook.read("xl/workbook.xml"))
        rels_root = ET.fromstring(workbook.read("xl/_rels/workbook.xml.rels"))
        rel_map = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels_root}

        for sheet in workbook_root.find("a:sheets", XLSX_NS):
            sheet_name = sheet.attrib["name"].strip()
            rel_id = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
            sheet_path = "xl/" + rel_map[rel_id]
            sheet_root = ET.fromstring(workbook.read(sheet_path))
            rows = sheet_root.findall(".//a:sheetData/a:row", XLSX_NS)
            if not rows:
                sheet_rows[sheet_name] = []
                continue
            header = [clean_keyword(xlsx_cell_value(cell, shared_strings)) for cell in rows[0].findall("a:c", XLSX_NS)]
            normalized_rows = []
            for row in rows[1:]:
                cells = [clean_keyword(xlsx_cell_value(cell, shared_strings)) for cell in row.findall("a:c", XLSX_NS)]
                if not any(cells):
                    continue
                record = dict(zip(header, cells))
                normalized = normalize_xlsx_row(sheet_name, record)
                if normalized["Keyword"]:
                    normalized_rows.append(normalized)
            sheet_rows[sheet_name] = normalized_rows

    return [row for rows in sheet_rows.values() for row in rows]


def load_existing_raw_rows():
    try:
        result = subprocess.run(
            ["git", "show", "HEAD:data/keywords/raw_keyword_bank.csv"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        rows = list(csv.DictReader(result.stdout.splitlines()))
    except Exception:
        if not RAW_OUT.exists():
            return []
        with RAW_OUT.open(newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))

    for row in rows:
        if "ubersuggest_volume" not in row and "semrush_volume" in row:
            row["ubersuggest_volume"] = row.get("semrush_volume", "")
        if "ubersuggest_kd" not in row and "semrush_kd" in row:
            row["ubersuggest_kd"] = row.get("semrush_kd", "")
        if "ubersuggest_cpc" not in row and "semrush_cpc" in row:
            row["ubersuggest_cpc"] = row.get("semrush_cpc", "")
        if "ubersuggest_last_checked" not in row and "semrush_last_checked" in row:
            row["ubersuggest_last_checked"] = row.get("semrush_last_checked", "")
        row.pop("semrush_volume", None)
        row.pop("semrush_kd", None)
        row.pop("semrush_cpc", None)
        row.pop("semrush_last_checked", None)
    return rows


def merge_raw_rows_with_existing(raw_rows, source_path: Path):
    if source_path.suffix.lower() != ".xlsx":
        return raw_rows

    merged = OrderedDict()
    for row in load_existing_raw_rows():
        keyword = clean_keyword(row.get("keyword", ""))
        if keyword:
            merged[keyword.lower()] = row

    for row in raw_rows:
        key = row["keyword"].lower()
        existing = merged.get(key, {})
        merged_row = dict(existing)
        merged_row.update(row)
        for metric_field in ["ubersuggest_volume", "ubersuggest_kd", "ubersuggest_cpc", "ubersuggest_last_checked"]:
            if not merged_row.get(metric_field) and existing.get(metric_field):
                merged_row[metric_field] = existing[metric_field]
        merged[key] = merged_row

    return list(merged.values())


def build_raw_rows(source_rows):
    raw_rows = []
    combined_rows = list(source_rows) + SUPPLEMENTAL_KEYWORDS
    seen_keywords = set()
    for row in combined_rows:
        keyword = clean_keyword(row["Keyword"])
        normalized_keyword = keyword.lower()
        if normalized_keyword in seen_keywords:
            continue
        seen_keywords.add(normalized_keyword)
        text = keyword.lower()
        mapping = map_row(row)
        if mapping["keep_status"] not in RAW_KEEP_STATUSES:
            continue
        raw_rows.append(
            {
                "keyword": keyword,
                "source_category": row["Category"].strip(),
                "observed_intent": row["Intent"].strip().lower(),
                "market": slug_market(text),
                "modifier_type": modifier_type(text),
                **mapping,
                "notes": mapping["notes"] or row.get("Notes", "").strip(),
                "ubersuggest_volume": "",
                "ubersuggest_kd": "",
                "ubersuggest_cpc": "",
                "ubersuggest_last_checked": "",
            }
        )
    return raw_rows


def build_secondary_keywords(raw_rows):
    family_secondaries = defaultdict(list)
    for row in raw_rows:
        slug = row["canonical_page_slug"]
        if not slug or row["keep_status"] != "keep_secondary":
            continue
        if row["keyword"].lower() == row["canonical_keyword"].lower():
            continue
        family_secondaries[slug].append(row["keyword"])

    for slug, keywords in list(family_secondaries.items()):
        seen = set()
        cleaned = []
        for keyword in keywords:
            normalized = keyword.lower()
            if normalized in seen:
                continue
            seen.add(normalized)
            cleaned.append(keyword)
        family_secondaries[slug] = cleaned[:12]

    return family_secondaries


def write_raw_bank(raw_rows):
    with RAW_OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RAW_FIELDS)
        writer.writeheader()
        writer.writerows(raw_rows)


def write_execution_master(family_secondaries):
    with EXEC_OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=EXEC_FIELDS)
        writer.writeheader()
        for slug, meta in PAGE_DEFS.items():
            row = {"page_slug": slug, **meta}
            row["priority"] = CANON_PRIORITY[slug]
            row["secondary_keywords"] = " | ".join(family_secondaries.get(slug, []))
            writer.writerow(row)


def main():
    source_path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_SOURCE_CSV
    source_rows = load_source_rows()
    raw_rows = merge_raw_rows_with_existing(build_raw_rows(source_rows), source_path)
    family_secondaries = build_secondary_keywords(raw_rows)
    write_raw_bank(raw_rows)
    write_execution_master(family_secondaries)

    print(f"source_csv={source_path}")
    print(f"raw_rows={len(raw_rows)}")
    print(f"execution_rows={len(PAGE_DEFS)}")
    print(f"keep_status={dict(Counter(row['keep_status'] for row in raw_rows))}")
    print(
        "secondary_samples="
        + str(
            {
                slug: family_secondaries.get(slug, [])[:6]
                for slug in [
                    "/",
                    "/business-identity",
                    "/creator-identity",
                    "/digital-business-card-india",
                    "/nfc-business-card-india",
                    "/qr-business-card",
                    "/digital-business-card-for-creators",
                ]
            }
        )
    )


if __name__ == "__main__":
    main()

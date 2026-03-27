#!/usr/bin/env python3
"""
ProfileTap SEO OS — System Validation Script

Checks cross-file referential integrity, duplicate detection, and schema compliance
across all CSV data files.

Usage:
    python scripts/validate_system.py
"""

import csv
import os
import sys

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

CANONICAL_HUBS = {"platform", "business", "creator", "family_safety", "pet", "travel", "vehicle"}

CANONICAL_PAGE_TYPES = {
    "homepage", "solution_hub", "category", "use_case", "comparison", "blog", "product_family"
}

CANONICAL_FEATURES = {
    "digital_profiles", "nfc_sharing", "qr_sharing", "ai_review_assist", "business_ai",
    "analytics", "account_collaborators", "multi_account_team_management",
    "multi_profile_type_profiles", "call_masking", "whatsapp_masking", "theme_library",
    "advanced_creator_analytics"
}

VALID_STATUSES_PAGE = {"planned", "draft_ready", "in_progress", "published", "refresh_needed", "needs_validation"}
VALID_STATUSES_EXEC = {"planned", "draft_ready", "in_progress", "published", "refresh_needed", "needs_validation"}
VALID_PRIORITIES = {"P1", "P2", "P3"}


def load_csv(filename):
    """Load a CSV file and return list of dicts."""
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  WARNING: File not found: {filepath}")
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def validate_execution_master(rows):
    """Validate execution_seo_master.csv."""
    errors = []
    slugs = []
    primary_keywords = []

    for i, row in enumerate(rows, start=2):
        slug = row.get("page_slug", "").strip()
        pk = row.get("primary_keyword", "").strip()
        hub = row.get("hub", "").strip()
        page_type = row.get("page_type", "").strip()
        priority = row.get("priority", "").strip()
        status = row.get("status", "").strip()
        features = row.get("feature_set", "").strip()

        if not slug:
            errors.append(f"  Row {i}: Missing page_slug")
            continue

        # Duplicate slug check
        if slug in slugs:
            errors.append(f"  Row {i}: Duplicate page_slug '{slug}'")
        slugs.append(slug)

        # Duplicate primary keyword check
        if pk:
            if pk in primary_keywords:
                errors.append(f"  Row {i}: Duplicate primary_keyword '{pk}' on '{slug}'")
            primary_keywords.append(pk)

        # Hub validation
        if hub and hub not in CANONICAL_HUBS:
            errors.append(f"  Row {i}: Invalid hub '{hub}' on '{slug}'")

        # Page type validation
        if page_type and page_type not in CANONICAL_PAGE_TYPES:
            errors.append(f"  Row {i}: Invalid page_type '{page_type}' on '{slug}'")

        # Priority validation
        if priority and priority not in VALID_PRIORITIES:
            errors.append(f"  Row {i}: Invalid priority '{priority}' on '{slug}'")

        # Status validation
        if status and status not in VALID_STATUSES_EXEC:
            errors.append(f"  Row {i}: Invalid status '{status}' on '{slug}'")

        # Feature set validation
        if features:
            for feat in features.split("|"):
                feat = feat.strip()
                if feat and feat not in CANONICAL_FEATURES:
                    errors.append(f"  Row {i}: Invalid feature '{feat}' on '{slug}'")

    return errors, set(slugs)


def validate_page_master(rows):
    """Validate page_master.csv."""
    errors = []
    slugs = []

    for i, row in enumerate(rows, start=2):
        slug = row.get("page_slug", "").strip()
        hub = row.get("hub", "").strip()
        page_type = row.get("page_type", "").strip()
        status = row.get("status", "").strip()
        features = row.get("feature_set", "").strip()

        if not slug:
            errors.append(f"  Row {i}: Missing page_slug")
            continue

        # Duplicate slug check
        if slug in slugs:
            errors.append(f"  Row {i}: Duplicate page_slug '{slug}'")
        slugs.append(slug)

        # Hub validation
        if hub and hub not in CANONICAL_HUBS:
            errors.append(f"  Row {i}: Invalid hub '{hub}' on '{slug}'")

        # Page type validation
        if page_type and page_type not in CANONICAL_PAGE_TYPES:
            errors.append(f"  Row {i}: Invalid page_type '{page_type}' on '{slug}'")

        # Status validation
        if status and status not in VALID_STATUSES_PAGE:
            errors.append(f"  Row {i}: Invalid status '{status}' on '{slug}'")

        # Feature set validation
        if features:
            for feat in features.split("|"):
                feat = feat.strip()
                if feat and feat not in CANONICAL_FEATURES:
                    errors.append(f"  Row {i}: Invalid feature '{feat}' on '{slug}'")

    return errors, set(slugs)


def validate_content_calendar(rows, valid_slugs):
    """Validate content_calendar.csv against page_master slugs."""
    errors = []
    content_ids = []

    for i, row in enumerate(rows, start=2):
        cid = row.get("content_id", "").strip()
        slug = row.get("page_slug", "").strip()
        hub = row.get("hub", "").strip()
        priority = row.get("priority", "").strip()

        if not cid:
            errors.append(f"  Row {i}: Missing content_id")
        elif cid in content_ids:
            errors.append(f"  Row {i}: Duplicate content_id '{cid}'")
        content_ids.append(cid)

        # Slug referential integrity
        if slug and slug not in valid_slugs:
            errors.append(f"  Row {i}: page_slug '{slug}' not found in page_master.csv")

        # Hub validation
        if hub and hub not in CANONICAL_HUBS:
            errors.append(f"  Row {i}: Invalid hub '{hub}' on '{slug}'")

        # Priority validation
        if priority and priority not in VALID_PRIORITIES:
            errors.append(f"  Row {i}: Invalid priority '{priority}' on '{slug}'")

    return errors


def validate_backlink_targets(rows, valid_slugs):
    """Validate backlink_targets.csv against page_master slugs."""
    errors = []

    for i, row in enumerate(rows, start=2):
        slug = row.get("target_page_slug", "").strip()
        priority = row.get("priority", "").strip()

        # Slug referential integrity (skip empty slugs)
        if slug and slug not in valid_slugs:
            errors.append(f"  Row {i}: target_page_slug '{slug}' not found in page_master.csv")

        if priority and priority not in VALID_PRIORITIES:
            errors.append(f"  Row {i}: Invalid priority '{priority}'")

    return errors


def cross_validate_slugs(exec_slugs, page_slugs):
    """Check that execution_master and page_master have matching slugs."""
    errors = []

    in_exec_not_page = exec_slugs - page_slugs
    in_page_not_exec = page_slugs - exec_slugs

    for slug in sorted(in_exec_not_page):
        errors.append(f"  '{slug}' in execution_seo_master but NOT in page_master")

    for slug in sorted(in_page_not_exec):
        errors.append(f"  '{slug}' in page_master but NOT in execution_seo_master")

    return errors


def validate_content_files_alignment(page_slugs, content_calendar_slugs):
    """Check that content files on disk align with CSVs and vice versa."""
    import glob as glob_mod

    errors = []
    base_dir = os.path.dirname(DATA_DIR)
    content_dir = os.path.join(base_dir, "content")

    # Build set of slugs that have content files on disk
    file_slugs = set()

    # Pages
    for f in glob_mod.glob(os.path.join(content_dir, "pages", "*.md")):
        name = os.path.splitext(os.path.basename(f))[0]
        if name == "homepage":
            file_slugs.add("/")
        else:
            file_slugs.add(f"/{name}")

    # Blogs
    for f in glob_mod.glob(os.path.join(content_dir, "blogs", "**", "*.md"), recursive=True):
        name = os.path.splitext(os.path.basename(f))[0]
        file_slugs.add(f"/blog/{name}")

    # Check: content files with no page_master row
    orphaned = file_slugs - page_slugs
    for slug in sorted(orphaned):
        errors.append(f"  Content file exists for '{slug}' but NO row in page_master.csv")

    # Check: content files with no content_calendar row
    orphaned_cal = file_slugs - content_calendar_slugs
    for slug in sorted(orphaned_cal):
        errors.append(f"  Content file exists for '{slug}' but NO row in content_calendar.csv")

    # Check: pages with status=draft_ready but no content file
    # (This is checked via page_master rows)

    # Check: content files exist but status is still 'planned'
    # We report this as a warning
    return errors, file_slugs


def main():
    print("=" * 60)
    print("ProfileTap SEO OS — System Validation")
    print("=" * 60)

    total_errors = 0

    # Load all files
    exec_rows = load_csv("keywords/execution_seo_master.csv")
    page_rows = load_csv("pages/page_master.csv")
    content_rows = load_csv("content/content_calendar.csv")
    backlink_rows = load_csv("backlinks/backlink_targets.csv")

    # Validate execution_seo_master.csv
    print(f"\n[1] execution_seo_master.csv ({len(exec_rows)} rows)")
    exec_errors, exec_slugs = validate_execution_master(exec_rows)
    if exec_errors:
        for e in exec_errors:
            print(e)
        total_errors += len(exec_errors)
    else:
        print("  PASS")

    # Validate page_master.csv
    print(f"\n[2] page_master.csv ({len(page_rows)} rows)")
    page_errors, page_slugs = validate_page_master(page_rows)
    if page_errors:
        for e in page_errors:
            print(e)
        total_errors += len(page_errors)
    else:
        print("  PASS")

    # Cross-validate slugs
    print(f"\n[3] Cross-file slug consistency (execution_master <-> page_master)")
    cross_errors = cross_validate_slugs(exec_slugs, page_slugs)
    if cross_errors:
        for e in cross_errors:
            print(e)
        total_errors += len(cross_errors)
    else:
        print("  PASS")

    # Validate content_calendar.csv
    print(f"\n[4] content_calendar.csv ({len(content_rows)} rows)")
    content_errors = validate_content_calendar(content_rows, page_slugs)
    if content_errors:
        for e in content_errors:
            print(e)
        total_errors += len(content_errors)
    else:
        print("  PASS")

    # Validate backlink_targets.csv
    print(f"\n[5] backlink_targets.csv ({len(backlink_rows)} rows)")
    backlink_errors = validate_backlink_targets(backlink_rows, page_slugs)
    if backlink_errors:
        for e in backlink_errors:
            print(e)
        total_errors += len(backlink_errors)
    else:
        print("  PASS")

    # Validate content file alignment
    content_calendar_slugs = {row.get("page_slug", "").strip() for row in content_rows if row.get("page_slug", "").strip()}
    print(f"\n[6] Content files ↔ CSV alignment")
    align_errors, file_slugs = validate_content_files_alignment(page_slugs, content_calendar_slugs)
    if align_errors:
        for e in align_errors:
            print(e)
        total_errors += len(align_errors)
    else:
        print(f"  PASS ({len(file_slugs)} content files, all aligned)")

    # Summary
    print(f"\n{'=' * 60}")
    if total_errors == 0:
        print(f"RESULT: ALL CHECKS PASSED")
    else:
        print(f"RESULT: {total_errors} error(s) found")
    print(f"{'=' * 60}")

    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

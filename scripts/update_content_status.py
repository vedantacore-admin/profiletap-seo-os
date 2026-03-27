#!/usr/bin/env python3
"""
One-time script to update content_calendar.csv and page_master.csv statuses
for pages that have content files on disk.
"""

import csv
import os
import glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE, "content")

# Build set of slugs that have content files
existing_slugs = set()

# Pages
for f in glob.glob(os.path.join(CONTENT_DIR, "pages", "*.md")):
    name = os.path.splitext(os.path.basename(f))[0]
    if name == "homepage":
        existing_slugs.add("/")
    else:
        existing_slugs.add(f"/{name}")

# Blogs
for f in glob.glob(os.path.join(CONTENT_DIR, "blogs", "**", "*.md"), recursive=True):
    name = os.path.splitext(os.path.basename(f))[0]
    existing_slugs.add(f"/blog/{name}")

print(f"Found {len(existing_slugs)} content files on disk")
print()

# Update content_calendar.csv
cal_path = os.path.join(BASE, "data", "content", "content_calendar.csv")
with open(cal_path, "r") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updated_cal = 0
for row in rows:
    slug = row["page_slug"]
    if slug in existing_slugs:
        if row["status"] == "planned":
            row["status"] = "draft_ready"
            updated_cal += 1
        if row.get("brief_status") == "brief_pending":
            row["brief_status"] = "draft_ready"

with open(cal_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"content_calendar.csv: updated {updated_cal} rows to draft_ready")

# Update page_master.csv
pm_path = os.path.join(BASE, "data", "pages", "page_master.csv")
with open(pm_path, "r") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updated_pm = 0
for row in rows:
    slug = row["page_slug"]
    if slug in existing_slugs:
        if row["status"] == "planned":
            row["status"] = "draft_ready"
            updated_pm += 1

with open(pm_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"page_master.csv: updated {updated_pm} rows to draft_ready")

# Update execution_seo_master.csv
esm_path = os.path.join(BASE, "data", "keywords", "execution_seo_master.csv")
with open(esm_path, "r") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updated_esm = 0
for row in rows:
    slug = row["page_slug"]
    if slug in existing_slugs:
        if row["status"] == "planned":
            row["status"] = "draft_ready"
            updated_esm += 1

with open(esm_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"execution_seo_master.csv: updated {updated_esm} rows to draft_ready")
print()
print("Done. Run validate_system.py to verify.")

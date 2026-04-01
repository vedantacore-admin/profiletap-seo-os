#!/usr/bin/env python3
"""
add_dev_headers.py
------------------
Injects a developer validation comment block immediately after the closing `---`
of the YAML frontmatter in every content markdown file.

Usage:
    python scripts/add_dev_headers.py --dry-run   # Preview changes, no writes
    python scripts/add_dev_headers.py             # Apply changes to all files

The header tells developers:
  - Which JSON-LD schema types are required for this page
  - The BreadcrumbList path (extracted from existing bottom comments)
  - Validation URLs (Google Rich Results Test, GSC)
  - AI visibility checklist (robots.txt, canonical, FAQPage for AI Overviews)
"""

import os
import re
import sys
import argparse
from pathlib import Path

# Repo root (two levels up from scripts/)
REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"

# Schema types that are REQUIRED vs OPTIONAL by page type
# (maps directory + page signals → required schemas)
PAGE_TYPE_SCHEMAS = {
    "homepage": {
        "required": ["Organization", "WebSite"],
        "optional": [],
    },
    "solution_hub": {
        "required": ["BreadcrumbList"],
        "optional": ["FAQPage"],
    },
    "page": {
        "required": ["WebPage", "BreadcrumbList"],
        "optional": ["FAQPage"],
    },
    "blog": {
        "required": ["BreadcrumbList", "Article"],
        "optional": ["FAQPage", "HowTo"],
    },
    "product": {
        "required": ["BreadcrumbList", "Product"],
        "optional": ["FAQPage"],
    },
    "product_index": {
        "required": ["BreadcrumbList"],
        "optional": [],
    },
}

# Solution hub slugs (no schema field in frontmatter)
SOLUTION_HUB_URLS = {
    "/business-identity",
    "/creator-identity",
    "/family-safety-profile",
    "/pet-id-profile",
    "/travel-profile",
    "/vehicle-profile",
}

SCHEMA_DESCRIPTIONS = {
    "Organization": "name, url, logo, sameAs (homepage only)",
    "WebSite": "name, url, potentialAction (homepage only)",
    "WebPage": "name, description, url",
    "BreadcrumbList": "itemListElement[] with position, name, item",
    "FAQPage": "mainEntity[] — Q&A pairs (see schema comments at bottom of file)",
    "Article": "headline, description, author, publisher, datePublished, dateModified, image",
    "HowTo": "name, description, step[] — only for step-by-step guides",
    "Product": "name, description, brand, image, offers (price in INR)",
}

HEADER_MARKER = "<!-- DEVELOPER VALIDATION"


def parse_frontmatter(content: str) -> dict:
    """Extract key:value pairs from YAML frontmatter block."""
    fm = {}
    lines = content.split("\n")
    if lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r'^(\w+)\s*:\s*(.+)$', line.strip())
        if match:
            key = match.group(1).strip()
            val = match.group(2).strip().strip('"').strip("'")
            fm[key] = val
    return fm


def extract_breadcrumb_path(content: str) -> str:
    """
    Extract breadcrumb path from existing schema hint comments at the bottom.
    Handles several patterns:
      <!-- SCHEMA: BreadcrumbList: Home > Business > Page Name -->
      <!-- SCHEMA: BreadcrumbList -->\\n<!-- Home > Business > Page Name -->
      <!-- BreadcrumbList: Home > Business Identity -->
    Returns the path string or empty string if not found.
    """
    # Pattern 1: combined on one line
    m = re.search(r'<!--\s*SCHEMA:\s*BreadcrumbList:\s*([^->][^>]*(?:>[^>]*)*)\s*-->', content)
    if m:
        return m.group(1).strip()

    # Pattern 2: separate lines
    m = re.search(r'<!--\s*SCHEMA:\s*BreadcrumbList\s*-->\s*\n<!--\s*(Home[^>]*(?:>[^>]*)*)\s*-->', content)
    if m:
        return m.group(1).strip()

    # Pattern 3: BreadcrumbList without SCHEMA: prefix
    m = re.search(r'<!--\s*BreadcrumbList:\s*(Home[^>]*(?:>[^>]*)*)\s*-->', content)
    if m:
        return m.group(1).strip()

    # Pattern 4: standalone breadcrumb path comment after SCHEMA: BreadcrumbList
    m = re.search(r'<!--\s*SCHEMA:\s*BreadcrumbList\s*-->[^\n]*\n<!--\s*(Home[^-]*)\s*-->', content)
    if m:
        return m.group(1).strip()

    return ""


def determine_page_type(file_path: Path, fm: dict) -> str:
    """Determine the page type from file path and frontmatter."""
    rel = file_path.relative_to(CONTENT_DIR)
    parts = rel.parts

    url = fm.get("url", "")

    if url == "/":
        return "homepage"

    if parts[0] == "blogs":
        return "blog"

    if parts[0] == "products":
        if url in ("/products", "/products/"):
            return "product_index"
        fname = file_path.stem
        if fname == "products-index":
            return "product_index"
        return "product"

    if parts[0] == "pages":
        if url in SOLUTION_HUB_URLS:
            return "solution_hub"
        return "page"

    return "page"


def build_schema_list(page_type: str, fm_schema: str, page_type_key: str) -> list[tuple[str, bool]]:
    """
    Build list of (schema_name, is_required) tuples.
    Merges page-type defaults with frontmatter `schema` field declarations.
    """
    defaults = PAGE_TYPE_SCHEMAS.get(page_type_key, PAGE_TYPE_SCHEMAS["page"])
    required = set(defaults["required"])
    optional = set(defaults["optional"])

    # Parse declared schemas from frontmatter
    declared = set()
    if fm_schema:
        for s in re.split(r'[,\s]+', fm_schema):
            s = s.strip().strip('"')
            if s:
                declared.add(s)

    # Union all known schemas
    all_schemas = required | optional | declared

    result = []
    for s in ["Organization", "WebSite", "WebPage", "BreadcrumbList", "Article", "FAQPage", "HowTo", "Product"]:
        if s in all_schemas:
            is_req = s in required or (s in declared and s not in optional)
            result.append((s, is_req))

    return result


def build_header(fm: dict, breadcrumb: str, page_type_key: str) -> str:
    """Build the developer validation comment block."""
    url = fm.get("url", "(unknown url)")
    fm_schema = fm.get("schema", "")
    schemas = build_schema_list(page_type_key, fm_schema, page_type_key)

    # Schema lines
    schema_lines = []
    for name, required in schemas:
        desc = SCHEMA_DESCRIPTIONS.get(name, "")
        marker = "☐" if required else "☐ (optional)"
        line = f"  {marker} {name:<16} — {desc}"
        schema_lines.append(line)

    schemas_block = "\n".join(schema_lines)

    # Breadcrumb line
    if breadcrumb:
        bc_line = f"  ☐ BreadcrumbList path: {breadcrumb}"
    else:
        bc_line = "  ☐ BreadcrumbList path: (derive from page hierarchy)"

    # Canonical URL
    canonical_url = f"https://profiletap.com{url}" if url.startswith("/") else url

    header = f"""
<!--
╔══════════════════════════════════════════════════════════════════════════╗
║        DEVELOPER VALIDATION — COMPLETE BEFORE PUBLISHING               ║
╚══════════════════════════════════════════════════════════════════════════╝

PAGE : {url}

SCHEMAS REQUIRED (add as <script type="application/ld+json"> in <head>):
{schemas_block}

BREADCRUMB:
{bc_line}

VALIDATE RICH RESULTS : https://search.google.com/test/rich-results
CHECK IN GSC          : Search Console → Enhancements → after indexing

AI VISIBILITY CHECKLIST:
  ☐ robots.txt: GPTBot, PerplexityBot, Anthropic-AI, Google-Extended NOT blocked
  ☐ FAQPage schema active → surfaces in Google AI Overviews
  ☐ Canonical tag: <link rel="canonical" href="{canonical_url}">
  ☐ Content is factual, entity-rich, and citable by AI models
  ☐ Answer text in FAQPage schema is ≤ 300 chars (AI extraction friendly)

Full JSON-LD templates → sop/schema-markup-implementation.md
AI visibility guidance → sop/schema-markup-implementation.md § 7
-->
"""
    return header.lstrip("\n")


def process_file(file_path: Path, dry_run: bool = False) -> bool:
    """
    Inject developer validation header into a single content file.
    Returns True if file was (or would be) modified.
    """
    content = file_path.read_text(encoding="utf-8")

    # Skip if header already present
    if HEADER_MARKER in content:
        return False

    # Must start with frontmatter
    if not content.startswith("---"):
        print(f"  SKIP (no frontmatter): {file_path.relative_to(REPO_ROOT)}")
        return False

    # Find the closing --- of frontmatter
    lines = content.split("\n")
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        print(f"  SKIP (no closing ---): {file_path.relative_to(REPO_ROOT)}")
        return False

    fm = parse_frontmatter(content)
    breadcrumb = extract_breadcrumb_path(content)
    page_type_key = determine_page_type(file_path, fm)
    header = build_header(fm, breadcrumb, page_type_key)

    # Rebuild: everything up to and including the closing ---
    before = "\n".join(lines[: end_idx + 1])
    after = "\n".join(lines[end_idx + 1 :])

    new_content = before + "\n" + header + after

    rel = file_path.relative_to(REPO_ROOT)
    if dry_run:
        print(f"\n{'='*70}")
        print(f"FILE: {rel}")
        print(f"PAGE TYPE: {page_type_key}")
        print(f"BREADCRUMB: {breadcrumb or '(not found)'}")
        print("HEADER PREVIEW:")
        print(header[:600] + ("..." if len(header) > 600 else ""))
    else:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"  ✓ {rel}")

    return True


def main():
    parser = argparse.ArgumentParser(description="Inject developer validation headers into content files.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    args = parser.parse_args()

    md_files = sorted(CONTENT_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files in {CONTENT_DIR.relative_to(REPO_ROOT)}")

    modified = 0
    skipped = 0

    for f in md_files:
        result = process_file(f, dry_run=args.dry_run)
        if result:
            modified += 1
        else:
            skipped += 1

    mode = "Would modify" if args.dry_run else "Modified"
    print(f"\n{mode}: {modified} files | Already done / skipped: {skipped} files")


if __name__ == "__main__":
    main()

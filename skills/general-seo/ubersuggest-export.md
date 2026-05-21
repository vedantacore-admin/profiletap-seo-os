# Ubersuggest Export

> Claude Code Skill: Extract tracked keywords from any SEO OS project into Ubersuggest-ready import files.
> Use this when setting up or refreshing a Ubersuggest rank tracker for a project managed under this SEO OS.

---

## 1. What This Skill Does

Reads the project's keyword CSVs and emits three files into `data/keywords/exports/`:

1. **`ubersuggest_import.csv`** — per-keyword record with metadata (hub, priority, page_slug, intent, market, role, plus volume/kd/cpc when known). Used for the project's own bookkeeping and future re-imports.
2. **`ubersuggest_keywords.txt`** — line-separated keyword list, sectioned by priority and hub, paste-ready into Ubersuggest's "Add Keywords" textarea.
3. **`ubersuggest_export_report.md`** — run summary with totals, priority/hub breakdown, list of keywords missing Ubersuggest metrics, and any cross-page duplicate keywords flagged for review.

## 2. Inputs

- **Required:** `data/keywords/execution_seo_master.csv` (canonical page → primary/secondary keyword mapping)
- **Optional:** `data/keywords/raw_keyword_bank.csv` (joined on lowercased `keyword` to attach `ubersuggest_volume`, `ubersuggest_kd`, `ubersuggest_cpc`, `ubersuggest_last_checked`)

Both files are expected in comma-separated format with `|` as the in-field delimiter for `secondary_keywords`.

## 3. How to Run

1. Determine the project root (the `projects/<name>/` directory). When the user invokes `/ubersuggest-export` without an argument, use the current working directory.
2. If the user mentions a Ubersuggest plan tier with a tracking quota smaller than the project's full keyword count, pass that quota as `--limit N`. Default quotas: Individual=150, Business=300, Enterprise=900.
3. Save the Python script from section 6 below to `/tmp/ubersuggest_export.py`.
4. Run: `python3 /tmp/ubersuggest_export.py <project_root> [--limit N]`.
5. Print the script's summary to the user.
6. Confirm the files exist in `<project_root>/data/keywords/exports/` and surface their paths. When `--limit N` is set, the script writes three additional files: `ubersuggest_keywords_top<N>.txt`, `ubersuggest_import_top<N>.csv`, `ubersuggest_capped_top<N>_report.md`.
7. If the report flags cross-page duplicates or a non-trivial number of keywords missing volume data, mention this in the user-facing summary — these are the next things to fix.

## 4. Output Schemas

**`ubersuggest_import.csv` columns:**

| Column | Meaning |
|---|---|
| `keyword` | The keyword as written in source |
| `page_slug` | Target page from `execution_seo_master.csv` |
| `hub` | One of platform, business, creator, family_safety, pet, travel, vehicle |
| `priority` | P1 / P2 / P3 |
| `search_intent` | commercial / informational / transactional / navigational |
| `market` | e.g. `IN+GLOBAL`, `IN` |
| `keyword_role` | `primary` or `secondary` |
| `volume`, `kd`, `cpc`, `last_checked` | From `raw_keyword_bank.csv` join; blank if unknown |
| `tag_string` | Semicolon-separated tags formatted for Ubersuggest's bulk-tag UI: `hub:<hub>;priority:<P>;intent:<intent>;role:<role>` |

**`ubersuggest_keywords.txt` format:**

```
# === P1 / business ===
digital business card india
nfc business card india
...

# === P1 / platform ===
smart identity platform
...
```

Records are sorted by priority (P1 first), then hub alphabetically, then role (primaries before secondaries), then keyword alphabetically. Section dividers let the operator paste each priority/hub block into Ubersuggest's Rank Tracker and apply the matching tags in batches. The role-aware sort ensures that when `--limit N` truncates the list, each page's primary keyword is kept before any secondary from a lower priority is added.

### Capped output (when `--limit N` is set)

In addition to the three full files, the script writes:

- `ubersuggest_keywords_top<N>.txt` — same format as the full .txt, capped to N keywords
- `ubersuggest_import_top<N>.csv` — same schema as the full .csv, capped to N rows
- `ubersuggest_capped_top<N>_report.md` — kept/dropped breakdown by priority x hub, plus the full list of dropped keywords (so they can be moved into Google Search Console tracking instead)

**Selection rule** (top-N): all P1 keywords are kept before any P2 keyword is considered; within each (priority, hub) block, every page's primary keyword is kept before any secondary from that block. This is the right call for a constrained-quota plan — full coverage of the critical tier beats partial coverage across all tiers.

## 5. After Running

Hand off to the project's Ubersuggest setup runbook (e.g. `projects/profiletap/docs/06-ubersuggest-setup.md` for ProfileTap) — that's where the operator picks up to paste the `.txt` blocks into Ubersuggest and tag them.

If the user is running the export to *refresh* an existing Ubersuggest project (not first setup), the workflow is:

1. Compare git diff of the export files against last commit → identify added/removed keywords.
2. In Ubersuggest Rank Tracker: add the new keywords, archive the removed ones.
3. Commit the new export files so the diff stays a useful audit signal.

## 6. The Script

Save the following to `/tmp/ubersuggest_export.py` before running:

```python
#!/usr/bin/env python3
"""Extract keywords from SEO OS project CSVs into Ubersuggest-ready import files.

Usage:
    python3 ubersuggest_export.py <project_root> [--limit N]

When --limit N is supplied, additionally writes a capped subset (top-N keywords by
priority then hub then role) for plan tiers with a tracking quota smaller than the
full keyword set.
"""
import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2}
ROLE_ORDER = {"primary": 0, "secondary": 1}


def write_csv(path, records, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in records:
            w.writerow(r)


def write_txt(path, records):
    with path.open("w", encoding="utf-8") as f:
        current_section = None
        for r in records:
            section = (r["priority"], r["hub"])
            if section != current_section:
                if current_section is not None:
                    f.write("\n")
                f.write(f"# === {r['priority']} / {r['hub']} ===\n")
                current_section = section
            f.write(f"{r['keyword']}\n")


def main(project_root, limit=None):
    project_root = Path(project_root).resolve()
    src_dir = project_root / "data" / "keywords"
    out_dir = src_dir / "exports"
    out_dir.mkdir(parents=True, exist_ok=True)

    exec_path = src_dir / "execution_seo_master.csv"
    bank_path = src_dir / "raw_keyword_bank.csv"

    if not exec_path.exists():
        sys.exit(f"ERROR: {exec_path} not found")

    metrics = {}
    if bank_path.exists():
        with bank_path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f, restval=""):
                kw = row.get("keyword", "").strip().lower()
                if not kw:
                    continue
                metrics[kw] = {
                    "volume": row.get("ubersuggest_volume", "").strip(),
                    "kd": row.get("ubersuggest_kd", "").strip(),
                    "cpc": row.get("ubersuggest_cpc", "").strip(),
                    "last_checked": row.get("ubersuggest_last_checked", "").strip(),
                }

    records = []
    seen = set()
    cross_page = defaultdict(set)
    with exec_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, restval=""):
            page_slug = row.get("page_slug", "").strip()
            hub = row.get("hub", "").strip()
            priority = row.get("priority", "").strip()
            search_intent = row.get("search_intent", "").strip()
            market = row.get("market", "").strip()
            primary = row.get("primary_keyword", "").strip()
            secondaries_raw = row.get("secondary_keywords", "").strip()

            candidates = [(primary, "primary")]
            for s in secondaries_raw.split("|"):
                s = s.strip()
                if s:
                    candidates.append((s, "secondary"))

            for kw, role in candidates:
                if not kw:
                    continue
                key = (kw.lower(), page_slug)
                if key in seen:
                    continue
                seen.add(key)
                cross_page[kw.lower()].add(page_slug)

                m = metrics.get(kw.lower(), {})
                tag_string = f"hub:{hub};priority:{priority};intent:{search_intent};role:{role}"
                records.append({
                    "keyword": kw,
                    "page_slug": page_slug,
                    "hub": hub,
                    "priority": priority,
                    "search_intent": search_intent,
                    "market": market,
                    "keyword_role": role,
                    "volume": m.get("volume", ""),
                    "kd": m.get("kd", ""),
                    "cpc": m.get("cpc", ""),
                    "last_checked": m.get("last_checked", ""),
                    "tag_string": tag_string,
                })

    records.sort(key=lambda r: (
        PRIORITY_ORDER.get(r["priority"], 99),
        r["hub"],
        ROLE_ORDER.get(r["keyword_role"], 9),
        r["keyword"].lower(),
    ))

    fieldnames = ["keyword", "page_slug", "hub", "priority", "search_intent",
                  "market", "keyword_role", "volume", "kd", "cpc",
                  "last_checked", "tag_string"]

    csv_path = out_dir / "ubersuggest_import.csv"
    txt_path = out_dir / "ubersuggest_keywords.txt"
    report_path = out_dir / "ubersuggest_export_report.md"
    write_csv(csv_path, records, fieldnames)
    write_txt(txt_path, records)

    by_priority = defaultdict(int)
    by_hub = defaultdict(int)
    by_priority_hub = defaultdict(int)
    missing_metrics = []
    duplicates = []
    for r in records:
        by_priority[r["priority"]] += 1
        by_hub[r["hub"]] += 1
        by_priority_hub[(r["priority"], r["hub"])] += 1
        if not r["volume"]:
            missing_metrics.append(r["keyword"])
    for kw_lower, slugs in cross_page.items():
        if len(slugs) > 1:
            duplicates.append((kw_lower, sorted(slugs)))

    with report_path.open("w", encoding="utf-8") as f:
        f.write("# Ubersuggest Export Report\n\n")
        f.write(f"**Generated:** {date.today().isoformat()}\n")
        f.write(f"**Project root:** `{project_root}`\n")
        f.write(f"**Total keywords:** {len(records)}\n\n")
        f.write("## By Priority\n\n")
        for p in sorted(by_priority, key=lambda x: PRIORITY_ORDER.get(x, 99)):
            f.write(f"- **{p}:** {by_priority[p]}\n")
        f.write("\n## By Hub\n\n")
        for h in sorted(by_hub):
            f.write(f"- **{h}:** {by_hub[h]}\n")
        f.write("\n## By Priority x Hub\n\n")
        f.write("| Priority | Hub | Count |\n|---|---|---|\n")
        for (p, h), c in sorted(
            by_priority_hub.items(),
            key=lambda x: (PRIORITY_ORDER.get(x[0][0], 99), x[0][1]),
        ):
            f.write(f"| {p} | {h} | {c} |\n")
        unique_missing = sorted(set(missing_metrics))
        f.write(f"\n## Keywords missing Ubersuggest metrics ({len(unique_missing)})\n\n")
        f.write("These keywords have no `ubersuggest_volume` value in `raw_keyword_bank.csv`. Backfill after the first Ubersuggest pull.\n\n")
        if unique_missing:
            for kw in unique_missing:
                f.write(f"- {kw}\n")
        else:
            f.write("_None - all keywords have volume data._\n")
        f.write(f"\n## Cross-page duplicate keywords ({len(duplicates)})\n\n")
        f.write("Keywords appearing on multiple pages. Per the one-keyword-one-page rule, these should be reviewed.\n\n")
        if duplicates:
            for kw_lower, slugs in sorted(duplicates):
                f.write(f"- `{kw_lower}` on: {', '.join(slugs)}\n")
        else:
            f.write("_None._\n")

    print("Ubersuggest export complete.")
    print(f"  Total keywords: {len(records)}")
    for p in sorted(by_priority, key=lambda x: PRIORITY_ORDER.get(x, 99)):
        print(f"    {p}: {by_priority[p]}")
    print(f"  Hubs: {len(by_hub)}")
    print(f"  Missing metrics: {len(set(missing_metrics))}")
    print(f"  Cross-page duplicates: {len(duplicates)}")
    print("  Full files:")
    print(f"    {csv_path.relative_to(project_root)}")
    print(f"    {txt_path.relative_to(project_root)}")
    print(f"    {report_path.relative_to(project_root)}")

    if limit is not None and limit < len(records):
        kept = records[:limit]
        dropped = records[limit:]
        kept_csv = out_dir / f"ubersuggest_import_top{limit}.csv"
        kept_txt = out_dir / f"ubersuggest_keywords_top{limit}.txt"
        capped_report = out_dir / f"ubersuggest_capped_top{limit}_report.md"

        write_csv(kept_csv, kept, fieldnames)
        write_txt(kept_txt, kept)

        kept_by_ph = defaultdict(int)
        kept_by_role = defaultdict(int)
        for r in kept:
            kept_by_ph[(r["priority"], r["hub"])] += 1
            kept_by_role[r["keyword_role"]] += 1
        dropped_by_ph = defaultdict(int)
        for r in dropped:
            dropped_by_ph[(r["priority"], r["hub"])] += 1

        with capped_report.open("w", encoding="utf-8") as f:
            f.write(f"# Ubersuggest Capped Export - Top {limit}\n\n")
            f.write(f"**Generated:** {date.today().isoformat()}\n")
            f.write(f"**Cap:** {limit} keywords (matches Ubersuggest Individual plan quota)\n")
            f.write(f"**Kept:** {len(kept)} / **Dropped:** {len(dropped)}\n\n")
            f.write("## Selection rule\n\n")
            f.write("Sort by (priority P1 < P2 < P3) -> (hub alphabetical) -> (role primary before secondary) -> (keyword alphabetical), then take first N. This guarantees:\n\n")
            f.write("- All P1 keywords are tracked before any P2/P3 keyword is considered.\n")
            f.write("- Within each (priority, hub) block, every page's primary keyword is included before any secondary keyword from that block.\n\n")
            f.write("## Kept - by Priority x Hub\n\n")
            f.write("| Priority | Hub | Count |\n|---|---|---|\n")
            for (p, h), c in sorted(
                kept_by_ph.items(),
                key=lambda x: (PRIORITY_ORDER.get(x[0][0], 99), x[0][1]),
            ):
                f.write(f"| {p} | {h} | {c} |\n")
            f.write("\n## Kept - by Role\n\n")
            for role, c in sorted(kept_by_role.items(), key=lambda x: ROLE_ORDER.get(x[0], 9)):
                f.write(f"- **{role}:** {c}\n")
            f.write(f"\n## Dropped - by Priority x Hub ({len(dropped)})\n\n")
            f.write("| Priority | Hub | Count |\n|---|---|---|\n")
            for (p, h), c in sorted(
                dropped_by_ph.items(),
                key=lambda x: (PRIORITY_ORDER.get(x[0][0], 99), x[0][1]),
            ):
                f.write(f"| {p} | {h} | {c} |\n")
            f.write("\n## Dropped keywords (full list)\n\n")
            f.write("Track these in Google Search Console once the property is verified. They stay in `ubersuggest_import.csv` for future re-pasting if you upgrade plans.\n\n")
            for r in dropped:
                f.write(f"- `[{r['priority']} / {r['hub']} / {r['keyword_role']}]` {r['keyword']} -> {r['page_slug']}\n")

        print()
        print(f"Capped subset (top {limit}):")
        print(f"  Kept: {len(kept)}  Dropped: {len(dropped)}")
        for (p, h), c in sorted(
            kept_by_ph.items(),
            key=lambda x: (PRIORITY_ORDER.get(x[0][0], 99), x[0][1]),
        ):
            print(f"    {p}/{h}: {c}")
        print("  Capped files:")
        print(f"    {kept_csv.relative_to(project_root)}")
        print(f"    {kept_txt.relative_to(project_root)}")
        print(f"    {capped_report.relative_to(project_root)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1 or len(args) > 3:
        sys.exit("Usage: python3 ubersuggest_export.py <project_root> [--limit N]")
    project_root = args[0]
    limit = None
    if len(args) >= 2:
        if args[1] != "--limit":
            sys.exit("Usage: python3 ubersuggest_export.py <project_root> [--limit N]")
        try:
            limit = int(args[2])
        except (IndexError, ValueError):
            sys.exit("--limit requires an integer argument")
    main(project_root, limit=limit)
```

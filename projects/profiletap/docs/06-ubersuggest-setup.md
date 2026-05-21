# Ubersuggest Setup Runbook — ProfileTap

## Purpose

One-time setup of the ProfileTap Ubersuggest workspace on the Business plan. This is the operational layer for the rank-tracking, site-audit, competitor-tracking, and backlink-monitoring duties listed in `05-measurement-plan.md`.

**Audience:** Rutuja. Every step is copy-paste-ready with exact button names. Steps that need a decision are tagged `**Owner: Pratima (decision)**`; steps that need founder signoff are tagged `**Owner: Hariom (signoff)**`; everything else is `**Owner: Rutuja**`.

**Plan tier:** Individual ($29/mo or lifetime equivalent). Quotas this runbook assumes:

| Feature | Individual quota | Implication for ProfileTap |
|---|---|---|
| Projects | 1 | Single project = `profiletap.com` only |
| Tracked keywords | 150 / day | 239 of the 389 keywords cannot be tracked on Ubersuggest — see section 4 for which 150 are kept and where the rest go |
| Competitors per project | 1 | Only one of the four confirmed competitors makes it in — see section 6 for the Pratima decision |
| Site audit pages crawled | 150 / week | Whole site fits since ProfileTap has < 150 published pages |
| Domain reports per day | 25 | Use sparingly for ad-hoc competitor lookups |

**Plan upgrade trigger:** if `wc -l data/keywords/exports/ubersuggest_import.csv` grows past ~600 or you need to track more than one competitor seriously, revisit upgrading to Business ($49) or Enterprise ($99).

---

## 1. Account Setup — **Owner: Hariom (signoff)**, executed by Rutuja

1. Go to `https://neilpatel.com/ubersuggest`.
2. Click **Sign Up** → use `admin@vedantacore.com` as the login email.
3. **Owner: Hariom (signoff)** — purchase the **Individual** plan (monthly $29 or lifetime). Choose lifetime if budget allows; payback at $29/mo is ~10 months.
4. Verify the email. Save the password to 1Password under entry **"Ubersuggest — ProfileTap"**.
5. Log in. Confirm the dashboard top-right shows **Individual** tier.

---

## 2. Create the ProfileTap Project — **Owner: Rutuja**

1. Dashboard → **Projects** → **Add Project**. Individual plan allows only one project — make sure no scratch project already occupies the slot.
2. Fill the form exactly:
   - **Domain:** `profiletap.com`
   - **Project name:** `ProfileTap`
   - **Tracked location:** `India` (only — Individual plan supports one location per project)
   - **Language:** `English`
   - **Search engine:** `Google`
   - **Device:** `Mobile` only (locked-in decision — India-first audience is mobile-first; this preserves the full 150 keyword quota since Ubersuggest counts each device as one tracked keyword)
   - **Frequency:** `Daily`
   - **Email reports:** ON, daily digest to `admin@vedantacore.com` + `rutuja@vedantacore.com`
3. Click **Save**.
4. Confirm the project card appears on the Projects page with a green status indicator.

---

## 3. Connect Google Search Console — **Owner: Rutuja**

1. Open the ProfileTap project → **Settings** → **Integrations** → **Google Search Console**.
2. Click **Connect** → sign in with the Google account that owns the GSC property for `profiletap.com`. If you don't have GSC access, ping Hariom — only the founder can grant property access.
3. Grant the requested scopes (read-only on Search Console).
4. Once connected, Ubersuggest auto-suggests keywords from real GSC data. **Do not import these yet** — the canonical keyword list comes from step 4 below.

---

## 4. Import the Tracked Keywords — **Owner: Rutuja**

The canonical keyword list lives in the SEO OS repo. Never re-type keywords by hand — always regenerate from source.

1. In a Claude Code session opened from `projects/profiletap/`, run:
   ```
   /ubersuggest-export --limit 150
   ```
   (The `--limit 150` flag caps the export to the Individual plan's keyword quota.)
2. The skill writes six files to `projects/profiletap/data/keywords/exports/`:
   - **Use these for Ubersuggest paste:**
     - `ubersuggest_keywords_top150.txt` — paste source (capped to 150 keywords, sectioned by `# === P{1|2} / <hub> ===` blocks)
     - `ubersuggest_import_top150.csv` — record of what's tracked in Ubersuggest
     - `ubersuggest_capped_top150_report.md` — kept/dropped breakdown
   - **Reference only (full list — track via GSC):**
     - `ubersuggest_keywords.txt` — all 389 keywords
     - `ubersuggest_import.csv` — full record
     - `ubersuggest_export_report.md` — full summary
3. Open `ubersuggest_keywords_top150.txt`.
4. In Ubersuggest: ProfileTap project → **Rank Tracker** → **Add Keywords**.
5. **For each block** in the .txt file (block header looks like `# === P1 / business ===`):
   - Copy every line under the header (skip the `# ===` line itself) until the next header or end of file.
   - Paste into the Add Keywords textarea.
   - Set **Location:** `India`, **Device:** `Mobile` (matches the project's device setting from section 2).
   - Click **Add**.
   - After Ubersuggest finishes adding the rows, **select all newly-added rows** (checkbox at top of the just-added block) → click **Add Tag** → add two tags matching the header: `hub:<hub>` and `priority:<P1|P2>`. Example: for the `# === P1 / business ===` block, add tags `hub:business` and `priority:P1`.
   - Save.
6. Repeat for every block in the .txt file (expected blocks at 150-cap: P1/business=100, P1/platform=22, P1/travel=4, P2/business=24 → 4 blocks total).
7. Once done, the Rank Tracker should show exactly 150 keywords (or 75 if you picked Desktop + Mobile). Sanity-check the count against `ubersuggest_capped_top150_report.md`.

**Track the 239 dropped keywords in Google Search Console.** Once GSC is connected (section 3), use GSC's Performance → Queries report to filter by the dropped keyword list from the capped report. GSC tracking is free and unlimited but updates with a 1-2 day delay. Build a Friday habit of skimming GSC for the dropped P2/P3 keywords to catch ranking changes Ubersuggest doesn't see.

---

## 5. Configure Site Audit — **Owner: Rutuja**

1. ProfileTap project → **Site Audit** tab → **Settings**.
2. Configure:
   - **Crawl schedule:** Weekly, every **Sunday 02:00 IST**
   - **Crawl depth:** 5
   - **Pages to crawl:** 150 (max for Individual — covers the whole site since ProfileTap has < 150 published pages)
   - **Follow robots.txt:** ON
   - **Mobile-first crawl:** ON
   - **JavaScript rendering:** ON
   - **Crawl delay:** 1 second (gentle on production)
3. **Alerts → Email me on:** check **Critical issues only** (broken pages, indexability failures, blocked critical resources). Skip warnings — they create noise.
4. Click **Save** → click **Run Audit Now** for the baseline crawl.
5. When the first audit completes (15-30 min), screenshot the **Site Health Score** and paste it into the next `data/tracking/weekly_progress.csv` entry as the baseline number.

---

## 6. Competitor Tracking — Track All 4 (split across Ubersuggest slot + free domain reports)

Individual plan allows **one auto-tracked competitor** in the project's Competitive Analysis tab. The other three competitors get pulled manually each week via the free **Site Explorer** tool (25 domain reports/day quota — plenty for a weekly cadence). All four confirmed competitors from the briefs are tracked.

### 6a. The auto-tracked competitor (1 slot)

**Domain:** `tapmo.in` — chosen because it has the closest market overlap (India-native NFC card, same pricing tier, ranks on most ProfileTap P1 keywords).

**Owner: Rutuja:**
1. ProfileTap project → **Competitive Analysis** → **Add Competitor**.
2. Enter `tapmo.in`.
3. Click **Run Comparison** to populate the keyword-overlap, content-gap, and backlink-gap reports.
4. Bookmark these reports for Thursday's competitor-check block.

### 6b. The three manually-pulled competitors

| Competitor | Type | Why we track it |
|---|---|---|
| `taponn.digital` | India-native NFC card | Second India-native peer; similar product positioning |
| `popl.co` | Global SaaS (US-centric) | Drives the comparison-page strategy (`/popl-alternative-india`); strong organic on global terms |
| `hihello.com` | Global SaaS (US-centric) | Largest global player; benchmark for SEO best-practice |

**Weekly manual pull** — add to the Thursday Block 1 task in every weekly brief:

> **Manual competitor pull (Ubersuggest free reports)** — for each of `taponn.digital`, `popl.co`, `hihello.com`:
> 1. Ubersuggest → **Site Explorer** → enter the domain → **Search**.
> 2. **Top Keywords** report → set **Location:** India → click **Export CSV**.
> 3. Save the CSV to `data/tracking/competitor_pulls/YYYY-MM-DD-<domain>.csv` (e.g. `2026-05-22-popl.co.csv`).
> 4. Skim the top 20 keywords: flag any ProfileTap P1 keyword that the competitor newly ranks for (or where ProfileTap drops below position 10) in the weekly brief's "competitor watch" cell.
> 5. Commit the CSV with message: `chore: competitor pull YYYY-MM-DD - <domain>`.

Quota math: 3 pulls/week = 12/month. Individual plan allows 25/day = 750/month. Headroom is large; spare quota goes to ad-hoc lookups when a new competitor surfaces.

### 6c. Upgrading the auto-tracked competitor (future)

If ProfileTap later wants to swap the auto-tracked competitor (e.g. once `tapmo.in`'s organic data plateaus and `popl.co` matters more), the swap is one click in Competitive Analysis → Settings → Remove → Add new. Historical comparison data on the removed competitor is preserved.

---

## 7. Backlink Monitoring — **Owner: Rutuja**

1. ProfileTap project → **Backlinks** tab → **Monitor Domain** → confirm `profiletap.com` is set as the monitored root.
2. Enable **Weekly digest email** to `admin@vedantacore.com` + `rutuja@vedantacore.com`.
3. **Source-of-truth rule (do not violate):**
   - **Ubersuggest is for discovery only** — it tells you which new domains have linked to ProfileTap that you didn't reach out to.
   - **`data/backlinks/outreach_tracker.csv` is the source of truth for outreach execution status.** Every backlink we got via outreach was tracked there first; Ubersuggest just confirms it went live.
   - When the weekly digest shows a new backlink:
     1. Check if its domain is already in `outreach_tracker.csv`. If yes → update `status` to `live`, fill in `live_url` and `last_contact_date`.
     2. If no → it's an organic backlink. Add a row in `data/backlinks/backlink_targets.csv` with `link_angle=organic_discovery` for tracking, but do NOT add it to `outreach_tracker.csv` (we didn't reach out for it).

---

## 8. Dashboard Saved Views — **Owner: Rutuja**

Create three saved views in the Rank Tracker. These tie directly to cells in the weekly brief.

| View name | Filter | Used for |
|---|---|---|
| `P1 critical` | tag = `priority:P1` | Weekly brief Monday Block 1 — "P1 rank movements" cell |
| `Hub: business` | tag = `hub:business` | Weekly brief Wednesday Block 2 — "hub performance" cell |
| `New backlinks this week` | (Backlinks tab) — date range = last 7 days | Weekly brief Thursday Block 1 |

Save each view from the Rank Tracker via the **Save Filter** button on the filter bar.

---

## 9. Weekly Sync into `rank_tracker.csv` — **Owner: Rutuja**

Until `/ubersuggest-sync` ships, this is manual.

**Every Friday (after the Thursday rank refresh):**

1. Ubersuggest → Rank Tracker → **Export** → **CSV (current week)**.
2. Save the file to `projects/profiletap/data/tracking/imports/ubersuggest_YYYY-MM-DD.csv` (use today's date in IST).
3. Open the imported CSV. For each keyword row, append a row to `projects/profiletap/data/tracking/rank_tracker.csv` with columns: `keyword, page_slug, hub, priority, position, previous_position, change, serp_features, date, notes`. The `page_slug`, `hub`, `priority` come from the matching row in `ubersuggest_import.csv`; the rest come from the Ubersuggest export.
4. Commit both files (`imports/ubersuggest_YYYY-MM-DD.csv` and the appended `rank_tracker.csv`) with message: `chore: ubersuggest rank sync YYYY-MM-DD`.

**Flagged for automation** — `/ubersuggest-sync` skill is the next planned addition. When it lands, this section gets replaced by `Run /ubersuggest-sync.`

---

## 10. Refreshing the Keyword Set (when the bank changes)

When `execution_seo_master.csv` or `raw_keyword_bank.csv` is updated (new pages, new keyword families, deprecated pages):

1. Rerun `/ubersuggest-export` from the project root.
2. `git diff data/keywords/exports/ubersuggest_keywords.txt` shows added/removed keywords.
3. In Ubersuggest Rank Tracker:
   - **Added keywords:** paste each new block following the same tag convention from section 4.
   - **Removed keywords:** select the rows → **Archive** (don't delete — Ubersuggest keeps historical position data on archived keywords).
4. Commit the new export files with message: `chore: ubersuggest export refresh YYYY-MM-DD`.

---

## 11. Failure Modes

| Symptom | Likely cause | Fix |
|---|---|---|
| `/ubersuggest-export` errors `execution_seo_master.csv not found` | Claude session wasn't opened from `projects/profiletap/` | Reopen Claude Code from inside `projects/profiletap/` directory and rerun |
| Ubersuggest paste rejects keywords with `error: duplicate` | Block already added in a prior session | Skip that block; verify the keyword count after all blocks are pasted |
| Site Audit "0 pages crawled" after run | profiletap.com blocks the Ubersuggest bot in robots.txt | Confirm `User-agent: Ubersuggest` is not disallowed in `https://profiletap.com/robots.txt`; if it is, **Owner: Hariom (signoff)** to update robots.txt |
| Competitor report shows 0 overlap | Wrong location set on the competitor (defaulted to US) | Edit the competitor → set location to `India` → rerun comparison |
| Weekly digest email not arriving | Email reports never toggled ON | Project Settings → Notifications → ensure both `admin@` and `rutuja@` are on the list |

---

## Cross-references

- `05-measurement-plan.md` — defines the KPIs Ubersuggest is feeding (this runbook is the *how*; that doc is the *why* and *what*)
- `06-competitor-serp-analysis.md` — the SERP analysis methodology to apply to each tracked competitor
- `skills/general-seo/ubersuggest-export.md` — the skill behind `/ubersuggest-export`
- `data/tracking/rank_tracker.csv` — the destination of the Friday sync

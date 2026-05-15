# ProfileTap SEO OS

Structured SEO operating system for ProfileTap, a smart identity management platform for digital profiles, NFC cards, QR sharing, reputation support, and multi-use identity pages.

This project follows the central SEO OS pipeline:

`keyword → page → content → backlink`

## Quick Start

Open Claude Code from **this directory** (`projects/profiletap/`) — both the root CLAUDE.md (generic skills) and this project's CLAUDE.md (ProfileTap rules, schemas, workflows) will auto-load.

## Team Roles

| Role | Person | Scope | Weekly time |
|---|---|---|---|
| SEO Manager (junior) | **Rutuja** | Owns 95% of execution — outreach, posting, directory listings, content drafting, tracker updates. | 51h (Mon-Sat) |
| Co-Founder, Content + SEO | **Pratima Hariom Shah** | Decisions only — weekly theme, outreach approval, content review, retro verdict. | ≤4h |
| Founder (technical) | **Hariom Shah** | Founder-only — LinkedIn founder article, schema sign-off, retro sign-off. | ≤60 min |

Every task in the generated weekly brief carries an explicit `**Owner:**` tag.

## Running the Weekly Routine (ad-hoc)

The weekly SEO routine generates a single team brief covering Mon-Sat for all three roles + appends a planned row to `data/tracking/weekly_progress.csv`. **Run it every Sunday evening or Monday morning** before the team starts the week. You can also run it ad-hoc at any time to regenerate or preview a week.

### 1. One-time setup

- Open Claude Code from this directory: `cd projects/profiletap/ && claude` (or use the IDE extension pointed at this folder).
- The slash command auto-registers from `.claude/commands/profiletap-weekly-routine.md`.
- Make sure `data/tracking/weekly_progress.csv` exists (it should — header-only file shipped with the repo).

### 2. Run the routine

Type one of these in Claude Code:

```
/profiletap-weekly-routine 2026-05-18
```

Or omit the date to auto-pick the next upcoming Monday in IST:

```
/profiletap-weekly-routine
```

### 3. What it does

The command runs through the full prompt in `skills/profiletap-weekly-routine.md`, which:

1. Reads 11 input files (backlink_targets, outreach_tracker, content_calendar, weekly_progress, the 5 ProfileTap skills, aio-geo-playbook, claude-in-chrome-companion, and the most recent weekly brief).
2. Assesses 8 state categories (follow-ups due, outreach-ready domains, content blockers, last week's retro, DA backlog, etc.).
3. Picks one of 6 weekly themes based on the highest-leverage gap.
4. Builds the 51h Mon-Sat schedule for Rutuja, the ≤4h decision schedule for Pratima, and the ≤60 min schedule for Hariom — each task tagged with an explicit `**Owner:**`.
5. Writes the brief to `briefs/weekly/[YYYY-MM-DD]-week-of-[same]-team-brief.md`.
6. Appends one new row to `data/tracking/weekly_progress.csv` with planned values for the week.
7. Confirms the path, chosen theme, role time totals, and carryover items.

### 4. Fallback — no slash command available

If the slash command doesn't appear in Claude Code (e.g., wrong working directory, older Claude Code version), run it manually instead — open a Claude Code session from this directory and say:

> "Read `skills/profiletap-weekly-routine.md` and execute the routine for the week starting 2026-05-18."

The skill file is the source of truth; the slash command is just a thin wrapper that references it.

### 5. After the brief is generated

- **Rutuja** opens the new `briefs/weekly/[date]-team-brief.md` Monday morning and works through her Mon-Sat tasks.
- **Pratima** scans the `## Pratima's Decision Tasks` section at the top of the brief and books ≤4h across the week for her 9 decisions.
- **Hariom** scans `## Hariom's Founder Tasks` and blocks ≤60 min total — publishing the LinkedIn article Wednesday + Saturday-morning sign-offs.
- Rutuja fills the `_actual` columns in `data/tracking/weekly_progress.csv` during the week.
- Pratima writes the `pratima_retro_verdict` cell Saturday morning; Hariom signs off in `founder_signoff_status`. The next week's run reads those columns and shapes the next brief.

### 6. Optional — schedule it to run automatically

Once you're comfortable running it manually, you can use the `/schedule` skill to run `/profiletap-weekly-routine` every Sunday evening automatically. Ask Claude in a session:

> "Use /schedule to run /profiletap-weekly-routine every Sunday at 8pm IST."

This creates a cron-style remote agent that generates the next week's brief while you sleep, so Rutuja walks into a ready brief Monday morning.

### Companion docs the routine relies on

- `skills/profiletap-weekly-routine.md` — full generator prompt
- `docs/aio-geo-playbook.md` — schema markup, comparison content, AI directories, citation strategy (Friday block reads this)
- `docs/claude-in-chrome-companion.md` — delegation map for the parallel Claude Pro + Chrome extension session (paste-ready prompts for directory listings, DA research, HARO triage, etc.)
- `skills/profiletap-backlink-ops.md` — outreach email templates (1-7) + ownership convention

## Operating Rules

- One keyword intent maps to one page only — no cannibalization
- No content is created without a mapped target page
- India-first transactional opportunities are prioritized before broader global expansion
- Comparisons, use cases, and blogs support commercial landing pages — never compete with them
- Features are embedded into hub and child pages, not standalone pages, unless keyword data proves distinct intent
- Product family pages own buying intent; solution pages own use-case intent

## Objective

Build ProfileTap into:

- the leading smart identity platform in India
- a strong SEO authority across business and multi-use identity workflows
- a conversion-focused landing page system with sustainable backlink growth

## Key Files

| File | Purpose |
|------|---------|
| `data/keywords/raw_keyword_bank.csv` | Full keyword research inventory (232 rows) |
| `data/keywords/execution_seo_master.csv` | Canonical page-to-keyword families (one row per page) |
| `data/pages/page_master.csv` | Master page inventory with architecture |
| `data/content/content_calendar.csv` | Content production queue |
| `data/backlinks/backlink_targets.csv` | Link prospect list |
| `data/products/product_catalog.json` | Product catalog with variants and hub mapping |

## System Check

```bash
python scripts/validate_system.py
```

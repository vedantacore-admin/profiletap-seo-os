---
description: Generate the ProfileTap SEO weekly team brief for Rutuja + Pratima + Hariom (replaces the prior daily routine). Run every Sunday evening or Monday morning.
argument-hint: "[optional: target week start date, e.g. 2026-05-18]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

You are the ProfileTap SEO Operations Assistant. Generate this week's team brief by following the instructions in @skills/profiletap-weekly-routine.md exactly.

**Target week start date:** $ARGUMENTS

If $ARGUMENTS is empty, use the next upcoming Monday in IST as the week start date.

Critical reminders before you begin:
- Read all 11 input files listed in Step 1 of the skill before writing anything.
- Apply the three-role discipline: every task gets an **Owner:** tag (Rutuja / Pratima / Hariom).
- Rutuja totals exactly 51h across Mon-Sat. Pratima ≤4h. Hariom ≤60 min.
- For every CIC-eligible task type (per docs/claude-in-chrome-companion.md), include a `▶ Delegate to Claude-in-Chrome` sub-block with a paste-ready prompt.
- Write the brief to `briefs/weekly/[YYYY-MM-DD]-week-of-[same-date]-team-brief.md`.
- Append exactly one row to `data/tracking/weekly_progress.csv` with this week's planned values.
- Carry over any unresolved Pratima decisions and unmade Hariom signoffs from last week's row.

After generating the brief, confirm to the user:
1. The path to the new brief
2. The chosen weekly theme + the Step 2 evidence that drove the choice
3. The total scheduled time for each role (Rutuja / Pratima / Hariom)
4. A one-line summary of carryover items from last week
5. The new row that was appended to weekly_progress.csv

Do not begin until you've read all 11 input files.

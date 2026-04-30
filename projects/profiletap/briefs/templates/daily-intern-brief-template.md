# Daily SEO Intern Brief — Template Reference

> This file is a static reference template. The actual daily briefs are generated automatically each morning at 6 AM IST by the Claude scheduler and written to `briefs/daily/YYYY-MM-DD-intern-brief.md`.

---

## Brief Header

```
Date: YYYY-MM-DD
Brief ID: YYYY-MM-DD-1
Total Work Time: X hours Y minutes
Hub Focus: [business | creator | pet | family_safety | travel | vehicle | platform_publish]
Day Type: [Monday=Business | Tuesday=Creator+Comparison | Wednesday=Pet+FamilySafety | Thursday=Travel+Vehicle | Friday=PlatformPublish+Tracking]
```

---

## Section 1: Today's Focus

3–5 sentences summarizing:
- Which hub is prioritized today (based on hub-day rotation)
- Which domains are outreach-ready (pages moved to `draft_ready` or `published`)
- How many follow-ups are due
- Whether any DA research tasks are queued
- Any blockers (e.g., pages still at `planned` status)

**Example:**
> Today's focus is the business hub. Two P1 domains (inc42.com, businessworld.in) are outreach-ready because /digital-business-card-india moved to draft_ready. One follow-up is due for yourstory.com (contacted 6 days ago). DA research covers 4 P2 domains in the pet hub to prepare for Wednesday's outreach.

---

## Section 2: Work Schedule

Time-blocked tasks from 6:00 AM to ~12:00 PM IST (4–6 hours). Each block groups related task types.

### Block Format

```
### Block N — HH:MM AM – HH:MM AM | [Total minutes] min
**[Task type: Outreach / Follow-up / Platform Publish / DA Research / Tracking Update]**
```

### Task Format (within a block)

```
#### Task N: [domain.com] | [Task type] | [X] min

**Objective:** One sentence — what the intern must accomplish.

**Target page:** /page-slug
**Target keyword:** keyword phrase
**Suggested anchor:** anchor text from backlink_targets.csv
**Link angle:** angle_name from backlink_targets.csv
**Priority:** P1 / P2 / P3

**Outreach template to use:** [Template name from profiletap-backlink-ops.md]
  e.g. "Template 1: Founder Story" / "Template 2: Data-Backed Category" / "Template 3: Creator Marketing"
       "Template 4: Comparison Roundup" / "Template 5: Expert Roundup"

**Subject line:** [Exact recommended email subject line — ready to use]

**Personalization hooks:**
- [Hook 1: specific to this publication's editorial focus, recent article, or audience]
- [Hook 2: angle that connects ProfileTap to their readers' needs]

**Key message points:**
- [Point 1: relevant to this domain's audience]
- [Point 2]
- [Point 3]

**After sending:**
Update outreach_tracker.csv:
- status → contacted
- first_contact_date → today (YYYY-MM-DD)
- next_follow_up_date → today + 6 days (YYYY-MM-DD)
```

---

## Section 3: Platform Publish Content Block

Used on **Fridays** (platform publish rotation day) and any day with platform publish tasks.

For each platform publish task, the brief includes the full ready-to-publish content so the intern can copy-paste directly.

### Platform Publish Task Format

```
#### Task N: [platform.com] | Platform Publish | [X] min

**Platform:** [Reddit / Quora / Hashnode / Dev.to / Medium / LinkedIn / Blogger / GitHub]
**Post type:** [Reddit thread reply / Quora answer / Blog post / LinkedIn article / GitHub README]
**Target URL:** [Specific subreddit / Quora question / own profile URL to post to]
**ProfileTap link to embed:** /page-slug
**Anchor text:** anchor from backlink_targets.csv
**Link type:** Dofollow / Nofollow

**Publishing instructions:**
- [Any tags, categories, or formatting notes]
- [Target subreddit / topic / question to answer]

**Full post/answer content:**

---
[Full ready-to-publish text — 200–400 words for Quora/Reddit answers, 500–800 words for blog posts/articles]
---

**After publishing:**
Update outreach_tracker.csv:
- Add new row: domain, target_page_slug, status=contacted, first_contact_date=today, live_url=[published URL]
```

---

## Section 4: DA Research Task Format

Used when `da_score` is blank in backlink_targets.csv for P1 or P2 domains.

```
#### Task N: DA Research — [list of domains] | [X] min

**Objective:** Populate da_score in backlink_targets.csv for the listed domains.

**Domains to research:**
- domain1.com
- domain2.com
- domain3.com

**Tools to use (in order of preference):**
1. Moz DA Checker: https://moz.com/domain-analysis (free, 10 lookups/day)
2. Ahrefs Free Webmaster Tools: https://ahrefs.com/webmaster-tools (DR score, requires site verification)
3. SEMrush Domain Overview: https://www.semrush.com/analytics/overview/ (free tier: 10 results/day)

**How to record:**
- Open backlink_targets.csv
- Find the domain row
- Update da_score column with the integer value (e.g., 72)
- Save the file

**After completing:** Confirm all researched domains now have da_score populated in backlink_targets.csv.
```

---

## Section 5: Follow-Up Task Format

Used when `outreach_tracker.csv` has rows at `status=contacted` or `status=follow_up_1` with `next_follow_up_date` ≤ today.

```
#### Task N: Follow-Up — [domain.com] | [X] min

**Objective:** Send follow-up email to [domain contact name if known].
**Original outreach date:** first_contact_date from outreach_tracker
**Follow-up number:** #1 (6 days after first contact) / #2 (12 days) / #3 (18 days — final)

**Subject line:** Re: [original subject line]

**Follow-up message:**
[Brief 3–4 sentence follow-up — reference the original pitch, add one new value point, include the ProfileTap link again]

**After sending:**
Update outreach_tracker.csv:
- status → follow_up_1 (or follow_up_2, follow_up_3)
- last_contact_date → today
- next_follow_up_date → today + 6 days (or "final" if this is follow_up_3)
```

---

## Section 6: End-of-Day Checklist

```
## End-of-Day Checklist

### outreach_tracker.csv updates
- [ ] New outreach emails logged: status=contacted, first_contact_date=today, next_follow_up_date set
- [ ] Follow-ups logged: status updated, last_contact_date=today, next_follow_up_date updated
- [ ] Bounced emails noted in notes field

### backlink_targets.csv updates
- [ ] da_score populated for all researched domains
- [ ] Any domain moved from prospecting to outreach_started where first email was sent

### Platform publish
- [ ] Published URLs added to outreach_tracker.csv live_url field
- [ ] Platform post status logged

### General
- [ ] This brief filed (no action needed — generated automatically to briefs/daily/)
- [ ] Any blockers noted for tomorrow (pages still at planned, no contact found, bounce, etc.)
```

---

## Section 7: Tomorrow's Preview

1–2 sentences covering:
- Which follow-up dates fall tomorrow
- Which hub is up next in the rotation
- Whether any pages are expected to move to `draft_ready` that would unlock new outreach

**Example:**
> Tomorrow (Tuesday) is creator hub day. Follow-ups are due for exchange4media.com and socialsamosa.com. No new pages are expected to move to draft_ready overnight.

---

## Hub-Day Rotation Reference

| Day | Hub | Primary Task |
|-----|-----|--------------|
| Monday | Business | New outreach — P1 startup media, business media |
| Tuesday | Creator + Comparison | New outreach — marketing media, review blogs, comparison pages |
| Wednesday | Pet + Family Safety | Outreach + DA research for pet and family safety hubs |
| Thursday | Travel + Vehicle | Outreach + DA research for travel and vehicle hubs |
| Friday | Platform Publish + Tracking | Reddit/Quora/Hashnode posts + full tracking update |

> Follow-ups always take priority over the rotation regardless of day.

---

## Page Status Reference (when to outreach)

| content_calendar status | Outreach allowed? |
|------------------------|-------------------|
| planned | No — page not live |
| in_progress | No — page not live |
| draft_ready | Yes — page ready for launch |
| published | Yes — preferred |
| refresh_needed | Yes — existing live page |

---

## Outreach Template Reference

Templates are in `skills/profiletap-backlink-ops.md`. Quick reference:

| Template | Best for |
|----------|----------|
| Template 1: Founder Story | yourstory, inc42, entrackr, livemint, economictimes, linkedin |
| Template 2: Data-Backed Category | inc42, siliconindia, techcircle, businessworld |
| Template 3: Creator Marketing | exchange4media, socialsamosa, shoutmeloud |
| Template 4: Comparison Roundup | indianstartupnews, nextbigwhat, vccircle, reddit, quora |
| Template 5: Expert Roundup | techpp, freelancermap, medium, hashnode |

---

## Daily Brief File Naming

Output files are written by the scheduler to:
```
projects/profiletap/briefs/daily/YYYY-MM-DD-intern-brief.md
```

Example: `2026-05-05-intern-brief.md`

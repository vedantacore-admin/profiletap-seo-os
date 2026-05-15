# ProfileTap Weekly SEO Routine — Brief Generator

> **Purpose.** This is the master prompt that generates the ProfileTap SEO team's weekly work brief. Run it every Sunday evening (or first thing Monday) to produce the next week's `team-brief.md`. Replaces the previous daily routine.

You are the ProfileTap SEO Operations Assistant. Generate a structured **weekly** work brief for the SEO team, covering Monday through Saturday (51 hours for Rutuja + ≤4h for Pratima + ≤60 min for Hariom). The primary goal during the next 15-30 days (pre-launch) is to **grow domain authority + organic + referral traffic + AI citation share** via *controllable* channels — Hashnode/Medium dofollow articles, directory listings, Reddit/Quora answers, listicle inclusion outreach, AI-tool directories, comparison content, and schema markup. Cold journalist outreach is deprioritised (max 3 reference-led emails per week, Thursday only).

---

## The three roles (always use these names and scopes)

| Role | Name | Scope | Weekly hours |
|---|---|---|---|
| **SEO Manager (junior)** | **Rutuja** | Owns 95% of execution. Sends outreach, posts answers, runs directory listings, drafts content, updates trackers. Needs maximum hand-holding: every task copy-paste-ready, exact thread URLs, scripted tracker updates. No ambiguous "figure it out" tasks. | 51h (Mon-Sat 8.5h/day) |
| **Co-Founder, Content + SEO** | **Pratima Hariom Shah** | Owns content quality, SEO strategy, and outreach approval. Makes decisions Rutuja cannot. Every Pratima task is decision-shaped (choose option A/B/C, approve/reject, sign-off). Rutuja prepares the options; Pratima only chooses. | ≤4h |
| **Founder (technical)** | **Hariom Shah** | Owns the technical setup and founder voice. Tasks are founder-only: publish the weekly founder LinkedIn article, sign off on schema JSON-LD specs, sign off on the weekly retrospective verdict. | ≤60 min |

**Rules these roles produce:**
- Every task in the generated brief carries an `**Owner:**` tag at the top — `Rutuja` (default), `Pratima`, or `Hariom`.
- Pratima and Hariom each get a collated section at the top of the brief (`## Pratima's Decision Tasks` and `## Hariom's Founder Tasks`) so they can scan their week in one sitting without reading Rutuja's full schedule.
- Rutuja never sends new media outreach without Pratima's Monday approval of the target list.
- Hariom is never assigned an execution task — only decision, review, sign-off, or founder-voice content publish.
- If a Pratima section runs >4h or a Hariom section runs >60 min, the generator drops the lowest-leverage task and notes it in `## Carryover for next week`.

---

## Step 1 — Read these files before doing anything else

Read in this order. Do not start writing until all 10 are in context.

1. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/data/backlinks/backlink_targets.csv`
2. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/data/backlinks/outreach_tracker.csv`
3. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/data/content/content_calendar.csv`
4. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/data/tracking/weekly_progress.csv` — read the last row (last week's planned vs actual + Pratima's retro verdict + carryover decisions)
5. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/skills/profiletap-context.md`
6. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/skills/profiletap-backlink-ops.md`
7. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/skills/profiletap-content-brief.md`
8. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/skills/profiletap-blog-writer.md`
9. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/docs/aio-geo-playbook.md`
10. `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/docs/claude-in-chrome-companion.md` — delegation map + paste-ready prompts for the parallel Claude Pro + Chrome extension session
11. Most recent file under `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/briefs/weekly/` (last week's team brief, if any)

---

## Step 2 — Assess current state

Identify and write down (as a working scratchpad before drafting the brief) each of the following:

**A. FOLLOW-UPS DUE THIS WEEK** — highest priority, always scheduled into Monday Block 1
outreach_tracker rows where:
- status ∈ {contacted, follow_up_1, follow_up_2}
- AND (next_follow_up_date ≤ week_end_date OR next_follow_up_date is blank)

**B. OUTREACH-READY MEDIA TARGETS** (for Thursday's max-3 selective media block)
backlink_targets rows where:
- status = prospecting
- priority ∈ {P1, P2}
- target_page_slug maps to a page with content_calendar status ∈ {draft_ready, published}
- domain NOT already in outreach_tracker
- notes does NOT start with "Page not live"
- site_type is a reporter-first media outlet (not a directory or platform)

**C. OUTREACH-READY ROUNDUP / LISTICLE TARGETS** (for Thursday's roundup block + Tuesday's listicle block)
backlink_targets rows where:
- status = prospecting
- site_type ∈ {roundup_blog, comparison_review, niche_directory, expert_contribution, b2b_review_site}
- domain NOT already in outreach_tracker
- notes does NOT start with "Page not live"

**D. PLATFORM PUBLISH + DIRECTORY QUEUE**
backlink_targets rows where:
- status = prospecting
- site_type ∈ {developer_blog_platform, blog_platform, publishing_platform, qa_platform, community_platform, developer_community, startup_directory, profile_platform, newsletter_platform, social_platform, ai_tool_directory}
- domain NOT already in outreach_tracker
Priority order for Tuesday's directory block: producthunt.com, g2.com, capterra.com, crunchbase.com, saashub.com, alternativeto.net, startupindia.gov.in, about.me, betalist.com, getapp.com. Then AI directories (Tuesday Block 2): theresanaiforthat.com, futurepedia.io, aitoolsclub.com, futuretools.io, toolify.ai.

**E. CONTENT CALENDAR HEALTH**
- Pages in_progress for >5 days with no draft delivered — flag as at-risk; recommend an explicit Day 2 or Day 3 push this week to unblock
- Top 2 planned pages by priority that have no assigned writer and no draft_start_date — flag as candidates for Pratima's Saturday-AM "next week's hero" decision
- Hubs with <2 published or draft_ready pages — recommend a new prep candidate to Pratima Saturday
- A weekly brief must always schedule **at least 2 content prep pages** running end-to-end (page A: Day 1 Mon, Day 2 Tue, Day 3 Wed; page B: Day 1 Thu, Day 2 Fri, Day 3 Sat). If only one page is in motion the generator must propose a second prep candidate.

**F. TRACKING CLEANUP** (Saturday block)
outreach_tracker rows where:
- first_contact_date is blank and status is not "not_started", OR
- next_follow_up_date is blank and status ∈ {contacted, follow_up_1}, OR
- live_url is present but status is not "won" (platform post rows), OR
- status = won but live_url is blank

**G. LAST WEEK'S RETROSPECTIVE**
Read the most recent row of weekly_progress.csv. Specifically:
- `to_change_next_week` (Pratima's verdict — apply directly to this week's brief where applicable)
- `blockers` (any unresolved items — schedule them first this week)
- `pratima_decisions_pending_count` (any decisions not made last week — push them to Monday Block 1 of Pratima's section)
- `worked_well_notes` (what to do more of)
- response-rate comparison: `media_responses_received` vs `media_outreach_sent_actual`, and same for roundup/listicle/HARO — if any channel returned 0 for 2 weeks running, the generator should reduce its volume by 50% next week and increase a channel that returned >0.

**H. DA RESEARCH BACKLOG**
backlink_targets rows where:
- da_score is blank or empty
- priority ∈ {P1, P2}

---

## Step 3 — Choose the week's theme

Pick exactly one theme based on which gap in Step 2 is most acute. Theme determines Tue and Fri task density. Mon/Wed/Thu/Sat templates are fixed.

1. **Authority Push** — when last week shipped <2 platform articles or hub coverage gap is severe. Tue gets a Medium dofollow article slot in addition to listicle work; Fri swaps the comparison page for a second Hashnode article.
2. **Directory Blitz** — when fewer than 8 directory listings are won. Tue scales to 5 directory listings; Fri adds a ProductHunt prep sub-block.
3. **Listicle Inclusion Sprint** — when no listicle outreach has gone out in 2 weeks. Tue scales to 6 listicle emails; Thu drops media outreach to 1 and adds 3 more listicle emails.
4. **Content Prep Catch-up** — when 2+ pages are in_progress >5 days. Tue/Fri each devote an extra block to content production; Mon's Hashnode swap to a content-prep block.
5. **AIO/GEO Sprint** — when 0 comparison pages were drafted last week or no schema spec was approved by Hariom. Fri scales to 2 comparison pages + 2 schema specs; Thu's HARO block swaps in for a third comparison page.
6. **Community SEO Push** — when last week's organic_sessions_estimate dropped vs the prior week. Mon-Fri all add a third Reddit OR Quora answer; Thu's media block compresses.

State the chosen theme in the brief opening with one sentence on why (referencing the Step 2 evidence).

---

## Step 4 — Build the schedule (51h Rutuja + ≤4h Pratima + ≤60 min Hariom)

### Rutuja's Mon-Sat day template

All times IST. Each day = 6 blocks + 15-min mid-morning break + 45-min lunch = 8.5h.

#### Monday — Retro + Authority Publishing

- **Block 1 (9:00-10:30 AM, 90 min)** — Read last week's retro (15 min) → send all due follow-ups in one batch (15 min each, up to 5 follow-ups) → if budget remains, prep Tuesday's directory listing logins
- **Block 2 (10:30-11:45 AM, 75 min)** — Publish 1 Hashnode dofollow article (uses last week's prepped page; Pratima approves draft in her Tue PM slot — for Monday Block 2 Rutuja publishes whichever article Pratima approved in last week's Sat handoff)
- **Break (11:45-12:00, 15 min)**
- **Block 3 (12:00-1:15 PM, 75 min)** — Content Prep Day 1 — keyword + structure brief for this week's Page A (Pratima picked Saturday)
- **Lunch (1:15-2:00, 45 min)**
- **Block 4 (2:00-3:30 PM, 90 min)** — 2 Reddit answers + 2 Quora answers (rotate subreddits + question follower-count priorities)
- **Block 5 (3:30-4:30 PM, 60 min)** — DA research catch-up (3-6 blank domains from category H)
- **Block 6 (4:30-5:15 PM, 45 min)** — Tracker update + plan Tue + write next-day handoff note

#### Tuesday — Directory + Listicle (theme-dependent density)

- **Block 1 (9:00-10:30 AM, 90 min)** — 3 directory listings (rotate the 10-platform pool; theme=Directory Blitz scales to 5)
- **Block 2 (10:30-11:45 AM, 75 min)** — 2 AI-tool directory submissions (theresanaiforthat, futurepedia, etc.)
- **Break (11:45-12:00, 15 min)**
- **Block 3 (12:00-1:15 PM, 75 min)** — 3 listicle inclusion emails to existing "Top X NFC business cards India" or similar roundups (theme=Listicle Sprint scales to 6)
- **Lunch (1:15-2:00, 45 min)**
- **Block 4 (2:00-3:30 PM, 90 min)** — Content Prep Day 2 — full draft of Page A
- **Block 5 (3:30-4:30 PM, 60 min)** — 2 Quora answers
- **Block 6 (4:30-5:15 PM, 45 min)** — Tracker update + ping Pratima for Tue PM Hashnode review (which she does in her own time)

#### Wednesday — Community SEO + Cross-post

- **Block 1 (9:00-10:30 AM, 90 min)** — Cross-post Hariom's LinkedIn founder article (which Hariom publishes Wed AM) to 3 Indian FB/community groups + create 5 Pinterest pins linking to the article and to 2 priority profiletap.io pages
- **Block 2 (10:30-11:45 AM, 75 min)** — 3 Quora answers (Wednesday is peak India traffic day on Quora)
- **Break (11:45-12:00, 15 min)**
- **Block 3 (12:00-1:15 PM, 75 min)** — 2 Reddit answers
- **Lunch (1:15-2:00, 45 min)**
- **Block 4 (2:00-3:30 PM, 90 min)** — Content Prep Day 3 — finalise Page A; output goes to dev for publishing
- **Block 5 (3:30-4:30 PM, 60 min)** — Indian community participation: 30 min on 1 Slack/Discord/FB group (provide value, no link spam — link in profile), 30 min on 1 IndieHackers/r/SaaS/r/Entrepreneur thread participation
- **Block 6 (4:30-5:15 PM, 45 min)** — Tracker update + handoff Page A to dev with publish checklist

#### Thursday — Selective Media + HARO

- **Block 1 (9:00-10:30 AM, 90 min)** — Draft 3 reference-led journalist tips (one per target Pratima approved Monday). Each requires reading 1 article published in the last 30 days on the target publication. **If no fresh article exists for any target, swap that slot for an additional roundup blog email in Block 2.** All drafts go to Pratima for PM approval — Rutuja does NOT send until Pratima signs off.
- **Block 2 (10:30-11:45 AM, 75 min)** — 2 roundup blog outreach emails (always — these respond 5-10x higher than cold media). Format: expert quote / inclusion request to a published roundup.
- **Break (11:45-12:00, 15 min)**
- **Block 3 (12:00-1:15 PM, 75 min)** — 3 HARO / Featured / Qwoted / SourceBottle / Help-A-B2B-Writer pitches. Journalists are looking for sources — response rate is 20-30%.
- **Lunch (1:15-2:00, 45 min)**
- **Block 4 (2:00-3:30 PM, 90 min)** — Publish 1 Substack OR Medium dofollow article (cross-post Monday's Hashnode with India-stat refresh; Medium uses inline dofollow links)
- **Block 5 (3:30-4:30 PM, 60 min)** — Content Prep Day 1 — Page B begins (keyword + structure brief)
- **Block 6 (4:30-5:15 PM, 45 min)** — Tracker update + after Pratima signs the 3 media drafts, send the approved ones

#### Friday — AIO/GEO + Comparison

- **Block 1 (9:00-10:30 AM, 90 min)** — Schema audit on 1 priority page + draft JSON-LD spec (one of: FAQPage, Product, Article, HowTo, LocalBusiness, ItemList — match page type per aio-geo-playbook.md §3). Output saved to `/projects/profiletap/docs/schema-specs/[page-slug]-[YYYY-MM-DD].json` for Hariom's Saturday sign-off.
- **Block 2 (10:30-11:45 AM, 75 min)** — Draft 1 comparison page ("ProfileTap vs [X]" — Pratima picked competitor Monday). 1200-1800 words, comparison table required, India-specific differentiator required. Output to `/briefs/content-prep/[YYYY-MM-DD]-vs-[competitor]-comparison.md`.
- **Break (11:45-12:00, 15 min)**
- **Block 3 (12:00-1:15 PM, 75 min)** — AI-citable content audit on 1 priority page — answer 5 likely AI queries in answer-shaped paragraphs (use aio-geo-playbook.md §4-5 checklist). Output: an amendment doc the dev team applies.
- **Lunch (1:15-2:00, 45 min)**
- **Block 4 (2:00-3:30 PM, 90 min)** — Content Prep Day 2 — full draft of Page B
- **Block 5 (3:30-4:30 PM, 60 min)** — 3 GitHub Awesome-list inclusion pitches (e.g., awesome-saas, awesome-nfc, awesome-india-startups, awesome-business-tools) + 2 Quora answers
- **Block 6 (4:30-5:15 PM, 45 min)** — Tracker update + draft Saturday's weekly retro shell (planned vs actual numbers ready for Pratima)

#### Saturday — Catch-up + Retro Wrap

- **Block 1 (9:00-10:30 AM, 90 min)** — Fill weekly_progress.csv `_actual` columns + write retro draft (worked_well_notes, blockers, recommended `to_change_next_week`) — hand to Pratima for her AM verdict
- **Block 2 (10:30-11:45 AM, 75 min)** — Wikipedia/Wikidata sources audit — list every verifiable secondary source mentioning ProfileTap (no submission — that's Hariom's call post-launch)
- **Break (11:45-12:00, 15 min)**
- **Block 3 (12:00-1:15 PM, 75 min)** — Press kit / media room content update — founder bio, fact sheet, product images, latest mentions index (Pratima reviews same morning)
- **Lunch (1:15-2:00, 45 min)**
- **Block 4 (2:00-3:30 PM, 90 min)** — Content Prep Day 3 — finalise Page B
- **Block 5 (3:30-4:30 PM, 60 min)** — Buffer for spillover from any earlier day
- **Block 6 (4:30-5:15 PM, 45 min)** — Hand retro draft + next-week recommendations to Pratima; queue any unresolved items as Sunday-evening "next brief generation" inputs

### Pratima's Decision Tasks (~3-4h total — schedule flexibly inside her own calendar)

The brief lists these in a collated section at the top, with day/time recommendation, exact deliverable, and a `Rutuja's pre-work` section showing the options or draft Pratima only needs to choose / approve.

1. **Monday morning, 15 min** — Read brief Snapshot + approve weekly theme (Rutuja proposes one, Pratima picks final).
2. **Monday morning, 20 min** — Approve list of 3 media outreach targets for Thursday. Rutuja's pre-work: 5 candidate domains pre-listed with link angle + page slug + reason; Pratima picks 3.
3. **Monday morning, 10 min** — Pick competitor for Friday's comparison page. Rutuja's pre-work: 3 candidates from aio-geo-playbook.md §7 backlog with India search volume; Pratima picks 1.
4. **Tuesday afternoon, 30 min** — Review and approve Monday's Hashnode article draft before Rutuja publishes. Rutuja's pre-work: full draft saved to `/briefs/content-prep/[YYYY-MM-DD]-hashnode-[topic].md`.
5. **Wednesday morning, 45 min** — Review 2-3 content prep briefs delivered last week (Day 1/2 outputs in `/briefs/content-prep/`). Catches structural issues before Day 2 drafts compound errors. Verdict: approve / request revisions.
6. **Thursday afternoon, 30 min** — Approve & send 3 media emails Rutuja drafted in Thu Block 1 (or send back for rewrite). Rutuja's pre-work: 3 drafts in `/briefs/content-prep/[YYYY-MM-DD]-media-drafts.md`, each with subject line + body + tracker row pre-filled.
7. **Friday afternoon, 30 min** — Review Friday's comparison page draft + AI-citable audit findings. Verdict: approve / request edits / hand to dev for publishing.
8. **Saturday morning, 45 min** — Read Rutuja's retro draft, write 3-line `to_change_next_week` note, finalise weekly_progress.csv row (Pratima types into the `pratima_retro_verdict` cell directly).
9. **Saturday morning, 15 min** — Decide next Monday's hero content prep page from content_calendar `planned` queue. Rutuja's pre-work: 3 candidate slugs with priority + keyword volume + hub gap reasoning.

### Hariom's Founder Tasks (≤60 min total)

1. **Wednesday morning, 40 min** — Edit + publish 1 LinkedIn founder article. Rutuja's pre-work: starter draft 500-700 words in `/briefs/content-prep/[YYYY-MM-DD]-linkedin-founder.md`, India-market insight, founder voice scaffolding, target slug for inline link. Hariom personalises tone and publishes from his personal LinkedIn.
2. **Saturday morning, 10 min** — Review schema JSON-LD spec Rutuja delivered Friday at `/docs/schema-specs/[page-slug]-[YYYY-MM-DD].json`. Verdict: ship to dev / push back. Yes/no decision, no rewriting.
3. **Saturday morning, 10 min** — Read Pratima's `to_change_next_week` note in weekly_progress.csv. One-line founder sign-off if change affects strategy or budget. Type into `founder_signoff_status` cell.

---

## Step 5 — Write the brief

Determine today's date in IST (UTC+5:30) and the upcoming Monday's date (week_start_date). Write the brief to:

`/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/briefs/weekly/[week_start_YYYY-MM-DD]-week-of-[same-date]-team-brief.md`

Use this exact top-level structure:

```
# ProfileTap SEO Weekly Team Brief — Week of [Mon DD Mon YYYY] (IST)

## This Week's Theme
**Theme:** [one of the 6 themes from Step 3]
**Why:** [1 sentence citing the Step 2 evidence — e.g. "Last week shipped 0 platform articles and yourstory follow-up is 11 days overdue."]

## Snapshot
### Hub Health
[Markdown table: hub | total pages | draft_ready | in_progress | planned]

### Outreach Pipeline
[Markdown table: status | count | trend vs last week]

### Follow-ups Due This Week
[Markdown table: domain | status | next_follow_up_date | overdue_by_days | target_page_slug]

### Content Blockers
[Bullet list of pages in_progress >5 days with the unblock action and Rutuja's day this week to push them]

### Carryover from Last Week
[Pratima's `to_change_next_week` note from last weekly_progress row, plus any `pratima_decisions_pending` items scheduled into Monday]

## Pratima's Decision Tasks (~Xh this week)
[9 items, each in the format:

### Pratima-1: [decision name] | [Day AM/PM] | [N] min
**Deliverable:** [exact one-line output]
**Rutuja's pre-work (already done):** [the 3 options OR the draft link OR the existing data]
**Pratima's decision:** [pick / approve-reject / sign-off]
**Owner:** Pratima
]

## Hariom's Founder Tasks (≤60 min this week)
[3 items, same format with Owner: Hariom]

## Rutuja's Day-by-day Schedule

### Monday [DD Mon] — Retro + Authority Publishing
[6 blocks. Each block lists tasks with full ID like T-MON-1, T-MON-2 etc.]

### Tuesday [DD Mon] — Directory + Listicle
[...]

### Wednesday [DD Mon] — Community SEO + Cross-post
[...]

### Thursday [DD Mon] — Selective Media + HARO
[...]

### Friday [DD Mon] — AIO/GEO + Comparison
[...]

### Saturday [DD Mon] — Catch-up + Retro Wrap
[...]

## Full Task Details (copy-paste ready)
[All Rutuja tasks expanded — use the task format rules in the next section. Pratima tasks above already contain Rutuja's pre-work links. Hariom tasks above contain the founder-article starter draft inline.]

## End-of-Week Checklist (Rutuja completes Saturday)
- [ ] All follow-ups due this week sent — tracker updated with last_contact_date and next_follow_up_date
- [ ] 3 media outreach emails approved by Pratima + sent (or noted as "no fresh article" with substitute roundup email logged)
- [ ] 2 roundup blog outreach emails sent
- [ ] 3 HARO/Featured/Qwoted pitches sent
- [ ] 3 listicle inclusion emails sent
- [ ] 3 directory listings completed — live_url logged, status set to won
- [ ] 2 AI-tool directory submissions completed
- [ ] 6 Reddit answers posted — live_urls logged, status set to won
- [ ] 7 Quora answers posted — live_urls logged, status set to won
- [ ] 1 Hashnode dofollow article published — live_url logged, status set to won
- [ ] 1 Hariom LinkedIn founder article published — live_url logged, status set to won
- [ ] 1 Substack or Medium article published — live_url logged
- [ ] 5 Pinterest pins published with profiletap.io links
- [ ] 3 GitHub Awesome-list inclusion pitches sent
- [ ] 2 content prep pages completed end-to-end (Page A by Wed, Page B by Sat)
- [ ] 1 schema spec drafted Friday + Hariom sign-off received Saturday
- [ ] 1 comparison page drafted Friday + Pratima review received Friday PM
- [ ] 1 AI-citable content audit delivered to dev
- [ ] Wikipedia/Wikidata sources audit list updated
- [ ] DA scores updated in backlink_targets.csv for all researched domains
- [ ] Tracking cleanup complete — no active rows with blank date fields remain
- [ ] No outreach sent to any domain where notes starts with "Page not live"
- [ ] No outreach sent to any page with content_calendar status = planned
- [ ] weekly_progress.csv `_actual` columns filled in
- [ ] Pratima `pratima_retro_verdict` received
- [ ] Hariom `founder_signoff_status` received

## Next Week's Preview
[2-3 sentences. Rutuja drafts Saturday morning, Pratima reviews same day.
- Specific domains with follow-up dates next week, by name
- Which hub rotates next
- Page A and Page B status for next week (will any roll over?)
- Suggested theme for next week]
```

---

## Task format rules — use these for every task type

These mirror the daily routine's task formats, with caps adjusted to weekly volumes. Every task block in `## Full Task Details` follows the matching template below.

### New outreach email — reference-led media (Thursday only, max 3/week)

```
#### Task T-THU-N: [domain.com] | New Outreach (reference-led) | 30 min
**Owner:** Rutuja drafts → Pratima approves Thu PM → Rutuja sends

**Objective:** [1 sentence — link placement targeted]

**Target page:** /[slug]
**Target keyword:** [from backlink_targets]
**Suggested anchor:** [from backlink_targets]
**Link angle:** [from backlink_targets]
**Priority:** P1 / P2

**Outreach template to use:** Template 1 / 2 / 4 from profiletap-backlink-ops.md (reporter-first publications: reference-led journalist tip ONLY — no expert quote blocks)

**Pre-send step (5 min):** Visit [domain.com] and find 1 article published in the last 30 days covering [relevant topic]. Note title + URL. Reference it in the first line of your email. If no recent relevant article exists, **skip this target and substitute a roundup blog email instead** — do NOT use a generic subject line.

**Subject line (reference-led):**
Re: your [article topic] piece — a data point on [India-specific angle]

**India-specific angle to lead with:** [WhatsApp masking / INR pricing / QR-native UPI behaviour / Bharat market / Tier 2/3 SMB / WhatsApp B2B — one specific detail]

**Full email (copy-paste ready, ≤120 words):**
---
[Reference-led opening (1 sentence naming their article) → India-specific trend or data point (1-2 sentences) → ProfileTap as relevant context (1-2 sentences, no feature list) → soft CTA (1 sentence). Journalist tone — no PR fluff, no bullets, no quote block.]
---

**After Pratima approves and Rutuja sends — update outreach_tracker.csv:**
- domain: [domain]
- target_page_slug: [slug]
- contact_name: [specific name if found, else Editorial Team]
- contact_email: [email]
- status: contacted
- first_contact_date: [today YYYY-MM-DD]
- next_follow_up_date: [today + 7 days]
- notes: reference-led tip — referenced [article title] published [date]
```

### New outreach email — roundup blog / listicle inclusion (Tue + Thu, 5/week total)

```
#### Task T-XXX-N: [domain.com] | Listicle Inclusion | 25 min
**Owner:** Rutuja

**Objective:** Request inclusion in their existing "[roundup title]" post, with anchor [from backlink_targets] linking to /[slug].

**Target page:** /[slug]
**Existing article URL:** [find via Google: site:domain.com "NFC business card" OR "digital business card" India]
**Suggested anchor:** [from backlink_targets]

**Pre-send step (5 min):** Read the existing article carefully — note which competitors are listed (Blinq, HiHello, Linktree, etc.) and what differentiators each is given. Your pitch references this directly.

**Subject line:**
Quick suggestion for your [roundup topic] post — one India-built option you may have missed

**Full email (copy-paste ready, ≤90 words):**
---
Hi [first name if found, else Editor],

Just read your [roundup title] from [pub date] — good list. I noticed you cover [Blinq / HiHello / X], all built for US markets.

One India-built option worth a mention: ProfileTap ([slug URL]) — INR pricing, WhatsApp masking built in, and India's first NFC card with multi-profile identity (business + personal + pet etc on one card). Used by [X] Indian professionals so far.

Happy to send specs / images / a comparison row if useful. No worries if not a fit.

[Sign-off]
---

**After sending — update outreach_tracker.csv:**
- domain: [domain]
- target_page_slug: [slug]
- contact_name / contact_email
- status: contacted
- first_contact_date: [today]
- next_follow_up_date: [today + 7 days]
- notes: listicle inclusion request — referenced [their article title]
```

### New outreach email — HARO / Featured / Qwoted / SourceBottle pitch (Thu, 3/week)

```
#### Task T-THU-N: [platform.com] HARO | Expert Pitch | 25 min
**Owner:** Rutuja

**Source platform:** HARO / Featured / Qwoted / SourceBottle / Help-a-B2B-Writer
**Query matched:** [exact journalist query text — found by scanning daily HARO / Featured emails or platform inbox]
**Query topic:** [one-line summary]
**Publication targeted:** [where the journalist is writing for]

**Pre-send step (3 min):** Re-read the journalist's exact requirements. Word count cap, deadline, format (quote / paragraph / bullet list).

**Full response (copy-paste ready — match the journalist's requested format and length):**
---
[Direct answer first. Concrete India-specific insight (data, observation, example). Quotable line that a journalist can lift verbatim. Brief credential line: "ProfileTap — India's multi-identity NFC + QR platform, used by Indian professionals across 6 contexts (business, creator, family safety, pet, travel, vehicle)." Single inline link to the most relevant /slug. Sign-off with name + title + 1-line bio + 1-line photo URL.]
---

**Required attribution:** "Source: [Name], Founder/Co-Founder, ProfileTap (profiletap.io)" + 1 inline link to /[slug]

**After submitting — update outreach_tracker.csv:**
- domain: [target publication — if known — else "haro-pitch"]
- target_page_slug: /[slug]
- status: contacted
- first_contact_date: [today]
- next_follow_up_date: [leave blank — HARO is one-shot]
- notes: HARO pitch — [query topic] — deadline [date] — pub: [name]
```

### Follow-up email (Mon, batched)

```
#### Task T-MON-N: [domain.com] | Follow-up #[1/2/3] | 15 min
**Owner:** Rutuja

**Objective:** Send follow-up [N] — [X] days since first contact on [first_contact_date].

**Contact:** [name] — [email]
**Original send date:** [first_contact_date]
**Original subject line:** [from tracker]
**Follow-up subject line:** Re: [original subject]

**Full follow-up email (copy-paste ready, ≤60 words):**
---
[1-line recap of original pitch → 1 NEW India-specific hook or data point not used in original email → ProfileTap page link → single soft question CTA. No "just checking in." Every follow-up adds new value.]
---

**After sending — update outreach_tracker.csv:**
- status: follow_up_[N]
- last_contact_date: [today]
- next_follow_up_date: [today + 7 days], OR "final" if this is follow_up_3
```

### Reddit answer (Mon Block 4, Wed Block 3 — 6/week total)

```
#### Task T-XXX-N: reddit.com | Answer | 25 min
**Owner:** Rutuja

**ProfileTap link to embed:** /[slug]
**Link type:** Nofollow

**Pre-task (5 min) — search Reddit for:**
- [Query 1 — matches target page keyword]
- [Query 2 — India-specific variant]
- [Query 3 — competitor or comparison angle]

**Target subreddits to prioritise:** r/india, r/IndiaInvestments, r/startups, r/Entrepreneur, r/smallbusiness, r/SaaS, r/IndianStreetBets (for digital business + finance crossover)

**Why this thread (Rutuja fills in after picking):** [1 sentence — comment count, upvote score, last activity within 90 days, keyword match]

**Answer (copy-paste ready — adapt opening to the specific question asked, 200-300 words):**
---
[Direct answer in first sentence — not "I work at ProfileTap" or "Great question". India-specific context. ProfileTap recommended in body with 1 bare URL. Practical next step for the reader. Useful even if they don't click.]
---

**Posting rules:**
- No-self-promo subreddits: skip
- Threads >90 days inactive: skip
- Max 1 ProfileTap link across all Reddit comments per day

**After posting — add new row to outreach_tracker.csv:**
- domain: reddit.com
- target_page_slug: /[slug]
- status: won
- first_contact_date: [today]
- live_url: [comment URL]
- notes: Reddit answer — r/[subreddit] — [thread title]
```

### Quora answer (Mon Block 4, Tue Block 5, Wed Block 2, Fri Block 5 — 7/week total)

```
#### Task T-XXX-N: quora.com | Answer | 25 min
**Owner:** Rutuja

**ProfileTap link to embed:** /[slug]
**Link type:** Nofollow

**Pre-task (5 min) — search Quora for:**
- [Query 1] / [Query 2 India variant] / [Query 3 comparison]

**Why this question (Rutuja fills in):** [follower count — prioritise 500+; keyword match to /slug]

**Answer (copy-paste ready, 250-400 words):**
---
[Direct answer first → India-specific framing → criteria for evaluating options in the category (not only ProfileTap) → ProfileTap as concrete recommendation with inline link → practical close.
Required at end: "Disclosure: I work with ProfileTap."]
---

**After posting — add new row to outreach_tracker.csv:**
- domain: quora.com
- target_page_slug: /[slug]
- status: won
- first_contact_date: [today]
- live_url: [answer URL]
- notes: Quora answer — [question title] — [follower count] followers
```

### Hashnode article (Monday, 1/week)

```
#### Task T-MON-2: hashnode.com | Article | 75 min
**Owner:** Rutuja publishes (Pratima approved draft in last week's Tue PM slot)

**Platform:** Hashnode (DA 91, dofollow)
**Where to post:** ProfileTap team Hashnode (create if not exists)
**ProfileTap link to embed:** /[slug] with anchor [from backlink_targets]
**Link type:** Dofollow

**Title (SEO-optimised — already in approved draft):**
[Keyword phrase]: [specificity / year / India qualifier]

**Target keyword:** [keyword] — [estimated India search volume]
**Search intent:** informational / comparison / transactional
**Tags:** [3-5 India tech + startup audience tags]

**Full article (copy-paste ready — already in /briefs/content-prep/[YYYY-MM-DD]-hashnode-[topic].md after Pratima approval):**

[Full 700-900 words follows structure:
Para 1 hook — reader's problem or India-specific gap; first paragraph contains target keyword
Para 2-3 context — India-specific framing (WhatsApp / UPI / INR / Bharat / Tier 2-3 SMB)
Para 4-5 substance — comparison criteria, how-to, evaluation framework
Para 6 recommendation — ProfileTap with 1 inline dofollow link at target anchor
Para 7 close — practical next step or question]

**After publishing — add new row to outreach_tracker.csv:**
- domain: hashnode.com
- target_page_slug: /[slug]
- status: won
- first_contact_date: [today]
- live_url: [article URL]
- notes: Dofollow — target keyword: [keyword] — [word count] words
```

### LinkedIn founder article (Wednesday — Hariom's only execution task)

```
#### Task T-WED-Hariom: linkedin.com | Founder Article | 40 min
**Owner:** Hariom Shah (founder) — Rutuja prepared starter draft below

**Platform:** LinkedIn (DA 99, nofollow but extreme referral + AI training corpus value)
**Where to post:** Hariom's personal LinkedIn profile (NOT company page)
**ProfileTap link to embed:** /[slug]
**Link type:** Nofollow — value is brand distribution and AI citation, not link equity

**Title (Rutuja-drafted, Hariom can personalise):**
[Founder voice, conversational, India professional context — e.g. "Why Indian professionals juggle 3 identities and how we're fixing it" or "What I learned building India's first multi-context identity platform"]

**Starter draft (500-700 words, founder voice — Hariom edits in his own voice and publishes):**

[Saved to /briefs/content-prep/[YYYY-MM-DD]-linkedin-founder.md — Rutuja's pre-work.

Structure:
- Personal observation or India-market insight (2-3 sentences)
- The professional problem this creates for Indian founders / SMBs
- What a better system looks like
- ProfileTap as an example of that system with 1 inline link
- Closing observation or question to drive comments]

**Mandatory India-specific element (at least one):**
- How WhatsApp drives B2B follow-up in India
- Why call masking matters in Indian professional culture
- How UPI normalised QR scanning across Bharat
- Why INR pricing signals trust to Indian buyers
- Tier 2/3 SMB adoption of digital identity

**After Hariom publishes — Rutuja adds new row to outreach_tracker.csv:**
- domain: linkedin.com
- target_page_slug: /[slug]
- status: won
- first_contact_date: [today]
- live_url: [article URL]
- notes: Nofollow — LinkedIn founder article — Hariom Shah personal profile — [word count] words
```

### Substack OR Medium article (Thursday, 1/week — alternate weekly)

```
#### Task T-THU-4: [substack.com OR medium.com] | Platform Article | 90 min
**Owner:** Rutuja

**Platform:** Substack (newsletter, nofollow) OR Medium (DA 96, inline dofollow)
**Cross-post source:** Mon's Hashnode article — refresh with 1 new India-stat or angle for this platform's audience
**ProfileTap link to embed:** /[slug]
**Anchor text:** [from backlink_targets]

[Title + tags + 400-600 words refreshed body, same structural rules as Hashnode adapted for platform tone]

**After publishing — add new row to outreach_tracker.csv:**
- domain: [substack.com OR medium.com]
- target_page_slug: /[slug]
- status: won
- live_url: [post URL]
- notes: [Dofollow/Nofollow] — cross-post of Hashnode article with India-stat refresh
```

### Directory listing (Tuesday Block 1, 3/week)

```
#### Task T-TUE-N: [platform.com] | Directory Listing | 25 min
**Owner:** Rutuja

**Platform:** [G2 / Capterra / Crunchbase / SaaSHub / AlternativeTo / ProductHunt / StartupIndia / About.me / BetaList / GetApp]
**Where to list:** [Exact URL — claim existing OR create new]
**ProfileTap link to embed:** /[slug]
**Link type:** [Dofollow / Nofollow]
**DA / Monthly traffic:** [from backlink_targets]

**Pre-task:** Search [platform] for "ProfileTap" — if profile exists, claim. If not, create new with content below.

**Profile content (copy-paste ready — fill every field, no blanks):**

Company name: ProfileTap
Website: https://profiletap.io
Short description (≤200 chars): [platform-search-algorithm-tuned line]
Full description (400-600 chars): [India-first positioning + multi-context identity + 6 use cases (business, creator, family safety, pet, travel, vehicle)]
Categories: [every relevant category on this platform]
Pricing: Freemium — free tier available, paid from ₹499
Deployment: Cloud / SaaS / Web-based / Mobile
Target market: Small Business, Mid-Market, India, Global
HQ: Palghar, Maharashtra, India
Founded: [confirm with Hariom before submitting if not already on file]

**After completing — add new row to outreach_tracker.csv:**
- domain: [platform.com]
- target_page_slug: /[slug]
- status: won
- first_contact_date: [today]
- live_url: [profile URL once live]
- notes: [Dofollow/Nofollow] — DA [X] — [reason this listing matters]
```

### AI-tool directory submission (Tuesday Block 2, 2/week)

```
#### Task T-TUE-N: [ai-directory.com] | AI Directory Submission | 30 min
**Owner:** Rutuja

**Directory:** [theresanaiforthat.com / futurepedia.io / aitoolsclub.com / futuretools.io / toolify.ai / aiparabellum.com / supertools.therundown.ai / aimagictools.com / aitoolsdirectory.com / easywithai.com / saashub.com / alternativeto.net]
**Submission URL:** [exact submit page]
**AI feature to highlight:** [ai_review_assist / business_ai] — ProfileTap's AI helps SMBs draft business replies and request reviews

**Profile content (copy-paste ready — fill every field):**

Tool name: ProfileTap
Tagline: India's multi-identity NFC + QR platform with AI review assist
Website: https://profiletap.io
Short description: [≤200 chars, lead with AI angle + India context]
Full description: [400-600 chars covering: 6 hubs, 13 features, AI review assist, India-first INR pricing, WhatsApp masking]
Categories: AI for Business, AI Customer Engagement, SaaS Tools, Digital Identity, NFC Tools, Indian SaaS
Pricing: Freemium
Platform: Web, Mobile (iOS, Android)
Use case: [pick the one that matches the directory's audience best]

**After submission — add new row to outreach_tracker.csv:**
- domain: [ai-directory.com]
- target_page_slug: /[slug]
- status: contacted (waiting for review) OR won (if listed immediately)
- first_contact_date: [today]
- next_follow_up_date: [today + 14 days — most directories review in 1-2 weeks]
- notes: AI directory submission — [feature angle] — review pending
```

### Content prep task (every day Mon-Sat)

```
#### Task T-XXX-N: Content Prep — Page [A/B] /[slug] | Day [1/2/3] | [45 / 90 / 45] min
**Owner:** Rutuja drafts → Pratima reviews Wed AM (Day 1) or Thu PM (Day 2) or as scheduled

**Page:** /[slug]
**Page type:** blog / category / use-case / comparison / hub
**Hub:** business / creator / pet / family_safety / travel / vehicle
**Target keyword:** [primary keyword]
**Search intent:** informational / comparison / transactional
**Current status in content_calendar:** planned / in_progress
**Why this page (Pratima selected Saturday):** [1 sentence — hub gap / no India-specific result ranks / blocking outreach to specific domains]

**Today's deliverable (Day [N]):**
[Day 1 — keyword + structure brief → /briefs/content-prep/[YYYY-MM-DD]-[slug]-prep.md
 Day 2 — full draft → /briefs/content-prep/[YYYY-MM-DD]-[slug]-draft.md
 Day 3 — final reviewed draft with SEO elements → ready for dev publishing]

[Full template content for that Day — same as daily routine, no changes to internal template structure]

**After completing — update content_calendar.csv for /[slug]:**
- Day 1: status → in_progress, assigned_writer → Rutuja, draft_start_date → [today], target_draft_date → [today+2], target_publish_date → [today+5]
- Day 2: brief_status → draft_ready
- Day 3: status → draft_ready, ready for dev handoff
```

### DA research (Monday Block 5)

```
#### Task T-MON-5: DA Research — [domain1], [domain2], [domain3] | 20 min per batch
**Owner:** Rutuja

**Domains to research (3 per batch):**
- [domain1.com] — current recorded score: [X or blank]
- [domain2.com] — current recorded score: [X or blank]
- [domain3.com] — current recorded score: [X or blank]

**Tools (in order of preference):** Moz DA Checker (moz.com/domain-analysis, 10 free/day) → Ahrefs Free Webmaster Tools → SEMrush free tier

**Threshold rule:** Any verified DA <30 → DO NOT outreach. Add notes: "DA below threshold — hold outreach until DA ≥ 30 — verified [date]."

**After completing — update backlink_targets.csv da_score column with verified integer. If score moved ±5 from previous, add note: "DA updated from [X] to [Y] on [date]."**
```

### Tracking update (every day Mon-Sat Block 6, plus Sat Block 1)

```
#### Task T-XXX-Last: Tracking Update — outreach_tracker.csv | 45 min
**Owner:** Rutuja

**Today's incomplete rows (from Step 2 category F):**
[list each row with the field that needs fixing and the correct value]

**Instructions:**
1. Platform post rows with live_url present and status ≠ won: set status → won, last_contact_date → first_contact_date, leave next_follow_up_date blank
2. contacted rows missing next_follow_up_date: set to first_contact_date + 7 days
3. follow_up_1 rows missing next_follow_up_date: set to last_contact_date + 7 days
4. won rows with blank live_url: flag note "live_url missing — verify post is still live and add URL"
5. Duplicates: keep most recent contact date row, mark the other as duplicate in notes
```

### Schema spec drafting (Friday Block 1)

```
#### Task T-FRI-1: Schema JSON-LD Spec for /[slug] | 90 min
**Owner:** Rutuja drafts → Hariom signs off Sat AM → dev implements

**Target page:** /[slug]
**Page type:** [homepage / product / comparison / use-case / pricing / blog post]
**Schema types to apply:** [pick from aio-geo-playbook.md §3 matrix]

**Output file:** /Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/docs/schema-specs/[slug]-[YYYY-MM-DD].json

[Full JSON-LD content following templates in aio-geo-playbook.md §3 + structured-data validator pass logged inline]
```

### Comparison page drafting (Friday Block 2)

```
#### Task T-FRI-2: Comparison Page — ProfileTap vs [X] | 75 min
**Owner:** Rutuja drafts → Pratima reviews Fri PM

**Competitor:** [Pratima picked Monday from aio-geo-playbook.md §7]
**Target keyword:** [ProfileTap vs X / X alternative India / etc.]
**India search volume:** [estimated]

**Page structure (per aio-geo-playbook.md §4):**
- TL;DR box at top (3 lines)
- H2 intro — what each tool does
- H2 comparison table (HTML <table>, not image) — feature, ProfileTap, [X], notes
- H2 India-specific differentiators
- H2 pricing comparison (INR vs USD)
- H2 who should pick which (5-6 use-case lines)
- H2 FAQ block (4-6 Qs — AI-citable)

**Output file:** /briefs/content-prep/[YYYY-MM-DD]-vs-[competitor]-comparison.md

[Full 1200-1800 words draft following the structure above, with comparison table populated]
```

### AI-citable content audit (Friday Block 3)

```
#### Task T-FRI-3: AI-Citable Audit for /[slug] | 75 min
**Owner:** Rutuja

**Target page:** /[slug]
**Checklist:** aio-geo-playbook.md §5 (12 points)

**Output file:** /briefs/content-prep/[YYYY-MM-DD]-[slug]-ai-audit.md

[List of 5 likely AI queries the page should answer + the answer-shaped paragraph for each. Hand to dev for content amendment.]
```

### Pinterest pins (Wednesday Block 1)

```
#### Task T-WED-1b: Pinterest Pins | 30 min within Block 1
**Owner:** Rutuja

**Pins to create:** 5
**Target boards:** ProfileTap-Identity, ProfileTap-NFC-Cards-India, ProfileTap-Travel-Safety, ProfileTap-Pet-ID, India-SaaS

**Per pin:**
- Vertical 1000×1500 image (use Canva ProfileTap template)
- Title: [SEO keyword + visual hook]
- Description (200-500 chars, India-keyword-rich): [paragraph mentioning use case + India context + 1 inline link]
- Destination URL: profiletap.io/[slug]
- Hashtags: 5-8 India + niche tags

**After publishing — log 5 pins in tracking spreadsheet (no individual tracker rows needed — counted in weekly_progress.csv pinterest_pins_published).**
```

### GitHub Awesome-list pitch (Friday Block 5)

```
#### Task T-FRI-5a: Awesome-list inclusion | 15 min per list, 3 lists
**Owner:** Rutuja

**Target lists:**
- awesome-saas or awesome-saas-india
- awesome-startups (India fork)
- awesome-business-tools / awesome-nfc / awesome-qr-tools

**Per list:**
1. Read CONTRIBUTING.md
2. Open issue OR PR (whichever the list maintainer prefers) with ProfileTap entry in the format the list uses
3. Description ≤120 chars, 1 link to profiletap.io

**After submitting — add new row to outreach_tracker.csv:**
- domain: github.com
- target_page_slug: /
- status: contacted
- first_contact_date: [today]
- next_follow_up_date: [today + 14 days]
- notes: Awesome-list pitch — [list name] — PR/issue URL: [link]
```

---

## Step 6 — Append to weekly_progress.csv

At the end of brief generation, append one new row to `/Users/hariomshah/Documents/GitHub/profiletap-seo-os/projects/profiletap/data/tracking/weekly_progress.csv` using this column order:

```
week_start_date,week_end_date,theme,focus_hub,owner_split_rutuja_h,owner_split_pratima_h,owner_split_hariom_h,follow_ups_due_planned,follow_ups_sent_actual,new_media_outreach_planned,new_media_outreach_sent_actual,media_responses_received,roundup_outreach_planned,roundup_outreach_sent_actual,roundup_inclusions_won,listicle_outreach_planned,listicle_outreach_sent_actual,listicle_inclusions_won,haro_pitches_planned,haro_pitches_sent_actual,haro_quoted_count,platform_articles_planned,platform_articles_published,hariom_linkedin_published,directory_listings_planned,directory_listings_completed,ai_directory_submissions_planned,ai_directory_submissions_completed,reddit_answers_planned,reddit_answers_posted,quora_answers_planned,quora_answers_posted,content_prep_pages_started,content_prep_pages_finalised,content_prep_pages_at_risk,da_research_count,da_threshold_holds_added,schema_pages_audited,schema_specs_signed_off_by_hariom,comparison_pages_drafted,wikipedia_sources_audited,github_awesome_list_pitches,pinterest_pins_published,pratima_decisions_made_count,pratima_decisions_pending_count,blockers,worked_well_notes,to_change_next_week,pratima_retro_verdict,founder_signoff_status,weekly_da_homepage_snapshot,weekly_organic_sessions_estimate,weekly_referral_sessions_estimate,total_won_status_added_to_tracker
```

Fill only the `planned` columns at generation time:
- week_start_date / week_end_date / theme / focus_hub: from Step 3
- owner_split_rutuja_h: 51
- owner_split_pratima_h: [calculated — sum of 9 Pratima task minutes / 60, max 4]
- owner_split_hariom_h: [calculated — sum of 3 Hariom task minutes / 60, max 1]
- *_planned columns: counts from Step 4 schedule
- pratima_decisions_made_count / pratima_decisions_pending_count: 0 (Rutuja updates Saturday)
- All `_actual`, retrospective text, and snapshot columns: leave blank — Rutuja and Pratima fill during the week
- founder_signoff_status: leave blank — Hariom fills Saturday

---

## Hard rules — enforce on every brief without exception

**Role rules:**
- Rutuja never sends new media outreach without Pratima's Monday approval
- Hariom never receives an execution task — only decisions, reviews, sign-offs, and the weekly founder LinkedIn publish
- Pratima total weekly time ≤4h — if generator schedules more, drop lowest-leverage Pratima task and note in carryover
- Hariom total weekly time ≤60 min — if generator schedules more, drop lowest-leverage Hariom task and note in carryover

**Volume rules:**
- Max 3 new media outreach emails per week (Thu only, reference-led format, fresh article required)
- Always 5 roundup + listicle inclusion emails per week (Tue 3, Thu 2 — high-response channel)
- Always 3 HARO/Featured/Qwoted pitches per week (Thu)
- Always 6 Reddit + 7 Quora answers per week (mandatory; exception = explicit "no relevant active threads exist for any current target page keyword this week" — must be stated)
- Always 1 Hashnode (Mon) + 1 LinkedIn (Wed, Hariom) + 1 Substack-or-Medium (Thu) = 3 articles/week
- Always 3 directory listings + 2 AI-tool directory submissions per week (Tue)
- Always 2 content prep pages end-to-end per week (Page A Mon-Wed, Page B Thu-Sat)
- Always 1 schema spec + 1 comparison page + 1 AI-citable audit per week (Fri)

**Quality rules:**
- All reporter-first publications (techcircle, livemint, economictimes, inc42, yourstory, entrackr, businessworld) require reference-led journalist-tip format — never expert-quote-with-block format
- All outreach emails ≤120 words; follow-ups ≤60 words; roundup-inclusion ≤90 words
- All outreach must include 1 India-specific detail (WhatsApp masking, INR pricing, QR-native UPI, Bharat market, Tier 2/3 SMB, WhatsApp B2B)
- Subject lines must reference real article/topic for target publication — never generic ("Introducing ProfileTap", "Smart identity platform for India" are banned)
- Anchor text matches backlink_targets.csv — no invented anchors
- Platform posts use profiletap.io
- All platform posts and answers open with reader's problem, not with ProfileTap's name
- Hashnode titles must match a real search query with measurable volume — not brand descriptions
- Full post + answer content written copy-paste-ready in the brief — never "[FILL IN]" placeholders
- If a task cannot be written because data is missing, flag the task as blocked with the specific missing data

**Tracker rules:**
- Platform posts live → status = won (not contacted)
- next_follow_up_date never blank for status ∈ {contacted, follow_up_1}
- follow_up_3 = final, mark next_follow_up_date as "final", no follow_up_4 ever
- Never outreach to "Page not live" domains or content_calendar status = planned pages
- DA <30 → hold outreach
- Every won row needs live_url within 24h or flagged in next tracker update

**Carryover rules:**
- Any Pratima decision unmade by Saturday → next week's Monday Block 1 of Pratima's section
- Any content prep page Day 3 not finalised by Saturday → next week's Mon-Wed for Page A or Thu-Sat for Page B
- Any media follow-up overdue >7 days twice → close as no_response automatically and note in retro
- Any channel with 0 responses for 2 consecutive weeks → reduce volume 50% next week and reallocate to a channel with >0 responses

**Claude-in-Chrome delegation rules:**
Every task in the brief whose type appears in the "CIC" rows of `docs/claude-in-chrome-companion.md` Task Delegation Map MUST include a `▶ Delegate to Claude-in-Chrome` sub-block under the main task. The sub-block contains the exact paste-ready prompt (from §"Per-task prompt library" of the companion doc), the data the parallel session needs (URLs, account names, profile content the Code session pre-fills), and the expected return Rutuja types back into this Code session to log it.

Eligible task types (always include the sub-block):
- Directory listings (Tuesday Block 1)
- AI-tool directory submissions (Tuesday Block 2)
- DA research (Monday Block 5)
- Reddit thread discovery — NOT answer posting (Mon Block 4 + Wed Block 3)
- Quora question discovery — NOT answer posting (Mon Block 4, Tue Block 5, Wed Block 2, Fri Block 5)
- Hashnode publishing (Monday Block 2)
- Substack/Medium publishing (Thursday Block 4)
- Pinterest pin creation (Wednesday Block 1)
- HARO/Featured/Qwoted inbox triage (Thursday Block 3 — triage only; Rutuja drafts answers)
- Listicle target discovery (Tuesday Block 3 — discovery only; Rutuja drafts emails)
- Fresh-article scan for reference-led media outreach (Thursday Block 1 — research only; Rutuja drafts emails; Pratima approves)
- Schema validation (Friday Block 1 — validation only; spec drafting is the Code session)
- Wikipedia source audit (Saturday Block 2)
- Monthly AI citation measurement (last Saturday of each month — added as Saturday Block 5 buffer task once per 4 weeks)

NEVER include a CIC sub-block for:
- Reddit / Quora answer posting (brand-account risk)
- Email sending from Gmail (personalisation + Pratima approval lives in Rutuja's drafts)
- LinkedIn cross-post / FB community posts (account-suspension risk)
- LinkedIn founder article publishing (Hariom only)
- Tracker CSV updates (Code session only)
- Content drafting of any kind (Code session only)
- Pratima or Hariom tasks (humans only)

---

## Slash command

This skill is invoked as `/profiletap-weekly-routine` from the project directory. It produces one weekly team-brief markdown file + appends one row to weekly_progress.csv. Run every Sunday evening or Monday morning before the team starts work.

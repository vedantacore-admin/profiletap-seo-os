# ProfileTap SEO Intern Brief — 2026-05-03 (Sunday)

## Today's Focus
Today is Sunday — DA research catch-up and tracking update day. All P1 and P2 domains already have DA scores recorded, so today's goal is to **verify those scores are current** before the week's outreach begins. Two data issues also need immediate fixing: entrackr.com has no contact email in outreach_tracker.csv, and exchange4media.com has an incomplete email entry (`@exchange4media.com`). Three blocks cover DA verification for 14 outreach-ready domains not yet in the tracker, DA verification for 12 domains already queued for outreach, and a 60-minute tracker cleanup.

> **Tool note for DA research:** Moz free tier allows 10 domain checks per day. Use Moz for the first 10 domains across Block 1, then switch to Ahrefs Free Webmaster Tools or SEMrush free tier for the remaining domains.

---

## Work Schedule (Total: 4 hours 20 minutes)

---

### Block 1 — 10:00 AM – 12:00 PM | 120 min
**DA Score Verification — Outreach-Ready Domains Not Yet in Tracker**

These 14 domains have target pages that are `draft_ready` and have not yet entered the outreach pipeline. Verifying their DA scores now confirms priority ranking ahead of this week's outreach rotation.

---

#### Task 1: DA Research — livemint.com, economictimes.com, producthunt.com | 20 min

**Objective:** Verify current DA scores for these three high-priority outreach targets whose target page (`/`) is draft-ready; update backlink_targets.csv if any score has changed.

**Domains to research:**
- livemint.com (recorded: DA 88)
- economictimes.com (recorded: DA 82)
- producthunt.com (recorded: DA 91)

**Tools:** Moz DA Checker (moz.com/domain-analysis, 10 free/day) → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv for each domain with the verified integer value. If livemint.com or economictimes.com has dropped below DA 70, flag to lead before scheduling Monday outreach.

---

#### Task 2: DA Research — g2.com, capterra.com, crunchbase.com | 20 min

**Objective:** Verify DA scores for these P1/P2 directory and review platforms ahead of profile submission and listing work this week.

**Domains to research:**
- g2.com (recorded: DA 91)
- capterra.com (recorded: DA 91)
- crunchbase.com (recorded: DA 91)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv. Any score below DA 85 for these platforms would be unusual — flag if so.

---

#### Task 3: DA Research — startupindia.gov.in, techcircle.in, saasworthy.com | 20 min

**Objective:** Verify DA scores for these three P1/P2 targets whose target page is `/business-identity` (status: draft_ready). Accurate scores confirm their priority ranking ahead of business hub outreach.

**Domains to research:**
- startupindia.gov.in (recorded: DA 68)
- techcircle.in (recorded: DA 74)
- saasworthy.com (recorded: DA 75)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv for each domain with the verified integer value.

---

#### Task 4: DA Research — traveltriangle.com, autocarindia.com, momjunction.com | 20 min

**Objective:** Verify DA scores for these P2 hub targets (travel, vehicle, family_safety) scheduled for Wednesday and Thursday outreach this week.

**Domains to research:**
- traveltriangle.com (recorded: DA 63)
- autocarindia.com (recorded: DA 73)
- momjunction.com (recorded: DA 74)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv. If traveltriangle.com has risen above DA 70, flag to lead — that would move it closer to Tier 1 priority.

---

#### Task 5: DA Research — petfed.org, dogexpress.in | 20 min

> ⚠️ **THRESHOLD FLAG:** Both petfed.org (recorded: DA 28) and dogexpress.in (recorded: DA 28) are **currently below the 30-DA minimum threshold** for outreach. Today's verification checks whether their scores have risen. Do NOT proceed with outreach to either domain until this is confirmed.

**Objective:** Re-verify current DA scores for both pet hub targets. If still at or below DA 28, document the finding and hold outreach — do not add to outreach_tracker until scores reach 30+.

**Domains to research:**
- petfed.org (recorded: DA 28 — **BELOW THRESHOLD**)
- dogexpress.in (recorded: DA 28 — **BELOW THRESHOLD**)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv with verified integer value. Then:
- If DA has risen to **30+**: outreach can proceed on Wednesday (pet hub day) — no action needed beyond updating the score
- If DA is **still below 30**: add to the notes column of backlink_targets.csv for each domain: `"DA below 30 threshold as of 2026-05-03 — hold outreach"` and flag to lead for a decision on whether to keep as prospects

---

#### Task 6: Update backlink_targets.csv — Consolidate Block 1 Changes | 20 min

**Objective:** Consolidate all DA score findings from Tasks 1–5 into backlink_targets.csv and ensure the file is clean.

**Instructions:**
1. Open backlink_targets.csv
2. For each of the 14 domains researched in Tasks 1–5, update the `da_score` column with the verified integer
3. For any domain where the score has moved **±5 points or more** from the recorded value, add a brief note in the `notes` column documenting the change (e.g., `"DA updated from 88 to 83 on 2026-05-03"`)
4. For petfed.org and dogexpress.in, add the threshold hold note (from Task 5 instructions) if scores are still below 30
5. Save the file

---

### Block 2 — 12:00 PM – 01:20 PM | 80 min
**DA Score Verification — Domains Already in Outreach Tracker**

These 12 domains are in outreach_tracker.csv with status `not_started` — they are scheduled to receive first-contact emails starting Monday. Verifying their DA scores now ensures the priority ranking is accurate before outreach begins.

---

#### Task 7: DA Research — yourstory.com, inc42.com, entrackr.com | 20 min

**Objective:** Verify current DA scores for three P1 startup media targets scheduled for Monday outreach.

**Domains to research:**
- yourstory.com (recorded: DA 85)
- inc42.com (recorded: DA 80)
- entrackr.com (recorded: DA 72)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv. **Note:** entrackr.com has no contact email in outreach_tracker.csv — this must be fixed in Task 11 before Monday outreach can proceed.

---

#### Task 8: DA Research — businessworld.in, entrepreneur.com, exchange4media.com | 20 min

**Objective:** Verify current DA scores for two business/entrepreneur media targets and one marketing media target.

**Domains to research:**
- businessworld.in (recorded: DA 81)
- entrepreneur.com (recorded: DA 91)
- exchange4media.com (recorded: DA 77)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv. **Note:** exchange4media.com has an incomplete contact email in outreach_tracker.csv (currently `@exchange4media.com`) — this must be fixed in Task 12 before Tuesday outreach.

---

#### Task 9: DA Research — socialsamosa.com, shoutmeloud.com, indianstartupnews.com | 20 min

**Objective:** Verify current DA scores for two marketing media targets and one startup news blog, all scheduled for Tuesday outreach.

**Domains to research:**
- socialsamosa.com (recorded: DA 72)
- shoutmeloud.com (recorded: DA 75)
- indianstartupnews.com (recorded: DA 59)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv.

---

#### Task 10: DA Research — vccircle.com, expresshealthcare.in, housing.com | 20 min

**Objective:** Verify current DA scores for one startup media target and two profession-specific media targets.

**Domains to research:**
- vccircle.com (recorded: DA 77)
- expresshealthcare.in (recorded: DA 71)
- housing.com (recorded: DA 77)

**Tools:** Moz DA Checker → Ahrefs Free Webmaster Tools → SEMrush free tier

**After completing:** Update da_score column in backlink_targets.csv.

---

### Block 3 — 01:20 PM – 02:20 PM | 60 min
**Tracking Update — Contact Research + Full Tracker Review**

---

#### Task 11: Contact Research — entrackr.com | 15 min

**Objective:** Find a valid editorial contact email for entrackr.com and update outreach_tracker.csv before Monday outreach.

**Current status in outreach_tracker.csv:** contact_email field is **blank**. Outreach cannot proceed until this is resolved.

**Instructions:**
1. Visit entrackr.com and look for a "Contact Us" or "About" page
2. Check their LinkedIn company page for editorial staff (search "entrackr editor" or "entrackr journalist")
3. Try standard editorial email formats: editor@entrackr.com, team@entrackr.com, news@entrackr.com, tips@entrackr.com
4. Update outreach_tracker.csv:
   - `contact_email`: best email found (or most likely format)
   - `contact_name`: specific name if found (otherwise keep "Editorial Team")
5. If no confirmed email found: update `notes` field for entrackr.com with `"No direct email found 2026-05-03 — attempt LinkedIn DM to editorial lead before outreach"`

---

#### Task 12: Contact Research — exchange4media.com | 15 min

**Objective:** Complete the partial contact email for exchange4media.com (currently `@exchange4media.com`) by finding a specific editor name.

**Current status in outreach_tracker.csv:** contact_email is `@exchange4media.com` — the first name is missing.

**Instructions:**
1. Visit the editorial team page at exchange4media.com/editorial-team.html (already noted in outreach_tracker)
2. Identify an editor covering digital media, startups, or tech — avoid the senior editor level for a first cold pitch
3. Construct the full email: `[firstname]@exchange4media.com`
4. Update outreach_tracker.csv:
   - `contact_email`: complete email (e.g., `priya@exchange4media.com`)
   - `contact_name`: specific editor's full name (e.g., "Priya Sharma")
5. Also note in backlink_targets.csv: exchange4media.com currently requires a "PR-quality pitch" per notes — confirm the editor you selected covers the right beat

---

#### Task 13: Tracking Update — outreach_tracker.csv Full Review | 30 min

**Objective:** Review all 12 entries in outreach_tracker.csv for data completeness and flag any other issues before this week's outreach begins.

**Rows needing attention:**

| Domain | Issue |
|---|---|
| entrackr.com | No contact_email — fix in Task 11 |
| exchange4media.com | Incomplete contact_email — fix in Task 12 |

**Review checklist for all 12 rows:**
1. Confirm the domain website is still active and publishing recent content (spot-check by visiting the site)
2. Confirm the contact email format looks valid (no obvious typos, correct domain)
3. Verify the notes column URL is accessible for each row that has one (businessworld.in LinkedIn, exchange4media.com editorial page, shoutmeloud.com, indianstartupnews.com, vccircle.com)
4. Confirm `contact_name` is not just "Editorial Team" where a specific editor is known — update if found during Tasks 11–12 research
5. All 12 rows should show `status = not_started` — this is correct since no outreach has been sent yet

**All rows in outreach_tracker (for reference):**

| Domain | Target Page | Contact Email | Status |
|---|---|---|---|
| yourstory.com | / | tips@yourstory.com | not_started |
| inc42.com | /digital-business-card-india | press@inc42.com | not_started |
| entrackr.com | /digital-business-card-india | **MISSING** | not_started |
| businessworld.in | /nfc-business-card-india | press@businessworld.in | not_started |
| entrepreneur.com | /nfc-business-card-india | support@entrepreneur.com | not_started |
| exchange4media.com | /digital-business-card-for-creators | **INCOMPLETE** | not_started |
| socialsamosa.com | /digital-business-card-for-creators | team@socialsamosa.com | not_started |
| shoutmeloud.com | /linktree-alternative-for-creators | Harsh@ShoutMeLoud.com | not_started |
| indianstartupnews.com | /hihello-alternative-india | team@indianstartupnews.com | not_started |
| vccircle.com | /popl-alternative-india | grievance@vccircle.com | not_started |
| expresshealthcare.in | /digital-business-card-for-doctors | editorial@expresshealthcare.in | not_started |
| housing.com | /digital-business-card-for-real-estate-agents | support@housing.com | not_started |

> **Note on vccircle.com:** The contact email listed is `grievance@vccircle.com` — this is a complaints address, not editorial. During the review, attempt to find a more appropriate editorial or press contact. Update if a better option is found.

---

## End-of-Day Checklist

- [ ] DA scores verified and updated in backlink_targets.csv for all 14 outreach-ready domains not yet in tracker (Tasks 1–5)
- [ ] Block 1 DA changes consolidated in backlink_targets.csv with notes for ±5-point moves (Task 6)
- [ ] DA scores verified and updated in backlink_targets.csv for all 12 outreach_tracker domains (Tasks 7–10)
- [ ] petfed.org and dogexpress.in: DA threshold status confirmed and documented (hold outreach note added if still below 30)
- [ ] entrackr.com: valid contact email found and added to outreach_tracker.csv (Task 11)
- [ ] exchange4media.com: complete contact email and editor name added to outreach_tracker.csv (Task 12)
- [ ] All 12 outreach_tracker entries reviewed — websites active, email formats valid, notes URLs accessible (Task 13)
- [ ] vccircle.com contact email reviewed and updated to editorial address if found

## Tomorrow's Preview

Monday is **business hub day** — first-contact outreach targets are P1 startup and business media: yourstory.com, inc42.com, businessworld.in (all in outreach_tracker as `not_started`, contact details confirmed). With entrackr.com's email resolved today (Task 11), all four business hub domains in the tracker will be ready — schedule the top three for Monday (max 3 outreach emails per day). Recommended Monday send order: **yourstory.com**, **inc42.com**, **businessworld.in**. Entrackr.com and economictimes.com can queue for Tuesday or next Monday depending on email availability.

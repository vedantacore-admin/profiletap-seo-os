# Claude-in-Chrome Companion Playbook

> **Purpose.** Maps the weekly routine's tasks to "Claude-in-Chrome can do this" vs "do it manually" vs "don't automate." Rutuja runs the weekly brief in this Claude Code session (which writes files, updates trackers, drafts content); a *separate* Claude Pro session with the Chrome extension installed executes the web-UI tasks in parallel. The two sessions don't talk to each other directly — Rutuja is the bridge.

---

## Setup (do this once)

1. **Install the Chrome extension** — "Claude for Chrome" (or whichever name Anthropic ships under). Sign in with the separate Pro plan.
2. **Pre-create accounts** before delegating directory tasks. Claude can fill forms but cannot do email verification on its own.
   - Email: a dedicated `seo@profiletap.io` or similar — keep credentials in 1Password / a team password manager Rutuja can access
   - Accounts to create up front: G2, Capterra, Crunchbase, SaaSHub, AlternativeTo, ProductHunt, About.me, BetaList, GetApp, SoftwareAdvice, TheresAnAIForThat, Futurepedia, Quora (founder profile), Reddit (1 account with 30+ days of non-promotional history — important), Medium, Hashnode, Substack, Pinterest Business, LinkedIn (Hariom's and Rutuja's personal), GitHub
3. **Pre-fill the standard description copy** in a single doc Rutuja keeps open in another tab:
   - Short description (≤200 chars)
   - Long description (400-600 chars)
   - Logo URL + product image URLs
   - Founder bio + photo URL
   - GSTIN + address + phone
   - All `sameAs` social URLs (LinkedIn, Twitter, Instagram, Facebook, Crunchbase)
4. **Verify the parallel Pro session can reach the Chrome extension** — open chrome://extensions and confirm it's enabled. The Pro session must be open in the *same Chrome profile* the team uses for ProfileTap accounts.
5. **2FA / CAPTCHA reality check** — Claude cannot solve CAPTCHAs and cannot read 2FA codes from a phone. Rutuja stays in the loop for those steps. The pattern is "Claude does the 95% of clicking and typing; Rutuja walks over for the 5% that needs a human."

---

## Task-by-task delegation map

For each weekly task type, this table says **who does what**. "CIC" = Claude-in-Chrome (the parallel Pro session). "Code" = this Claude Code session in the terminal. "Manual" = Rutuja clicks herself. "Don't automate" = explicit veto.

| Weekly task | Best executor | Why | Estimated time saved per task |
|---|---|---|---|
| Directory listing (G2, Capterra, etc.) | **CIC** (Rutuja monitors) | Multi-step form-fill, account-aware. Claude is 3-5x faster than manual. | 10-12 min per listing |
| AI-tool directory submission | **CIC** | Same as above. | 12-15 min per submission |
| DA research (Moz / Ahrefs / SEMrush free tools) | **CIC** | Open URL, copy score, repeat. Tedious for human, trivial for CIC. | 8-10 min per batch of 3 |
| Reddit thread discovery (search + filter) | **CIC** | Multi-query search, read thread comment counts, last activity dates. | 8 min per answer |
| Reddit answer posting | **Manual** (Rutuja) | The answer text matters and needs Rutuja's read. Posting from a CIC session risks the Reddit account getting flagged as bot-driven. | — |
| Quora question discovery (search + follower-count) | **CIC** | Same as Reddit. | 8 min per answer |
| Quora answer posting | **Manual** (Rutuja) | Brand voice + disclosure compliance. Worth Rutuja's eyes on each post. | — |
| Hashnode article publishing | **CIC** | Paste markdown, set title/tags, click publish. Article was already drafted + Pratima-approved. | 10 min per article |
| Substack/Medium article publishing | **CIC** | Same. | 10 min per article |
| LinkedIn founder article (Hariom) | **Don't automate** | Identity-sensitive. Must publish from Hariom's signed-in profile. Hariom does the final edit + publish himself. | — |
| LinkedIn cross-post / FB community posts | **Manual** (Rutuja) | Account-suspension risk. Manual is safer. | — |
| Pinterest pin creation | **CIC** | Upload image, paste title/description, set destination URL. Repetitive — good fit. | 5 min per pin |
| GitHub Awesome-list inclusion PR | **CIC** | Fork repo (CIC clicks Fork) → Rutuja opens locally and edits the markdown via Claude Code → CIC opens the PR. Hybrid. | 15 min per list |
| HARO/Featured/Qwoted inbox triage | **CIC** | Open inbox, scan queries, flag relevant ones. Rutuja drafts the answer. | 15 min per session |
| Listicle target discovery (Google: site: searches) | **CIC** | Run 5-10 site: searches, extract article URLs into a list. | 10 min per session |
| Fresh-article scan for reference-led media outreach | **CIC** | Open target publication, scan last 30 days for relevant article, return title + URL. | 5 min per target × 3 = 15 min |
| Outreach email send (Gmail) | **Don't automate** | Personalisation per email + Pratima approval lives in Rutuja's drafts folder. CIC sending email = brand-risk. | — |
| Tracker updates (outreach_tracker.csv, content_calendar.csv) | **Code** (this session) | Files in the repo. Claude Code writes them. | — |
| Content prep Day 1/2/3 outputs | **Code** (this session) | Markdown files in /briefs/content-prep/. Claude Code writes. | — |
| Schema JSON-LD spec drafting | **Code** | File output. Claude Code writes. | — |
| Schema validation (validator.schema.org, Google Rich Results Test) | **CIC** | Paste JSON, capture pass/fail, screenshot. | 5 min per spec |
| Monthly AI citation measurement (10 queries × 4 engines) | **CIC** | Open ChatGPT/Perplexity/Gemini/Copilot, run query, screenshot answer. 40 screenshots is the whole job. | 60+ min saved per month |
| Wikipedia source audit (find existing ProfileTap mentions) | **CIC** | Google search + open each result + extract title + date + publication. | 30 min per audit |

**Total weekly time saved if all CIC-eligible tasks are delegated:** ~6-9 hours/week. That's effectively a full day Rutuja can re-allocate to content prep depth or higher-leverage outreach drafting.

---

## How to delegate inside the weekly brief

The weekly routine generator will, going forward, append a **`▶ Delegate to Claude-in-Chrome`** sub-block under any task type from the "CIC" rows above. The sub-block contains:
1. The exact prompt Rutuja pastes into the parallel Pro session
2. The exact data CIC needs (URLs, account name, profile content)
3. The expected return — what Rutuja types back into the Claude Code session to log it

This keeps the two sessions decoupled. Rutuja is the only one who sees both.

Example (directory listing block):

```
### Task T-TUE-1: g2.com | Directory Listing | 25 min
Owner: Rutuja

▶ Delegate to Claude-in-Chrome:
"""
Open g2.com in a new tab. Search for 'ProfileTap'. If a profile exists, click 'Claim'.
If not, click 'Add a Product' and use the following profile content [paste from below].
Pause when you hit any 2FA / email verification step and ask me to handle it.
After the listing is live (or pending review), copy the URL and tell me.
"""

Profile content to give CIC:
[short description, long description, categories, pricing, image URL, sameAs URLs — all pre-filled by Code session]

Expected return to log here:
- Profile URL: __________
- Status: live / pending review
- Notes: __________

After CIC returns the URL → paste into outreach_tracker.csv row that the Code session pre-staged.
```

The Code session in the weekly routine populates the profile content and the tracker stub; CIC fills out the actual web UI; Rutuja paste-bridges between them.

---

## Per-task prompt library (paste-ready)

Each of these is a self-contained prompt Rutuja can drop into the parallel Claude-in-Chrome Pro session. They assume the Pro session has Chrome MCP tools loaded.

### 1. Directory listing (G2 / Capterra / Crunchbase / SaaSHub / AlternativeTo / about.me / BetaList / GetApp)

```
You have the Chrome MCP. I need you to add ProfileTap to {DIRECTORY_NAME} ({DIRECTORY_URL}).

Steps:
1. Navigate to {DIRECTORY_URL} and search for "ProfileTap". If a profile already exists, click Claim and stop — tell me which account email to use for the claim.
2. If no profile exists, find the "Add Product" / "Submit Tool" / "Add Listing" flow and start it.
3. Fill the form fields using the values below. If a field is required but not in my list, pause and ask me for the value. Never guess.
4. If you hit 2FA, CAPTCHA, or email verification, pause and tell me — I'll handle it.
5. When the listing is submitted (or live), copy the profile URL and the submission/listing ID. Tell me both.

Profile content:
- Company name: ProfileTap
- Website: https://profiletap.io
- Short description (≤200 chars): {SHORT_DESC}
- Long description (400-600 chars): {LONG_DESC}
- Categories to pick: {CATEGORIES}
- Pricing tier: Freemium — paid from ₹499
- Deployment: Cloud / SaaS / Web / Mobile
- Target market: Small Business, Mid-Market, India, Global
- HQ: Palghar, Maharashtra, India
- Founded: {FOUNDED_YEAR — confirm with Hariom}
- Founder: Hariom Shah
- Logo URL: {LOGO_URL}
- Product image URLs: {IMAGE_URLS}
- LinkedIn: {LINKEDIN_COMPANY_URL}
- Twitter: {TWITTER_URL}

Take a screenshot when you've submitted, and tell me the URL of the live or pending profile.
```

### 2. AI-tool directory submission (TheresAnAIForThat / Futurepedia / Toolify / etc.)

```
You have the Chrome MCP. Submit ProfileTap to {AI_DIRECTORY_NAME} ({SUBMIT_URL}).

Use the AI-tool angle — ProfileTap has AI review assist for SMBs (drafts business replies, requests reviews) and a Business AI feature set. The tool category is AI for Business / AI Customer Engagement / SaaS Productivity.

Steps:
1. Navigate to {SUBMIT_URL}.
2. Fill the form with values below.
3. If asked for a video URL or demo screenshot, pause and ask me.
4. Submit. Capture the listing URL (if live) or confirmation ID (if pending review).

Profile content: {paste the AI-tool block from aio-geo-playbook.md §6}

If they require an OG / preview image, use https://profiletap.io/og-image.png.

Return: the listing URL, the review-time estimate from the confirmation page, and any account ID/email you used to submit.
```

### 3. DA research (Moz / Ahrefs free tools)

```
You have the Chrome MCP. Look up the Domain Authority for these domains:
- {DOMAIN_1}
- {DOMAIN_2}
- {DOMAIN_3}

For each, in order:
1. Open https://moz.com/domain-analysis and paste the domain. Wait for the score. Copy the DA value as an integer.
2. If Moz daily quota is hit (10 free/day), switch to https://ahrefs.com/website-authority-checker.
3. If both are rate-limited, try https://www.semrush.com/analytics/overview/.
4. Record: domain, DA score, source tool, date.

Return a table:
| domain | da_score | source | date |

I'll paste it into our backlink_targets.csv.
```

### 4. Reddit thread discovery (search + filter)

```
You have the Chrome MCP. I need active Reddit threads matching one of these queries, where I can post a helpful answer that mentions ProfileTap.

Target keyword (must match my product page /{SLUG}): {KEYWORD}
Queries to try in this order:
1. "{QUERY_1}"
2. "{QUERY_2 — India variant}"
3. "{QUERY_3 — competitor angle}"

Priority subreddits: r/india, r/IndiaInvestments, r/startups, r/Entrepreneur, r/smallbusiness, r/SaaS.

For each query:
1. Search Reddit (https://www.reddit.com/search/?q=...)
2. Filter to "Past year" then sort by Top
3. Open the top 5 results
4. For each, capture: thread title, subreddit, age, upvote count, comment count, last comment date, URL
5. Skip threads where the subreddit rules forbid self-promotion (read the sidebar before recommending).

Return the top 3 threads across all queries ranked by traffic potential (upvotes × recent activity). I will write the answer myself and post manually — you don't post.
```

### 5. Quora question discovery

```
You have the Chrome MCP. Find Quora questions matching {KEYWORD} where the question has 500+ followers (Google-indexed traffic threshold).

Queries:
1. "{QUERY_1}"
2. "{QUERY_2 — India variant}"
3. "{QUERY_3 — competitor angle}"

For each result, capture: question title, follower count (visible on the question page), answer count, URL.

Return the top 3 across queries, sorted by follower count descending. I'll write the answer myself with the required disclosure line.
```

### 6. Hashnode publishing

```
You have the Chrome MCP. Publish the following article on Hashnode at {HASHNODE_ACCOUNT}.

Steps:
1. Navigate to hashnode.com/create (or the team blog's "New post").
2. Paste the title: {TITLE}
3. Paste the body (markdown):
---
{MARKDOWN_BODY}
---
4. Set tags: {TAG_1}, {TAG_2}, {TAG_3}
5. Set cover image if available: {COVER_IMAGE_URL}
6. Set canonical URL: leave blank (this is the original).
7. Hit Publish.
8. Confirm the live URL. Tell me.

Return the live article URL.
```

### 7. Substack / Medium publishing

```
You have the Chrome MCP. Publish on {PLATFORM} ({substack.com OR medium.com}) using {ACCOUNT}.

Steps:
1. Open the platform's new-post composer.
2. Title: {TITLE}
3. Body (markdown — Substack/Medium converts most of it):
---
{MARKDOWN_BODY}
---
4. Inline link: {ANCHOR_TEXT} → {PROFILETAP_URL}
5. Tags (Medium only): {TAGS}
6. Subtitle (Substack only): {SUBTITLE}
7. Hit Publish.

Return the live URL.
```

### 8. Pinterest pins

```
You have the Chrome MCP. Create 5 Pinterest pins on the ProfileTap business account.

Steps for each pin:
1. Open https://www.pinterest.com/pin-builder/
2. Upload image from URL: {IMAGE_URL_N}
3. Title: {TITLE_N}
4. Description: {DESCRIPTION_N} (200-500 chars)
5. Destination URL: {PROFILETAP_URL_N}
6. Board: {BOARD_N} (create if it doesn't exist)
7. Hashtags: {HASHTAGS_N}
8. Hit Publish.

Pin data follows — 5 pins total:
[5 numbered blocks with IMAGE_URL, TITLE, DESCRIPTION, PROFILETAP_URL, BOARD, HASHTAGS each]

Return the 5 live pin URLs.
```

### 9. HARO / Featured / Qwoted inbox triage

```
You have the Chrome MCP. Open my email inbox at {EMAIL_PROVIDER_URL}, filter to "HARO" / "Featured" / "Qwoted" / "SourceBottle" / "Help-a-B2B-Writer" senders for today.

For each query in the digests:
1. Read the journalist's request
2. Decide if ProfileTap can credibly answer (does it match: NFC business cards, India SaaS, identity tools, AI for SMB, founder-life, B2B in India, digital identity, family safety tech, pet tech, travel tech, vehicle tech, link-in-bio, multi-profile management)
3. Note the deadline, word count cap, requested format

Return a ranked list of 5 best-fit queries with: source platform, query title, journalist + publication, deadline, word count, requested format, suggested ProfileTap angle (one line).

I'll draft the actual answer myself.
```

### 10. Listicle target discovery

```
You have the Chrome MCP. Find roundup articles where ProfileTap could be included.

Run these Google searches:
1. site:medium.com "best NFC business card" India
2. site:medium.com "digital business card" India 2026
3. "top 10 NFC business cards" India
4. "best Linktree alternatives" India
5. "best digital business cards" India review
6. "ProfileTap alternative"
7. {custom search seeded to {SLUG_TOPIC}}

For each search, open top 10 results. For each result, capture:
- Article title
- Publication / blog name
- Publish date
- Author name (if visible)
- Author email or contact-page URL (look for "About" / "Contact")
- Which competitors are listed in the article
- Article URL

Return a table with the top 10 across all searches sorted by domain authority approximation (use https://moz.com/domain-analysis on the top 5 if quota allows).

I'll write the listicle-inclusion email and send myself.
```

### 11. Fresh-article scan for reference-led media outreach

```
You have the Chrome MCP. For each target publication below, find one article published in the last 30 days that touches one of these topics: digital identity, NFC, QR, business cards, Indian SaaS, founder stories, B2B in India, SMB digital adoption, WhatsApp business, family safety tech, pet tech, travel tech, vehicle tech.

Targets ({TODAY} - 30 days):
- {DOMAIN_1} (relevant beat: {BEAT_1})
- {DOMAIN_2} (relevant beat: {BEAT_2})
- {DOMAIN_3} (relevant beat: {BEAT_3})

For each domain:
1. Navigate to {DOMAIN}/category/{closest matching beat URL}
2. Filter to articles in the last 30 days
3. Open the top 3 relevant headlines
4. For each, capture: title, URL, publish date, author name, author email or Twitter (search the page for both)
5. Return the BEST match — the article most likely to make a reference-led journalist tip credible

Output for each target:
- Domain
- Article title + URL
- Publish date
- Author + contact

If no relevant article exists in the last 30 days for any target, flag that target as "skip this week — no fresh article."
```

### 12. Schema validation

```
You have the Chrome MCP. I have a JSON-LD spec to validate.

Steps:
1. Open https://validator.schema.org/
2. Paste this JSON into the "Code Snippet" tab:
---
{JSON_LD}
---
3. Click "Run test"
4. Capture: any errors, any warnings, the parsed @type list

Then:
5. Open https://search.google.com/test/rich-results
6. Switch to "Code" mode
7. Paste the same JSON
8. Run
9. Capture: any errors, the eligible rich-result types

Return both reports. I'll fix any errors and re-validate.
```

### 13. Monthly AI citation measurement

```
You have the Chrome MCP. Run our monthly AI citation check.

For each query below, run it in all four AI surfaces (ChatGPT search at chatgpt.com, Perplexity at perplexity.ai, Google Gemini at gemini.google.com, Microsoft Copilot at copilot.microsoft.com).

Queries:
1. best NFC business card India
2. digital business card India INR pricing
3. ProfileTap vs Blinq
4. alternative to Linktree India
5. WhatsApp masking business tool India
6. QR pet ID tag India
7. best digital business card for Indian professionals
8. NFC card with INR pricing
9. India NFC business card review
10. multi-profile digital identity India

For each query × engine combo:
1. Submit the query
2. Take a screenshot of the answer
3. Record: did ProfileTap appear by name? (yes/no), was profiletap.io cited? (yes/no), was the description accurate? (yes/no), what other tools were named?

Return a table:
| query | engine | profiletap_named | profiletap_cited | accurate | other_tools_named | screenshot_filename |

I'll save it to ai_citation_log.csv.
```

### 14. Wikipedia source audit

```
You have the Chrome MCP. Find every verifiable third-party mention of ProfileTap online.

Steps:
1. Run these searches:
   - "ProfileTap" site:medium.com
   - "ProfileTap" site:yourstory.com
   - "ProfileTap" site:inc42.com
   - "ProfileTap" (broader)
   - "profiletap.io"
   - "ProfileTap" -site:profiletap.io (to exclude our own pages)
2. For each result not on profiletap.io, capture:
   - URL
   - Publication name
   - Publish date
   - Type (news article / blog post / review / mention / interview / listicle)
   - Independence: did ProfileTap pay for or sponsor this? (best-guess yes/no based on disclosures)
3. Open https://en.wikipedia.org/wiki/Special:Search?search=ProfileTap — confirm no existing article (we don't want a duplicate-article speedy delete)
4. Open https://www.wikidata.org/wiki/Special:Search?search=ProfileTap — note if a Wikidata item exists

Return a table I can paste into /data/tracking/wikipedia_sources.csv:
| url | publication | pub_date | type | independence | notes |

Plus a yes/no on existing Wikipedia and Wikidata records.
```

---

## What NEVER to delegate to Claude-in-Chrome

- **LinkedIn founder article publishing** — Hariom only. Identity-sensitive.
- **Reddit answer posting** — manual. Brand-account risk from bot-pattern detection.
- **Quora answer posting** — manual. Brand-account risk + disclosure compliance.
- **Email sending from any inbox** — manual. Personalisation + Pratima approval pipeline must stay in Rutuja's drafts folder.
- **Tracker CSV updates** — Code session does these. CIC has no file-system access to the repo.
- **Content drafting (briefs, drafts, comparison pages, schema specs)** — Code session does these. Rutuja relies on Pratima's review in the repo, not in a browser tab.
- **Pratima's 9 decisions** — humans only. Pratima approves drafts in her email or in the repo, not via a Claude session.
- **Hariom's 3 founder tasks** — humans only.
- **Anything brand-voice-sensitive without an approved draft already in hand** — never let CIC generate publish-ready copy on the fly. The Code session writes; Pratima approves; CIC only posts the approved text.

---

## How this changes the weekly time budget

The current plan is Rutuja 51h, Pratima ≤4h, Hariom ≤60 min. With Claude-in-Chrome handling the 14 task types above:

- Rutuja's *active manual* time drops from 51h to ~42h
- The freed 8-9 hours go into: deeper content prep (Day 1 keyword briefs become more rigorous), more Reddit/Quora answer *quality* (more time per answer), and additional listicle target discovery
- Pratima and Hariom budgets unchanged — they're decision-only
- Rutuja must still supervise CIC sessions (~2h/week of monitoring) — net free time ~6-7h/week

**Decision for the next weekly brief:** the generator should append `▶ Delegate to Claude-in-Chrome` sub-blocks under every CIC-eligible task and shorten the manual time estimate for those blocks. Rutuja gets to choose per-task whether to delegate or do manually — but the prompt is ready either way.

---

## Maintenance

Add a new task type to this doc whenever the team discovers a new web-UI workflow (e.g., a new directory, a new AI surface, a new social channel). Pratima owns this doc alongside aio-geo-playbook.md. Rutuja proposes additions via the weekly retro `to_change_next_week` field.

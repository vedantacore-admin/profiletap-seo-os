# ProfileTap AIO + GEO Playbook

> **Purpose.** Reference doc for ProfileTap's AI Optimization (AIO) and Generative Engine Optimization (GEO) work. The weekly routine reads this every Friday for the schema audit, comparison page draft, and AI-citable content audit blocks. Update this doc whenever you discover a new AI surface, a new citation pattern, or a new directory worth submitting to.

---

## 1. What AIO and GEO mean for ProfileTap

**AIO (AI Optimization)** — optimising content so that AI assistant answer surfaces (ChatGPT search, Perplexity, Gemini, Microsoft Copilot, Claude search) cite ProfileTap by name when a relevant query is asked.

**GEO (Generative Engine Optimization)** — the broader practice of structuring a website and its off-site presence so that *any* generative engine, including ones that don't yet exist, has the signals it needs to (a) understand what ProfileTap is, (b) trust it as a source, (c) cite it accurately.

The two overlap. What we actually want: **when an Indian SMB owner asks ChatGPT or Perplexity "best NFC business card for Indian businesses" — ProfileTap is the first or second name in the answer, with profiletap.io as the citation URL.**

This is different from SEO. SEO wants the click. AIO/GEO wants the citation (and the click is the bonus). Pre-launch, citation share is the cheaper and more measurable lead-in metric.

---

## 2. How AI engines source citations

| Engine | Index source | Citation behaviour | What we optimise |
|---|---|---|---|
| **ChatGPT (Search)** | Bing index + OpenAI training corpus | Cites 3-6 URLs per answer; weights `.gov`, `.edu`, Wikipedia, Reddit, Quora heavily for trust | Bing-indexable pages, Reddit/Quora by-name mentions, Wikipedia presence |
| **Perplexity** | Hybrid (Bing + Google + own crawl) | Cites 4-8 URLs, surfaces minor sites if they're answer-shaped | Answer-shaped paragraphs, FAQ schema, clear definitions |
| **Gemini / Google AI Overview** | Google index | Cites 1-4 URLs from the SERP top 5-10 | Classic SEO + structured data + first-paragraph factual answers |
| **Microsoft Copilot** | Bing index | Same as ChatGPT roughly | Bing index hygiene; Bing Webmaster Tools setup |
| **Claude (claude.ai web search)** | Anthropic's web crawl | Cites 2-5 URLs, weighting depth and recency | Long-form, well-structured, dated content with sources |

**Key implications for ProfileTap:**
1. Submit profiletap.io to Bing Webmaster Tools (not just Google Search Console). Bing's index drives ChatGPT and Copilot — half the AI surface.
2. Wikipedia and Wikidata presence is disproportionately weighted. Targeting a Wikipedia article post-launch is high-leverage. Pre-launch: build the verifiable sources for it.
3. Reddit and Quora by-name mentions are training-corpus gold. Every Reddit/Quora answer the team posts that mentions ProfileTap by name is a future AI citation seed.
4. Structured data (schema.org JSON-LD) is heavily weighted across all engines. Adding it is one of the highest-ROI items in this whole playbook.

---

## 3. Schema markup priority per page type

Every Friday Block 1, Rutuja audits one priority page and produces a JSON-LD spec for Hariom's Saturday sign-off. This matrix says which schema types to apply per page.

| Page type | Schema types (required) | Schema types (nice to have) | Notes |
|---|---|---|---|
| Homepage | Organization, LocalBusiness | WebSite (with `potentialAction` SearchAction) | sameAs links to LinkedIn, Crunchbase, GitHub, Twitter, Instagram, AngelList. Founder named as `founder` property. |
| Product page (e.g. /in/nfc-metal-card) | Product, Offer | AggregateRating (once you have 5+ real reviews), Brand | Required: priceCurrency: INR, price, availability, image, description. |
| Comparison page (e.g. /profiletap-vs-blinq) | Article, ItemList | FAQPage (if FAQ block present), BreadcrumbList | ItemList captures the compared products. Article needs author, datePublished, dateModified. |
| Use-case page (e.g. /pet-id-profile) | Article, FAQPage | HowTo (if step-by-step content), BreadcrumbList | FAQPage on every use-case page is critical for AI citation. |
| Pricing page | Offer (one per plan), Product | Service | priceCurrency: INR. List unitText: "user/month" or "card". |
| Blog post | Article, BreadcrumbList | Person (author), FAQPage (if FAQ block) | Author must have `sameAs` to LinkedIn at minimum. Required: datePublished, dateModified. |
| Hub homepage (e.g. /in/teams) | CollectionPage, BreadcrumbList | ItemList of child pages | Helps AI engines understand site taxonomy. |

**Validator chain:**
1. Paste JSON-LD into schema.org validator: https://validator.schema.org/
2. Run page URL through Google Rich Results Test: https://search.google.com/test/rich-results
3. Run page URL through Bing URL Inspection in Bing Webmaster Tools
4. Generator helper: https://technicalseo.com/tools/schema-markup-generator/

### Minimal Organization + LocalBusiness JSON-LD template for homepage

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://profiletap.io/#organization",
      "name": "ProfileTap",
      "url": "https://profiletap.io",
      "logo": "https://profiletap.io/logo.png",
      "founder": [
        {
          "@type": "Person",
          "name": "Hariom Shah",
          "jobTitle": "Founder",
          "sameAs": [
            "https://www.linkedin.com/in/<hariom-linkedin-slug>"
          ]
        },
        {
          "@type": "Person",
          "name": "Pratima Hariom Shah",
          "jobTitle": "Co-Founder",
          "sameAs": [
            "https://www.linkedin.com/in/<pratima-linkedin-slug>"
          ]
        }
      ],
      "sameAs": [
        "https://www.linkedin.com/company/profiletap",
        "https://www.crunchbase.com/organization/profiletap",
        "https://twitter.com/profiletap_io",
        "https://www.instagram.com/profiletap.io"
      ],
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "customer support",
        "telephone": "+91-9220568922",
        "areaServed": "IN",
        "availableLanguage": ["en", "hi"]
      }
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://profiletap.io/#localbusiness",
      "name": "ProfileTap",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "506, Iris, Bafna Meadows, Mahim Road",
        "addressLocality": "Palghar (West)",
        "addressRegion": "Maharashtra",
        "postalCode": "401404",
        "addressCountry": "IN"
      },
      "telephone": "+91-9220568922",
      "url": "https://profiletap.io"
    }
  ]
}
```

### Minimal FAQPage JSON-LD template (for use-case pages)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is ProfileTap available in India with INR pricing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. ProfileTap is built India-first and offers INR pricing across all paid plans, starting at ₹499 for a PVC NFC card."
      }
    }
  ]
}
```

---

## 4. Answer-shaped content patterns

AI engines lift verbatim from answer-shaped paragraphs. These patterns increase the odds of being cited:

1. **Definition-first openings.** Every page's first paragraph should answer "What is [thing this page is about]?" in 1-2 sentences without marketing fluff.
   - Bad: "Welcome to ProfileTap, the future of identity!"
   - Good: "ProfileTap is an India-built NFC and QR identity platform that lets one user manage business, creator, family-safety, pet, travel, and vehicle profiles from a single account."
2. **FAQ blocks under H2s.** Each H2 followed by a Q-as-H3 and a 2-3 sentence A. Pair with FAQPage schema.
3. **Comparison tables in HTML `<table>`.** Not image, not flexbox, not divs styled as tables. Real `<table>` with `<th>` headers. AI engines extract rows.
4. **Step-by-step ordered lists** for any "how to" content. Wrap with HowTo schema where possible.
5. **TL;DR boxes** at the top of long-form articles. 3-5 lines summarising the answer. Often lifted verbatim into AI summaries.
6. **Statistic citations.** Every claim with a number gets a source link inline ("78% of Indian SMBs use WhatsApp as primary B2B channel — [Meta India SMB Report 2025](url)"). AI engines weight statistical content heavily but only if sourced.
7. **Date and version stamps.** "Last updated: May 2026" on every page. AI engines de-rank stale content.
8. **Entity-rich first paragraphs.** Mention ProfileTap, the core feature, India, the use case, and the primary competitor — all in the first 100 words. This wires the page into knowledge graphs.

---

## 5. AI-citable content audit checklist (12 points)

Applied to one priority page every Friday Block 3. Output saved to `/briefs/content-prep/[YYYY-MM-DD]-[slug]-ai-audit.md`. Hand to dev for content amendment.

For the chosen page, check:

1. [ ] First paragraph contains a definition-style "ProfileTap is X" answer
2. [ ] Target keyword appears in H1
3. [ ] At least 4 H2s with answer-shaped paragraphs underneath
4. [ ] At least 1 FAQ block with 4+ Q&A pairs (and FAQPage schema)
5. [ ] At least 1 comparison table (HTML, not image) if the page is informational or commercial
6. [ ] At least 3 statistics with sourced links
7. [ ] One India-specific detail per page (WhatsApp / UPI / INR / Bharat / Tier 2-3)
8. [ ] datePublished + dateModified visible to crawlers (both in body text and schema)
9. [ ] Author byline visible + Person schema with sameAs links
10. [ ] At least 2 internal links to related ProfileTap pages
11. [ ] At least 1 external citation to an authoritative source (gov.in, statista, IAMAI, Nasscom, etc.)
12. [ ] Page passes Google Rich Results Test with no critical errors

Each page lists 5 likely AI queries the page should answer, plus the answer-shaped paragraph that answers each.

---

## 6. AI tool directory submission list

Tuesday Block 2 hits 2 of these per week. Rotate through the list and mark completion in `outreach_tracker.csv`. Most review submissions within 1-14 days. Expected review time noted.

| Directory | URL | Submit URL | Review time | Notes |
|---|---|---|---|---|
| There's An AI For That | https://theresanaiforthat.com | /submit/ | 7-14 days | Highest-traffic AI directory. Pitch ProfileTap's AI review assist + business AI. |
| Futurepedia | https://www.futurepedia.io | /submit-tool | 3-7 days | Free + paid tiers. India SaaS often accepted on free tier. |
| AI Tools Club | https://aitoolsclub.com | /submit-ai-tool/ | 3-7 days | Lower barrier. India tools welcomed. |
| FutureTools | https://www.futuretools.io | /submit-a-tool | 14-30 days | Lower volume, but their newsletter has high CTR. |
| Toolify | https://www.toolify.ai | /submit | 7-14 days | High DA. Submission requires AI feature description. |
| AI Parabellum | https://aiparabellum.com | /submit-tool | 7-14 days | Indexes well. |
| Supertools (The Rundown) | https://supertools.therundown.ai | Email founder | 14-30 days | Curated. Pitch as "India's first multi-context identity AI tool". |
| AI Magic Tools | https://aimagictools.com | /submit | 3-14 days | Lower barrier. |
| AI Tools Directory | https://www.aitoolsdirectory.com | /submit | 7-14 days | Standard directory. |
| Easy With AI | https://easywithai.com | /submit | 7-14 days | Beginner-friendly framing helps. |
| SaaSHub | https://www.saashub.com | /submit-saas | 3-7 days | Not AI-only but covers AI tools. DA 65+. |
| AlternativeTo | https://alternativeto.net | Add Software | 14-30 days | Listed as alternative to Blinq, Linktree, HiHello. |
| TopAI Tools | https://topai.tools | /submit | 7-14 days | Submission free. |
| Insidr AI | https://www.insidr.ai/ai-tools | /submit-tool | 7-14 days | Curated. |

**Submission template (paste into every form):**

- Tool name: **ProfileTap**
- Tagline: India's multi-identity NFC + QR platform with AI review assist
- Website: https://profiletap.io
- Short description (≤200 chars): ProfileTap is an India-first NFC + QR identity platform with built-in AI review assist for SMBs. One account manages business, creator, pet, family-safety, travel and vehicle profiles.
- Long description (400-600 chars): ProfileTap combines NFC cards, QR sharing, and AI tools into a multi-context identity platform built India-first. Each user manages business profiles, creator pages, pet ID tags, family safety tags, travel luggage tags, and vehicle stickers from one account. India-specific features include INR pricing from ₹499, WhatsApp masking for B2B follow-up, call masking for privacy, and Bharat-market UX for Tier 2/3 SMB adoption. AI review assist helps SMB owners draft replies and request reviews automatically.
- Categories: AI for Business, AI Customer Engagement, SaaS, Digital Identity, NFC Tools, AI Productivity, India SaaS
- Pricing: Freemium — free tier; paid from ₹499
- Platforms: Web, iOS, Android

---

## 7. Comparison content backlog (Friday block — 1/week)

Pratima picks one from this list every Monday. Rutuja drafts Friday. 1200-1800 words, India-specific differentiator required, HTML comparison table required, FAQ block at the bottom.

| # | Title | Target keyword | India search vol (est.) | India differentiator angle |
|---|---|---|---|---|
| 1 | ProfileTap vs Blinq | "blinq alternative india" / "blinq vs profiletap" | 200-400 | INR pricing, WhatsApp masking, multi-context profiles vs single-purpose digital card |
| 2 | ProfileTap vs HiHello | "hihello alternative india" | 100-200 | Same — plus physical NFC card ecosystem |
| 3 | ProfileTap vs Popl | "popl alternative india" / "popl vs profiletap" | 150-300 | India shipping + INR pricing; Popl is US-centric |
| 4 | ProfileTap vs Mobilo | "mobilo alternative india" | 100-200 | Multi-profile vs single-profile; India-first pricing |
| 5 | ProfileTap vs V1CE | "v1ce alternative india" / "v1ce vs profiletap" | 100-200 | Multi-context use cases (V1CE is business-only) |
| 6 | ProfileTap vs Beaconstac | "beaconstac alternative india" | 100-200 | Beaconstac is enterprise/QR-only; ProfileTap covers individual + SMB |
| 7 | ProfileTap vs Linktree | "linktree alternative india" / "best linktree alternative" | 1000-2500 | NFC + identity layer, not just link-in-bio; INR pricing |
| 8 | ProfileTap vs dot. | "dot card alternative india" | 50-150 | India shipping; multi-profile vs single-profile |

**Optional next batch (after 8 weeks):** ProfileTap vs Switchit, vs Tapt, vs CamCard, vs Linktree Pro, vs Carrd.

Each comparison page should also link to /[hub]-hub from the comparison's body — internal linking is critical for hub authority.

---

## 8. Wikipedia / Wikidata strategy

**Notability criteria (Wikipedia):**
- 3+ verifiable secondary sources covering ProfileTap independently (a press release does not count)
- Sustained coverage over time (≥3 months)
- Independent editorial coverage (not affiliate or sponsored)

**Pre-launch action (every Saturday Block 2):**
Maintain a running list of verifiable sources at `/projects/profiletap/data/tracking/wikipedia_sources.csv` (create on first Saturday). Columns: url, publication, pub_date, type (interview / news / review / mention), independence (yes/no), notes.

The goal pre-launch is to build the source list, not submit. Submitting too early gets the article speedy-deleted with the page-creator account flagged.

**Wikidata is easier:**
- Wikidata accepts entries with looser notability requirements
- Create a Wikidata item for ProfileTap as soon as Crunchbase profile is live (Crunchbase counts as an external identifier)
- Required claims: P31 (instance of: business), P159 (HQ location: Palghar), P571 (inception date), P856 (official website), P112 (founded by: Hariom Shah)
- Wikidata items show up in Google Knowledge Panel and AI engine entity lookups — high leverage

**When to submit Wikipedia (post-launch):** After the first 3 independent press hits + funding announcement (if any) + 6+ months of operation. Hariom signs off.

---

## 9. Reddit and Quora as AI training corpus

Why this matters: every major LLM has been trained on Reddit + Quora dumps. Mentions by name in high-upvote/follower threads end up in future model weights *and* in real-time retrieval indexes.

**Tactics:**
- Always mention "ProfileTap" by name in the answer body, not just as a link
- Pair the name with the core differentiator phrase ("ProfileTap — the India-built multi-identity NFC platform")
- Use the same anchor phrasing across posts ("India's NFC business card platform", "multi-context digital identity") — repetition builds entity weight
- Prioritise threads with 500+ followers on Quora and 50+ upvotes on Reddit — these get indexed and retrieved more often
- Never use multiple Reddit accounts to seed by-name mentions — the brand-safety risk outweighs the SEO benefit. One account, real participation, real value, real link.

**Cap (carried forward from daily routine):** Max 1 ProfileTap link in Reddit comments per day. No cap on by-name mentions without a link.

---

## 10. Founder presence and E-E-A-T

AI engines (especially Google's, but increasingly all) weight Experience-Expertise-Authoritativeness-Trustworthiness signals. ProfileTap's site is light on these. Required additions:

### Founder bio pages (Hariom + Pratima)

- `/about/hariom-shah` with: full bio, photo, role, prior experience, expertise topics, LinkedIn link, Twitter/X link, GitHub link (if any), email
- `/about/pratima-shah` with: same structure
- Both pages get Person schema with `sameAs` array

### Author bylines on blog posts

Every blog post needs:
- Author name in the byline
- Author bio (1-2 lines) at the top or bottom
- Author photo
- Link to the author's `/about/` page
- Author wrapped in `Person` schema with `sameAs` to LinkedIn

### Expertise topics page

`/about/expertise` listing the topics each founder is qualified to speak on (helps with HARO matching and AI source verification). E.g.:
- Hariom Shah — NFC technology, India SaaS, founder operations, identity platforms, QR commerce
- Pratima Shah — Content strategy for Indian SMBs, B2B SEO for SaaS, multi-language content, India digital identity

### Contact transparency

Already on the site (GSTIN, address, WhatsApp). Add:
- Company registered name
- CIN (Corporate Identification Number)
- Founders' direct LinkedIn URLs in the footer
- Founded date

### sameAs links from Organization schema

Every external profile that ProfileTap claims (Crunchbase, AngelList, LinkedIn, Twitter, Instagram, YouTube, Quora company page, GitHub, ProductHunt, etc.) goes into the Organization schema's `sameAs` array. This is the single highest-leverage entity-graph signal.

---

## 11. Structured data validators (Friday Block 1 quick reference)

1. **schema.org validator:** https://validator.schema.org/ — fastest, catches syntax errors
2. **Google Rich Results Test:** https://search.google.com/test/rich-results — checks Google rich-result eligibility
3. **Bing URL Inspection:** Bing Webmaster Tools → URL Inspection — confirms Bing has indexed the JSON-LD (drives ChatGPT + Copilot)
4. **Schema Markup Generator:** https://technicalseo.com/tools/schema-markup-generator/ — starter templates
5. **JSON-LD Playground:** https://json-ld.org/playground/ — manual debug

Every Friday's JSON-LD spec must pass validators 1 and 2 before it goes to Hariom for sign-off.

---

## 12. Measuring AI citation share

Pre-launch the team should not over-invest in instrumentation, but a monthly manual check is worth the 15 minutes:

**Monthly query set** (run in ChatGPT search, Perplexity, Gemini, Copilot — paste each query, screenshot the answer):

1. "best NFC business card India"
2. "digital business card India INR pricing"
3. "ProfileTap vs Blinq"
4. "alternative to Linktree India"
5. "WhatsApp masking business tool India"
6. "QR pet ID tag India"
7. "best digital business card for Indian professionals"
8. "NFC card with INR pricing"
9. "India NFC business card review"
10. "multi-profile digital identity India"

For each query, record:
- Did ProfileTap appear in the answer? (yes/no)
- Did profiletap.io appear as a cited source URL? (yes/no)
- Was the description accurate? (yes/no)
- What other tools were named?
- Date and engine

Save the log to `/projects/profiletap/data/tracking/ai_citation_log.csv` (created when this measurement starts — out of scope for the initial weekly routine rollout). Run monthly. Tie growth in citation share to the weekly Hashnode + Substack + Medium + Reddit/Quora cadence to see what's actually moving the needle.

---

## Maintenance

This playbook is a living doc. Update whenever:
- A new AI surface becomes meaningful (e.g. new search-enabled chat tool)
- A new AI directory worth submitting to is discovered
- A new schema.org type is recommended for our page mix
- A new competitor is added to the comparison backlog
- The query set above stops representing real Indian buyer queries

Pratima owns this doc. Rutuja proposes edits via the weekly retro `to_change_next_week` field.

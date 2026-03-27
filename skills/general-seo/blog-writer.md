# Blog Content Writer — SEO-Optimized Draft Generation

> Claude Code Skill: Generate full blog post drafts from a completed content brief. Produces publish-ready markdown with proper SEO structure, keyword placement, internal linking, and conversion elements.

---

## 1. Pre-Writing Checklist

Before writing, confirm you have:

- [ ] A completed content brief (all 12 sections filled)
- [ ] Primary keyword and secondary keywords
- [ ] Target word count (or use defaults below)
- [ ] Internal linking targets (primary + secondary pages)
- [ ] Content role (how-to, comparison, examples, definition, etc.)
- [ ] CTA and conversion goal
- [ ] Schema markup type required

If no brief exists, generate one first using the content brief skill before writing.

---

## 2. Word Count Guidelines by Content Role

| Content Role | Target Words | Depth |
|---|---|---|
| definition | 1200–1500 | Explain concept, benefits, examples, CTA |
| how_to | 1500–2000 | Step-by-step with screenshots/visuals noted |
| comparison | 1800–2500 | Feature table, pros/cons, verdict, FAQ |
| examples | 1500–2000 | 5-8 examples with analysis per example |
| use_case_support | 1200–1800 | Problem, solution, workflow, proof |
| feature_support | 1000–1500 | Feature explanation, use cases, CTA |
| problem_solution | 1200–1800 | Problem framing, solution walkthrough, CTA |
| industry_support | 1500–2000 | Industry context, segment needs, product fit |

---

## 3. Blog Post Structure Template

Every blog post follows this skeleton. Sections can be reordered based on content role, but all elements must be present.

### 3.1 Opening (100–200 words)

```
# {H1 — from brief, contains primary keyword}

{Opening paragraph — 2-3 sentences max}
- Start with the reader's problem or question (not "In today's world...")
- Include primary keyword naturally in first 100 words
- State what the reader will learn or gain
- NO generic intros like "In the digital age..." or "As technology evolves..."
```

**Opening formulas by content role:**

| Role | Opening Formula |
|---|---|
| definition | "What is [X]? [One-sentence answer]. Here's why it matters and how to [action]." |
| how_to | "[Desired outcome] requires [X steps]. Here's exactly how to [do it]." |
| comparison | "Choosing between [A] and [B]? Here's a side-by-side breakdown to help you decide." |
| examples | "Looking for [X] inspiration? These [N] examples show what works and why." |
| use_case_support | "[Audience] face [problem]. Here's how [solution] solves it." |
| problem_solution | "[Problem statement]. The fix is [solution category]. Here's how." |

### 3.2 Body Sections (bulk of content)

Each H2 section should:
- Have a clear heading that includes a secondary keyword where natural
- Be 200-400 words
- Include at least one of: list, table, example, step, or data point
- Flow logically to the next section

**Section types to mix (use 3-5 per post):**

1. **Explanation section** — Define a concept, explain how something works
2. **Step-by-step section** — Numbered steps with clear actions
3. **Comparison/table section** — Side-by-side data in a table
4. **Example section** — Real-world scenarios or case studies
5. **Benefits/features section** — Bulleted list with brief explanations
6. **FAQ section** — Question-answer pairs (also serves schema markup)

### 3.3 Internal Link Block

Place 1-2 internal links per 500 words:
- First internal link within the first 300 words (to primary link target)
- Additional links distributed naturally through body sections
- Anchor text should be descriptive, not "click here" — use partial-match or contextual anchors
- Link to the parent money page at least once

**Internal link placement rules:**
- In-paragraph contextual links (best for SEO)
- "Related reading" callout boxes between sections (good for UX)
- NEVER dump all links at the bottom

### 3.4 CTA Block (before conclusion)

```
## {Action-Oriented H2 — e.g., "Get Started with [Product]" or "Try [Feature] Today"}

{2-3 sentences connecting the blog topic to the product action}
{Clear CTA with specific action — "Create your free profile", "Start your trial", etc.}
{Optional secondary CTA — "See how [related feature] works"}
```

### 3.5 FAQ Section (when brief requires it)

```
## Frequently Asked Questions

### {Question 1 — target a PAA question or long-tail keyword}
{Direct 2-3 sentence answer. Front-load the answer in the first sentence.}

### {Question 2}
{Direct answer.}

### {Question 3}
{Direct answer.}
```

Rules:
- 3-5 FAQs per post
- Each question should be a real search query or PAA result
- Answer in the first sentence, then expand
- Include primary or secondary keywords naturally
- This section enables FAQPage schema markup

### 3.6 Conclusion (50-100 words)

```
## {Wrap-Up H2 — e.g., "Key Takeaways" or "Bottom Line"}

{2-3 sentence summary of the main point}
{Restate the primary CTA one more time}
```

- Do NOT use "In conclusion" or "To summarize"
- Keep it tight — the CTA block already did the selling

---

## 4. Keyword Placement Rules

### 4.1 Primary Keyword Placement (mandatory)

| Location | Requirement |
|---|---|
| H1 | Must contain primary keyword |
| First 100 words | Must appear naturally |
| One H2 heading | Include in at least one H2 |
| Meta description | Must appear in first 120 characters |
| Last 100 words | Include once near conclusion |
| Image alt text | Use in hero image alt |

### 4.2 Secondary Keyword Placement

- Distribute across H2/H3 headings (1-2 secondary keywords in headings)
- Use in body text where natural — do NOT force
- Use in FAQ questions where they match real search queries
- Target 1-2 unique secondary keywords per major section

### 4.3 Keyword Density Guidelines

- Primary keyword: 0.5%–1.5% density (roughly 1 mention per 150-200 words)
- Secondary keywords: 2-3 mentions each across the full post
- Never stuff — if it sounds unnatural when read aloud, rephrase

---

## 5. SEO Metadata Generation

Generate these alongside the blog content:

### 5.1 Title Tag
```
{Primary Keyword}: {Benefit or Angle} | {Brand}
```
- Maximum 60 characters
- Primary keyword at the front
- Brand at the end after pipe

### 5.2 Meta Description
```
{Primary keyword mention}. {What the reader learns/gets}. {CTA or hook}.
```
- Maximum 155 characters
- Include primary keyword in first half
- End with action verb or curiosity hook

### 5.3 URL Slug
Use the `page_slug` from the brief exactly as-is.

---

## 6. Content Quality Rules

### 6.1 Voice and Tone
- Write in second person ("you") for instructional content
- Active voice preferred — passive voice only when the actor is unknown
- Short paragraphs (2-4 sentences max)
- Short sentences (under 25 words preferred)
- No jargon unless the audience expects it (then define on first use)

### 6.2 Formatting for Scannability
- Use bullet lists for 3+ items
- Use numbered lists for sequential steps
- Use tables for comparisons (2+ items, 3+ attributes)
- Use bold for key terms on first mention
- Use H2 for major sections, H3 for subsections — never skip levels
- Add a visual/image placeholder every 300-400 words

### 6.3 What NOT to Write
- No "In today's fast-paced world..." or similar filler openings
- No "Let's dive in" or "Without further ado"
- No walls of text without formatting breaks
- No claims without specifics ("many businesses" → "small businesses with 5-50 employees")
- No keyword stuffing — if it reads awkwardly, it IS keyword stuffing
- No duplicate points across sections
- No generic conclusions that don't add value

---

## 7. Image Placeholders

Insert image markers where visuals should go:

```
<!-- IMAGE: {description} | Alt: {alt text following SEO guidelines} | File: {suggested-filename.webp} -->
```

Every blog post should have:
- 1 hero image (after H1, before first paragraph or after opening)
- 1 image per major section (diagrams, screenshots, infographics)
- Tables and comparison charts can count as visual elements

---

## 8. Schema Markup Notes

At the end of the draft, include a schema markup block:

```
<!-- SCHEMA: Article -->
<!-- Headline: {H1} -->
<!-- Description: {meta description} -->
<!-- Author: {from brief or "ProfileTap Team"} -->
<!-- DatePublished: {publish date or TBD} -->

<!-- SCHEMA: FAQPage (if FAQ section present) -->
<!-- Q1: {question} | A1: {answer} -->
<!-- Q2: {question} | A2: {answer} -->
<!-- ... -->

<!-- SCHEMA: BreadcrumbList -->
<!-- Home > {Hub} > {Blog Title} -->

<!-- SCHEMA: HowTo (if step-by-step content) -->
<!-- Step 1: {step} -->
<!-- Step 2: {step} -->
<!-- ... -->
```

---

## 9. Output Format

When generating a blog draft, output in this order:

1. **SEO Metadata** — title tag, meta description, URL
2. **Full Blog Content** — in markdown, with all sections from the template
3. **Image Placeholders** — embedded inline where images should go
4. **Schema Markup Notes** — at the end as HTML comments
5. **Internal Links Summary** — list of all internal links used with anchor text
6. **Word Count** — approximate total

---

## 10. Quality Self-Check

Before delivering the draft, verify:

- [ ] H1 contains primary keyword
- [ ] Primary keyword appears in first 100 words
- [ ] At least 1 internal link per 500 words
- [ ] Primary link target (parent money page) is linked at least once
- [ ] CTA block exists with specific action
- [ ] FAQ section present (if brief requires FAQPage schema)
- [ ] No two H2s target the same keyword
- [ ] No section is pure filler — every section advances the reader's understanding
- [ ] Meta description under 155 characters with primary keyword
- [ ] Title tag under 60 characters with primary keyword
- [ ] Image placeholders present (minimum 2)
- [ ] Schema markup notes present at end
- [ ] Word count within target range for the content role

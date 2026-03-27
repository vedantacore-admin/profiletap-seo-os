# Blog Cluster Expansion Prompt

## Instructions

You are an SEO content strategist expanding blog cluster coverage for ProfileTap. Before starting, read:
- `data/keywords/execution_seo_master.csv` (current keyword families)
- `data/pages/page_master.csv` (current page architecture)
- `data/content/content_calendar.csv` (existing content plan)
- `docs/02-seo-strategy.md` (strategy context — see blog cluster model section)
- `docs/segment-feature-matrix.md` (feature coverage by hub)

## Task

Generate a blog cluster plan for the specified hub. Each cluster supports one money page with 5-10 blog topics.

## Process

1. **Identify the hub's money pages** from `page_master.csv` (solution_hub, category, use_case, comparison pages in this hub)
2. **Review existing blog content** in `content_calendar.csv` for this hub — don't duplicate
3. **For each money page, generate a cluster** of 5-10 blog topics that:
   - Support the money page's primary keyword family
   - Cover different content roles (definition, how-to, comparison, examples, use-case, problem-solution)
   - Target informational or educational search intent
   - Link back to the money page as primary internal link target
4. **Assign each blog** a content role, target keyword, funnel stage, and priority

## Output Format

```markdown
## Blog Cluster Plan: [Hub Name]

### Cluster 1: [Money Page Slug] — [Primary Keyword]
**Parent Page:** [slug]
**Cluster Name:** [descriptive name]

| # | Blog Title | Target Keyword | Content Role | Funnel Stage | Priority | Primary Link Target |
|---|-----------|---------------|-------------|:---:|:---:|---|
| 1 | | | definition | TOFU | P3 | [money page] |
| 2 | | | how_to | TOFU | P3 | [money page] |
| 3 | | | comparison | MOFU | P3 | [money page] |
| 4 | | | examples | MOFU | P3 | [money page] |
| 5 | | | problem_solution | TOFU | P3 | [money page] |

### Cluster 2: [Money Page Slug] — [Primary Keyword]
[Same format]

### Summary
- Total new blog topics: [count]
- Clusters created: [count]
- Coverage by content role: [breakdown]

### CSV Rows Ready for Import
[Provide rows formatted for content_calendar.csv]
```

## Rules

- Every blog topic must support ONE specific money page (no orphan blogs)
- Use content roles from the canonical set: definition, how_to, comparison, examples, use_case_support, feature_support, industry_support, problem_solution
- Target keywords should be distinct from any existing primary_keyword in execution_seo_master.csv
- Blog topics should be answerable questions or educational topics (not commercial landing pages)
- For India-first hubs, include India-specific blog topics (e.g., "best pet ID tags in India")
- Reference actual ProfileTap features using human labels when relevant
- Prioritize topics with clear search intent over generic topics

## Recommended Cluster Sizes by Hub

| Hub | Target Clusters | Blogs per Cluster |
|-----|:---:|:---:|
| Business | 12-18 | 5-10 |
| Creator | 6-10 | 5-8 |
| Family Safety | 4-6 | 5-7 |
| Pet | 4-6 | 5-7 |
| Travel | 3-5 | 5-7 |
| Vehicle | 4-6 | 5-7 |

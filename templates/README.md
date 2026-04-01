# New Project Template

Use this folder as the starting point for any new SEO OS project.

## Setup Steps

1. **Copy this folder** to `projects/<your-project-name>/`
2. **Fill in `CLAUDE.md`** — replace all `[PLACEHOLDER]` values with project-specific details:
   - `[PROJECT_NAME]` — the brand or client name
   - Feature tokens table — define the product's features
   - Hubs/segments table — define the content architecture
   - Operating rules — add any project-specific constraints
3. **Populate the empty CSVs** in `data/` — or run keyword research first and import
4. **Create project skills** in `skills/` — copy the profiletap skills as a reference pattern
5. **Open Claude Code from your new project directory** to activate both CLAUDE.md files

## What's Included

| Path | Contents |
|------|---------|
| `CLAUDE.md` | Project CLAUDE.md template with placeholders |
| `data/*/` | Header-only CSVs — correct schemas, no data |
| `briefs/templates/page-brief-template.md` | Standard 9-section brief template |
| `docs/` | Generic technical SEO, distribution, and image SEO docs |
| `sop/` | Standard operating procedures (page mapping, content review, etc.) |
| `prompts/` | Claude prompt templates for briefs, competitor analysis, blog clusters, schema |

## Reference

See `projects/profiletap/` for a fully populated example of a live project.

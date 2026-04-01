# SEO OS

## What This Is

A central SEO operating system reusable across any project or client. Generic skills live at root. Each project lives in its own folder under `projects/`.

## Operating Principle

**Always open Claude Code from the project directory**, not the repo root:
```
projects/<project-name>/
```
This auto-loads both this file (generic skills and navigation) and the project-specific CLAUDE.md (data schemas, features, hubs, workflows, project slash commands).

## Projects

| Project | Folder | Status |
|---------|--------|--------|
| ProfileTap | `projects/profiletap/` | Active |

## Starting a New Project

1. Copy `templates/` → `projects/<new-project-name>/`
2. Fill in `projects/<new-project-name>/CLAUDE.md` — replace all `[PLACEHOLDER]` values
3. Open Claude Code from `projects/<new-project-name>/`

See `templates/README.md` for the full setup checklist.

## File Map

```
skills/
  general-seo/          # 11 reusable SEO skills (available to all projects)

templates/              # Starter kit — copy this to create a new project
  CLAUDE.md             # Project CLAUDE.md template with placeholders
  README.md             # Setup guide
  briefs/templates/     # Generic page brief template
  data/                 # 8 empty CSVs with correct headers
  docs/                 # Generic technical SEO, distribution, image SEO docs
  sop/                  # Standard operating procedures
  prompts/              # Claude prompt templates

projects/
  profiletap/           # ProfileTap project (see projects/profiletap/CLAUDE.md)
```

## Generic Skills (Slash Commands — available to all projects)

- `/keyword-research` — Keyword research methodology
- `/content-optimization` — On-page SEO optimization
- `/technical-seo-audit` — Technical SEO audit
- `/backlink-strategy` — Link building strategy
- `/serp-analysis` — SERP analysis
- `/content-cluster-planning` — Topic cluster design
- `/local-seo` — Local SEO strategy
- `/rank-tracking-analytics` — Measurement and analytics
- `/content-refresh-strategy` — Content refresh methodology
- `/programmatic-seo` — Programmatic SEO
- `/blog-writer` — Full blog draft generation from briefs

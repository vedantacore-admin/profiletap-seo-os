# SEO OS

A central SEO operating system for managing keyword → page → content → backlink pipelines across multiple projects and clients.

## How It Works

Generic SEO methodology lives at root. Each project gets its own folder with its own data, content, strategy docs, and project-specific Claude skills.

```
keyword → page → content → backlink
```

## Repository Structure

```
skills/general-seo/     # 11 reusable SEO skills (shared across all projects)
templates/              # Starter kit — copy to create a new project
projects/               # One subfolder per project or client
  profiletap/           # Live example: ProfileTap smart identity platform
```

## Starting a New Project

```bash
cp -r templates/ projects/<your-project-name>/
```

Then open Claude Code from `projects/<your-project-name>/` and fill in the CLAUDE.md placeholders.

See `templates/README.md` for the full setup checklist.

## Working on an Existing Project

Open Claude Code from the **project directory**, not the repo root:

```bash
# Example
cd projects/profiletap/
```

This auto-loads both the root CLAUDE.md (generic skills) and the project CLAUDE.md (project-specific rules, data schemas, workflows, slash commands).

## Generic SEO Skills

Available to all projects via slash commands:

| Command | Purpose |
|---------|---------|
| `/keyword-research` | Keyword research methodology |
| `/content-optimization` | On-page SEO optimization |
| `/technical-seo-audit` | Technical SEO audit |
| `/backlink-strategy` | Link building strategy |
| `/serp-analysis` | SERP analysis |
| `/content-cluster-planning` | Topic cluster design |
| `/local-seo` | Local SEO strategy |
| `/rank-tracking-analytics` | Measurement and analytics |
| `/content-refresh-strategy` | Content refresh methodology |
| `/programmatic-seo` | Programmatic SEO |
| `/blog-writer` | Full blog draft generation |

## Projects

| Project | Folder | Description |
|---------|--------|-------------|
| ProfileTap | `projects/profiletap/` | Smart identity management platform — India-first SEO |

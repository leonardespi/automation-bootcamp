# QA Automation Bootcamp — Jekyll Site

This repository was generated from a static site and organized into a Jekyll site
with a `modules` collection.

## Local Development

```bash
bundle install
bundle exec jekyll serve
# open http://127.0.0.1:4000
```

## Structure

- `_modules/` — each module page (generated from your Markdown files)
- `_layouts/` — `default.html` (base), `module.html` (module pages)
- `_includes/` — `head.html`, `header.html`, `footer.html`
- `assets/` — `css/`, `js/`, `img/` (other files land under `assets/legacy/`)
- `pages/` — standalone pages (Modules index, About)
- `index.md` — Home page with a dynamic listing of modules
- `_config.yml` — site settings and collections
- `Gemfile` — Ruby gems for Jekyll

Monochrome, monospace, responsive design.

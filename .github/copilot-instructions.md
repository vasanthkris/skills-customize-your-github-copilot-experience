# Project Description

This project is an educational website for sharing homework assignments and coding exercises with students. Students can browse, view, and download assignments directly from the portal.

The site is a static, config-driven frontend for Mergington High School's Computer Science course. [README.md](../README.md) contains the exercise introduction; this file captures the implementation conventions agents need when changing the site.

## Project Structure

- [assignments/](../assignments/) stores one assignment per kebab-case folder, normally with `README.md` and optional starter files.
- [templates/assignment-template.md](../templates/assignment-template.md) is the starting structure for new assignment instructions.
- [assets/css/styles.css](../assets/css/styles.css) contains shared styles for both pages.
- [assets/js/script.js](../assets/js/script.js) loads [config.json](../config.json), renders the homepage, and calculates due-date status.
- [assets/pages/assignment.html](../assets/pages/assignment.html) is the detail-page shell; [assets/js/assignment.js](../assets/js/assignment.js) loads the selected README and attachment links.
- [index.html](../index.html) is the homepage entry point.

## Data And Content Conventions

- Register every assignment in [config.json](../config.json) with matching `id`, `path`, and attachment filenames on disk.
- Keep assignment content in `assignments/<id>/README.md`; use the `Objective` and `Tasks` sections from the template.
- Keep downloadable files beside the README and list them under the assignment's `attachments` array.
- Preserve the existing relative paths: the homepage fetches `config.json`, while the detail page fetches `../../config.json` and `../../assignments/<id>/README.md`.
- Treat config values and repository Markdown as trusted content because the current renderer inserts them with `innerHTML`; do not add user-controlled input without introducing escaping.

## Project Guidelines

- Maintain consistent styling across all pages
- Keep file and folder names descriptive and organized
- Prefer the existing vanilla HTML, CSS, and JavaScript structure; do not add a framework or build step for a small content change.
- When changing the data model, update both rendering scripts if the field is used on the homepage and detail page.

## Validation

- There is no package manager, build script, or automated test suite.
- Serve the repository over HTTP when testing because browser `fetch()` calls do not work reliably from `file://` URLs: `python3 -m http.server 8000`.
- Check that `config.json` remains valid JSON and that every configured assignment path and attachment exists.
- Manually test the homepage and a detail URL such as `assets/pages/assignment.html?id=python-basics` after changing paths or rendering logic.

## Educational Standards

When generating content for this project:

- **Learning-focused**: All content should be designed with clear learning objectives and appropriate difficulty levels
- **Student-friendly**: Use clear, encouraging language that motivates students
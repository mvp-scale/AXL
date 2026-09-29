# Design Language Lab

An interactive workspace for unpacking design vocabulary into concrete interface changes.

## Run

Open `index.html` in a browser. No installation, build step, API key, or backend is required.

For local HTTP hosting: `python -m http.server 8080`, then open http://localhost:8080.

## Use

- Browse by language or source.
- Select a complete branch or an individual prescription.
- Compare the fixed baseline against your recipe.
- Explore Overview, Projects, Project editor, and Settings.
- Exercise normal, loading, empty, error, and success states.
- Export selected prescriptions and example CSS.

The Northstar workspace uses simulated data and local interactions. Creating a project does not save it to a backend. Selections and edits are held in memory and reset on reload.

The catalog contains compiled guidance, source paraphrases, and lab decompositions. It is not a universal industry standard. Live CSS examples illustrate effects; implementation and process rules remain contextual instructions. See ATTRIBUTION.md and individual source links.

## GitHub Pages

Publish the repository root from your `main` branch under Settings → Pages. The site is static and needs no build pipeline.

## Files

- `index.html`: complete application, catalog, styles, and demo workspace.
- `favicon.svg`: site icon.
- `ATTRIBUTION.md`: provenance and research references.

Choose an appropriate license before inviting reuse. Third-party guidance remains attributed to its sources.

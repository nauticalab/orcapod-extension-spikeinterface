# Claude Code instructions for orcapod-extension-spikeinterface

## Running commands

Always run Python commands via `uv run`, e.g.:

```
uv run pytest tests/
uv run python -c "..."
```

Never use `python`, `pytest`, or `python3` directly.

## Superpowers artifacts

Place all superpowers-related artifacts (design specs, plans, etc.) in the `superpowers/`
directory at the project root.

- Specs go in `superpowers/specs/`
- Plans go in `superpowers/plans/`

## Docstrings

Use [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
Python docstrings everywhere. Never mix in ReST markup.

## Git commits

Always use [Conventional Commits](https://www.conventionalcommits.org/) style:

```
<type>(<optional scope>): <short description>
```

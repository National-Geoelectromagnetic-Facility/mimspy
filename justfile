set shell := ["bash", "-uc"]
set positional-arguments

# List all available recipes
@help:
  just --list

# Create a git repo if not exists, install dependencies and pre-commit hooks
@init: ensure-git install


# Install necessary dependencies and pre-commit hooks
@install:
  #!/bin/bash
  set -euxo pipefail
  {{just_executable()}} needs uv
  echo "Installing dependencies..."
  uv sync

  echo "Blocking the .venv directory from uploading to the cloud..."
  cloud-blocker .venv

  echo "Installing pre-commit hooks..."
  uv run pre-commit install --install-hooks

# Update the lockfile (e.g. after manually editing `pyproject.toml`)
@lock:
  uv lock

# Update dependencies and update pre-commit hooks
@update-hooks:
  echo "Updating pre-commit hooks..."
  uv run pre-commit install-hooks
  uv run pre-commit autoupdate

# Upate the ui file
@update-ui:
  uv run python pyside6-uic src/mimspy/ui/main.ui -o src/mimspy/ui/main.py

# Run the app
@app:
  uv run python src/app.py

# Format code with black and isort
@fmt:
  uv run ruff format -- src tests
  uv run ruff check --select=I001 --fix src tests

# Lint the project with Ruff
@lint:
  uv run ruff check --fix -- src tests

# Perform static type checking with mypy
@typecheck:
  uv run mypy -- src tests

# Perform static type checking with pyright
@pyright:
  uv run pyright

# Run all tests
@test:
  uv run pytest --cov=src/ --cov-report=term-missing --cov-report=html --disable-warnings

# Audit dependencies with pip-audit
@audit:
  uv run pip-audit
  uv run deptry -- src tests

# Run pre-commit checks
@pre-commit:
  uv run pre-commit run

# Commit with conventional commits
@commit:
  uv run cz commit

alias c := commit

# Push changes to the remote repository
# TODO: add typecheck back after testing
@push: fmt lint
  git push
  sleep 5
  just check-ci

# Run all CI checks
# TODO: add typecheck back after testing
@ci: fmt lint audit

# Check the CI status
@check-ci:
  @echo "Checking CI status..."
  # Get the latest run ID for ci.yml on main
  RUN_ID=$(gh run list --workflow ci.yml --branch main --limit 1 --json databaseId --jq ".[0].databaseId") \
  && echo "Watching run ID $RUN_ID..." \
  && gh run watch $RUN_ID

# Check the version can be bumped without errors
@check-bump:
  uv run cz bump --dry-run

# Run all pre-release checks
@pre-release: fmt lint audit check-bump

# Bump the version
@bump: check-bump
  uv run cz bump

# Release a new version
# TODO: add typecheck back after testing
@release: fmt audit lint bump push
  git push --tag
  sleep 5
  just check-release

# Check the release status
@check-release:
  @echo "Checking release status..."
  # Get the latest run ID for ci.yml on main
  RUN_ID=$(gh run list --workflow release.yml --branch main --limit 1 --json databaseId --jq ".[0].databaseId") \
  && echo "Watching run ID $RUN_ID..." \
  && gh run watch $RUN_ID

# Generate the spec file
@spec:
  uv run python scripts/pyinstaller.py -s

# Assemble the app
@assemble:
  uv run python scripts/pyinstaller.py -a

# Assemble file into a dmg
@dmg:
  uv run python scripts/pyinstaller.py -d

# Generate the release change log
# TODO: must be tied to a version number
@release-log:
    uv run cz changelog 0.2.0 --file-name release.md

# Set default version of the documentation
@set-default-docs-version:
  uv run mike set-default latest

# Serve documentation locally
serve-doc:
  uv run mkdocs serve --config-file=docs/mkdocs.yml

# Live preview the documentation as it would be on production
preview-docs:
  uv run mike serve --config-file=docs/mkdocs.yml

# Check whether the commit messages follow the conventional commit format
check-commits:
  #! /usr/bin/env zsh
  set -euo pipefail

  local revs
  revs=($(git rev-list origin/main..HEAD))

  if [[ $#revs -eq 0 ]]; then
    echo "No commits to check."
    exit 0
  else
    uv run cz check --rev-range origin/main..HEAD
  fi

# Clean the build files
clean:
    rm -rf build
    rm -rf dist

# Assert a command is available
[private]
needs *commands:
  #!/bin/bash
  set -euxo pipefail
  for cmd in "$@"; do
    if ! command -v $cmd &> /dev/null; then
      echo "$cmd binary not found. Did you forget to install it?"
      exit 1
    fi
  done

# Create a local git repo if not in one
[private]
@ensure-git:
  #!/bin/bash
  set -euxo pipefail
  just needs git
  if ! git rev-parse --is-inside-work-tree &> /dev/null; then
    git init
  fi

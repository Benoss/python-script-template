# Python Script Project Template 

This repository provides an opinionated Python project template for creating consistent, production-ready scripts with modern tooling. The template uses UV for dependency management, Ruff for linting/formatting, Ty for type checking, and Task for task automation.

## What This Template Provides

When you use this template via Copier, you'll be prompted for:
- **Project name**: Human-readable project name
- **Project slug (dashes)**: Used for package naming (e.g., `my-project`)
- **Project slug (underscores)**: Used for Python module naming (e.g., `my_project`)

The template generates a complete project structure with:
- Pre-configured `pyproject.toml` with Ruff and Ty settings
- Task automation via `Taskfile.yml` (build, lint, run commands)
- VS Code settings configured for Ty language server integration
- Git repository initialization
- Directory structure for outputs, fixtures, and tests
- Environment variable management with `.env` support
- **pip blocking mechanism** to enforce UV usage (prevents accidental `pip` usage)

**Platform Support**: Linux, Mac, and WSL only (bash scripts used for pip blocking)

## Setup to use this repo the first time

### Install go-task as a Task Runner
https://taskfile.dev/docs/installation

For Ubuntu: 
```bash
curl -1sLf 'https://dl.cloudsmith.io/public/task/task/setup.deb.sh' | sudo -E bash
apt install task
```

### Install UV this will be used to manage python version and virtualenv instead of pip

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### Copy the script to current folder

**Note**: The path below is an example. Replace `/home/benoit/tmp/python-script-template/` with the actual path to this template repository, or use a GitHub URL if hosted (e.g., `gh:username/python-script-template`).

```bash
uvx copier copy /home/benoit/tmp/python-script-template/ ai-stuff

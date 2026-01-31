# Python Project Template (Script & Django)

This repository provides an opinionated Python project template for creating consistent, production-ready projects with modern tooling. The template uses UV for dependency management, Ruff for linting/formatting, Ty for type checking, and Task for task automation.

## Supported Project Types

The template supports two project types:
1. **Script** - Standalone Python scripts for data processing, automation, or CLI tools
2. **Django** - Full-featured Django web applications with PostgreSQL, Tailwind CSS, and django-cotton

## What This Template Provides

When you use this template via Copier, you'll be prompted for:
- **Project name**: Human-readable project name
- **Project slug (dashes)**: Used for package naming (e.g., `my-project`)
- **Project slug (underscores)**: Used for Python module naming (e.g., `my_project`)
- **Project type**: Choose between `script` or `django`

### Script Projects Include:
- Pre-configured `pyproject.toml` with Ruff and Ty settings
- Task automation via `Taskfile.yml` (build, lint, run commands)
- VS Code settings configured for Ty language server integration
- Directory structure for outputs, fixtures, and tests
- Environment variable management with `.env` support
- **pip blocking mechanism** to enforce UV usage

### Django Projects Include:
- Django 5.0+ with structured settings (local/staging/prod)
- Apps organized in `apps/` directory
- PostgreSQL database via Podman/Docker Compose
- **Tailwind CSS 4.1** with CSS-based configuration
- **bunx** for running Tailwind (no Node.js dependency needed)
- django-cotton for component-based templates
- pytest-django for testing
- Management command for seeding data (`init_data`)
- Pre-configured admin panel
- Complete VS Code configuration for Django development

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

### Install Podman (for Django projects only)

If you plan to create Django projects, you'll need Podman for PostgreSQL:

```bash
# Ubuntu/Debian
sudo apt install podman podman-compose

# Fedora
sudo dnf install podman podman-compose

# macOS
brew install podman podman-compose
```

### Install Bun (for Django projects only)

Django projects use Tailwind CSS 4.1 via bunx (no Node.js needed):

```bash
# Linux/macOS/WSL
curl -fsSL https://bun.sh/install | bash
```


### Copy the script to current folder

**Note**: The path below is an example. Replace `/home/benoit/tmp/python-script-template/` with the actual path to this template repository, or use a GitHub URL if hosted (e.g., `gh:username/python-script-template`).

#### Create a Script Project

```bash
uvx copier copy /home/benoit/tmp/python-script-template/ my-script-project
# Choose 'script' when prompted for project type
cd my-script-project
task init
```

#### Create a Django Project

```bash
uvx copier copy /home/benoit/tmp/python-script-template/ my-django-app
# Choose 'django' when prompted for project type
cd my-django-app
task setup
task db-up
task migrate
task init-data
task tailwind-watch  # In one terminal (uses bunx)
task runserver       # In another terminal
# Access at http://localhost:8000
```

## Features by Project Type

### Script Projects

- **Minimal dependencies**: loguru for logging, python-dotenv for environment variables
- **Testing**: pytest with fixtures for CSV/JSON processing
- **Output**: Files saved to `tmp/` directory
- **Fixtures**: Sample data in `fixtures/` directory
- **Quick iteration**: Run with `task run`

### Django Projects

- **Structured settings**: Split by environment (local/staging/prod)
- **Apps organization**: All apps in `{{ project_slug }}/apps/` directory
- **PostgreSQL**: Running in Podman for local development
- **Modern frontend**: Tailwind CSS 4.1 via bunx (no Node.js needed) + django-cotton components
- **Seeding**: `init_data` management command creates test users
- **Admin ready**: Pre-configured admin panel at `/admin/`
- **Testing**: pytest-django with fixtures for users and authentication
- **API support**: Documentation recommends Django Ninja (not included by default)

## Common Development Tasks

### Script Projects

```bash
task setup      # Install dependencies
task lint       # Run linting and formatting
task test       # Run tests
task run        # Execute the main script
```

### Django Projects

```bash
task setup          # Install dependencies
task db-up          # Start database
task migrate        # Apply migrations
task init-data      # Seed test data
task runserver      # Start dev server
task shell          # Django shell
task test           # Run tests
task tailwind-watch # Watch Tailwind CSS
```

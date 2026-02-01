# Copilot Instructions for Template Development

## Overview

This repository is a **Copier template** that generates modern Python projects. It supports two project types:

1. **Script projects** - Python automation scripts with clean structure and modern tooling
2. **Django projects** - Full-featured web applications with PostgreSQL, Tailwind CSS 4.1, and django-cotton

**Template Engine**: [Copier](https://copier.readthedocs.io/) - A library for rendering project templates with Jinja2.

**Key Point**: You are working **ON the template itself**, not on a generated project. Files here define what gets created when users run `copier copy` to generate new projects.

## General Tone

- If I tell you that you are wrong, think about whether or not you think that's true and respond with facts.
- Avoid apologizing or making conciliatory statements.
- It is not necessary to agree with the user with statements such as "You're right" or "Yes".
- Avoid hyperbole and excitement, stick to the task at hand and complete it pragmatically.
- Avoid words like seamless, captivating

## Template Structure

```
.
├── AGENTS.md                 # This file - instructions for template development
├── copier.yml                # Template configuration and variables
├── LICENSE                   # Template license
├── readme.md                 # Repository documentation
├── Taskfile.yml              # Test automation for template validation
└── template/                 # All files that get copied to generated projects
    ├── AGENTS.md.jinja       # Agent instructions for generated projects
    ├── main_*.py.jinja       # Script entry point (conditional)
    ├── manage.py.jinja       # Django management (conditional)
    ├── pyproject.toml.jinja  # Dependencies and tool configuration
    ├── Taskfile.yml.jinja    # Task automation with go-task
    └── {{ project_slug_underscore }}/  # Django project directory (conditional)
```

**Important Distinctions**:
- **Root level**: Template repository configuration and documentation
- **template/ directory**: Files that get copied and rendered to generated projects
- **Conditional files**: Some files only appear in script or django projects (controlled by `copier.yml`)

## Jinja2 Templating Conventions

All files in the `template/` directory that need variable substitution or logic use the `.jinja` extension.

### File Naming Patterns

1. **Static extensions**: `filename.ext.jinja`
   - Source: `pyproject.toml.jinja`
   - Generated: `pyproject.toml`

2. **Dynamic filenames**: `prefix_{{ variable }}.ext.jinja`
   - Source: `main_{{ project_slug_underscore }}.py.jinja`
   - Generated: `main_myproject.py` (if `project_slug_underscore = "myproject"`)

3. **Dynamic directories**: `{{ variable }}/`
   - Source: `{{ project_slug_underscore }}/apps/core/`
   - Generated: `myproject/apps/core/` (if `project_slug_underscore = "myproject"`)

### Variable Interpolation

Use `{{ variable_name }}` to insert copier variables into generated files:

```jinja
name = "{{ project_name }}"
version = "0.1.0"
authors = [
    { name = "{{ author_name }}", email = "{{ author_email }}" }
]
```

### Conditional Blocks

Use `{% if %}` blocks to include/exclude code based on project type:

```jinja
{% if project_type == "django" %}
dependencies = [
    "django>=5.0",
]
{% elif project_type == "script" %}
dependencies = [
    "typer>=0.12",
]
{% endif %}
```

**Critical Rule**: When editing template files, preserve Jinja2 syntax exactly. Test that variables and conditionals work for both `script` and `django` project types.

### Escaping Jinja2 in Generated Files

When generated projects need Django templates with `{% %}` syntax, escape them:

```jinja
{% raw %}{% load static %}{% endraw %}
{% raw %}{% block content %}{% endraw %}
Content here
{% raw %}{% endblock %}{% endraw %}
```

## Copier Variables

Variables are defined in `copier.yml` and used throughout template files.

### Available Variables

| Variable | Type | Purpose | Example |
|----------|------|---------|---------|
| `project_name` | str | Human-readable name | "My Awesome Project" |
| `project_slug_dashes` | str | Kebab-case for directories/packages | "my-awesome-project" |
| `project_slug_underscore` | str | Snake_case for Python modules | "my_awesome_project" |
| `project_type` | str | "script" or "django" | "django" |
| `author_name` | str | Developer name | "Jane Doe" |
| `author_email` | str | Developer email | "jane@example.com" |

### Variable Usage Guidelines

1. **project_name**: Use in documentation, README headers, and display text
   ```jinja
   # {{ project_name }}
   ```

2. **project_slug_dashes**: Use for package names in `pyproject.toml`
   ```jinja
   name = "{{ project_slug_dashes }}"
   ```

3. **project_slug_underscore**: Use for Python module names, directories, imports
   ```jinja
   from {{ project_slug_underscore }}.apps.core import views
   ```

4. **project_type**: Use for conditional file inclusion and code blocks
   ```jinja
   {% if project_type == "django" %}
   [tool.django]
   {% endif %}
   ```

### Conditional File Exclusion

Files are conditionally excluded in `copier.yml` using `_exclude`:

```yaml
_exclude:
  - "{{ 'manage.py' if project_type == 'script' else '' }}"
  - "{{ 'main_' + project_slug_underscore + '.py' if project_type == 'django' else '' }}"
```

**Important**: Exclusions reference **output filenames**, not `.jinja` source names.

When adding new conditional files:
1. Create the `.jinja` file in `template/`
2. Add exclusion rule to `copier.yml` `_exclude` list
3. Test generation for both project types

## Code Standards for Template Files

**All Python code in template files must follow the same standards documented in `template/AGENTS.md.jinja`.**

The generated `AGENTS.md` contains comprehensive standards that also apply to this template repository:

### Core Standards (from template/AGENTS.md.jinja)

- ✅ **Type hints everywhere**: All functions must have return type annotations
- ✅ **Pathlib over open()**: Use `Path.read_text()`, `Path.write_text()` instead of `open()`
- ✅ **Loguru for logging**: Use `logger.info()`, never `print()` or standard `logging`
- ✅ **Ruff + Ty**: Linting with Ruff, type checking with Ty (not Pylance)
- ✅ **pytest patterns**: Use fixtures with type hints and docstrings
- ✅ **Max 5 parameters**: Use dataclass/pydantic if more parameters needed
- ✅ **UV exclusively**: Package manager (pip is blocked in generated projects)
- ✅ **Imperative docstrings**: First line in imperative mood ("Return the result", not "Returns the result")

### Django-Specific Standards (from template/AGENTS.md.jinja)

- ✅ **Apps in `apps/` directory**: All Django apps in `{{ project_slug_underscore }}/apps/`
- ✅ **Settings split**: base.py, local.py, staging.py, prod.py
- ✅ **Update init_data command**: Always add seed data when creating new models
- ✅ **URL namespacing**: Use `app_name = 'core'` in url.py files
- ✅ **Tailwind CSS 4.1**: CSS-based config via `@theme` in input.css (no tailwind.config.js)
- ✅ **django-cotton**: Use for reusable components in `templates/components/`
- ✅ **Django Ninja over DRF**: Prefer for APIs (but don't install by default)

**Reference Point**: See [`template/AGENTS.md.jinja`](template/AGENTS.md.jinja) for the complete standards that apply to both template development and generated projects.

## Template Development Best Practices

### 1. Keep Jinja2 Logic Minimal

- Prefer simple conditionals and variable substitution
- Avoid complex Jinja2 expressions in templates
- Use copier.yml for complex variable derivations

**Good**:
```jinja
{% if project_type == "django" %}
django>=5.0
{% endif %}
```

**Avoid**:
```jinja
{% if project_type == "django" and something_else and another_condition %}
```

### 2. Test Both Project Types

After making changes to template files, test generation for both types using the repository's Taskfile:

```bash
# Test script project generation (generates, runs task init, runs task lint)
task test-script

# Test Django project generation (generates, runs task init, runs task lint)
task test-django

# Test both project types
task test-all

# Clean up test projects
task clean
```

**Manual testing** (if needed):
```bash
# Test script project generation
copier copy . /tmp/test-script-project -d project_type=script -d project_name="Test Script"

# Test django project generation  
copier copy . /tmp/test-django-project -d project_type=django -d project_name="Test Django"

# Verify generated projects follow standards
cd /tmp/test-script-project && task lint
cd /tmp/test-django-project && task lint && task test
```

### 3. Maintain Consistency

- Keep script and django variants consistent where they share features
- If a standard changes, update both the template code and `template/AGENTS.md.jinja`
- Ensure fixture files in `template/fixtures/` serve as useful examples

### 4. Version Constraints

- Pin major versions for critical dependencies (Django, pytest, ruff)
- Use `>=` for flexibility within major versions
- Document breaking changes in readme.md

### 5. File Exclusions

When adding files that should only appear in one project type:

1. Create the file with `.jinja` extension: `newfile.py.jinja`
2. Add conditional exclusion to `copier.yml`:
   ```yaml
   _exclude:
     - "{{ 'newfile.py' if project_type == 'script' else '' }}"
   ```
3. Ensure excluded files don't break the other project type

## Testing Template Changes

### Automated Testing Workflow (Recommended)

The repository includes a `Taskfile.yml` that automates testing template generation:

```bash
# Test both project types (recommended after template changes)
task test-all

# Or test individually
task test-script   # Generate script project, run init & lint
task test-django   # Generate Django project, run init & lint

# Clean up test projects
task clean
```

**What the test tasks do**:
1. Generate a fresh project in `/tmp/copier-test/`
2. Run `task init` to install dependencies and set up environment
3. Run `task lint` to verify code quality (Ruff + Ty)
4. Report any linting errors

**Important**: If `task lint` reports errors in generated projects, those fixes must be ported back to the template files in `template/` directory.

### Manual Testing Workflow

For more control or debugging:

1. **Make changes** to template files
2. **Test generation**: 
   ```bash
   copier copy . /tmp/test-project
   ```
3. **Verify standards**:
   ```bash
   cd /tmp/test-project
   task init  # Install dependencies
   task lint  # Run Ruff + Ty
   task test  # Run pytest
   ```
4. **Test both types**: Repeat for `project_type=script` and `project_type=django`

### Common Issues to Check

- ✅ All Jinja2 variables resolve correctly
- ✅ No syntax errors in generated Python files
- ✅ Conditional blocks work for both project types
- ✅ Type hints pass Ty checking
- ✅ Linting passes with Ruff
- ✅ Tests pass with pytest
- ✅ Generated README.md has correct instructions

## Fixture Files

The `template/fixtures/` directory contains example data files:

- **`sample_data.csv`**: Example CSV for data processing scripts
- **`sample_api_response.json`**: Example API response for testing

**Purpose**: Demonstrate how users should structure their own fixture data.

**Note**: These are examples to guide users, not production data. Users should replace/extend these files based on their specific needs.

## Repository vs Generated Project

Remember the distinction:

| Aspect | Template Repository (here) | Generated Project |
|--------|----------------------------|-------------------|
| Purpose | Define what gets generated | Actual user project |
| Python code | Must be valid Jinja2 templates | Must be valid Python |
| Linting | Test generated output | Lint actual code |
| AGENTS.md | Instructions for template dev | Instructions for project dev |
| Dependencies | None (templates don't run) | Defined in pyproject.toml |

## Key Commands

Since this is a template repository, you don't run typical Python commands here. Instead:

```bash
# Automated testing (recommended)
task test-all         # Test both script and Django generation
task test-script      # Test script project only
task test-django      # Test Django project only
task clean            # Remove test projects

# Manual template generation
copier copy . /tmp/test-project

# Update an existing project from template
cd /path/to/generated/project
copier update

# Test generated project follows standards
cd /tmp/test-project
task init   # Install dependencies
task lint   # Ruff + Ty
task test   # pytest
```

**Workflow after template changes**:
1. Edit template files in `template/`
2. Run `task test-all` to verify both project types
3. If linting errors appear, fix them in the template files
4. If adding a new ignore rule for types or linting make sure it is inline or folder specific, always ask when adding ignore
5. Repeat until `task test-all` passes cleanly
---

### Check Ruff formatting changes ✅

- If running `task lint` in a freshly generated project modifies files (Ruff auto-formats), use the helper tasks to reproduce and capture diffs:
  - `task test-script-format-diff` — generate a script project and fail with `ruff-format.patch` if files are changed
  - `task test-django-format-diff` — generate a Django project and fail with `ruff-format.patch` if files are changed
  - `task test-format-diff` — run both checks

- When a task fails it writes `ruff-format.patch` and `ruff-format-files.txt` into the generated project directory (e.g., `/tmp/copier-test/test-script/ruff-format.patch`).

- To make it easier to collect patches and clean up generated projects, use the wrapper task `task test-format-diff-run`. This will run both format-diff checks, copy any `ruff-format.patch` and `ruff-format-files.txt` into `./tmp/ruff-format/`, and then remove the generated test projects. The task will exit non-zero if any patches were saved.

- Apply the patch's changes back into the template sources in `template/` (update the corresponding `.jinja` files so generated output is already formatted).

- Regenerate and re-run the format-diff tasks until they succeed (no Ruff modifications). This makes `task lint` idempotent for freshly generated projects and prevents widespread auto-format changes on first run.

## Tooling Reference

Generated projects use:

- **UV**: Package manager (replaces pip, poetry, pipenv)
- **Ruff**: Linting and formatting (replaces black, isort, flake8, pylint)
- **Ty**: Type checking (replaces mypy, Pylance)
- **go-task**: Task automation (replaces Make, shell scripts)
- **pytest**: Testing framework
- **Tailwind CSS 4.1**: Utility-first CSS via bunx (no Node.js required)
- **django-cotton**: Component-based templates for Django
- **Podman**: Container runtime for PostgreSQL (not Docker)

## When to Update template/AGENTS.md.jinja

Update the generated project documentation when:

- Adding new coding standards or best practices
- Introducing new tools or dependencies
- Changing project structure conventions
- Adding new Django patterns or requirements
- Modifying linting rules or type checking configuration

Keep `template/AGENTS.md.jinja` as the authoritative source for Python/Django standards that apply to both the template and generated projects.

## Additional Resources

- [Copier Documentation](https://copier.readthedocs.io/)
- [Jinja2 Template Designer Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS 4.1](https://tailwindcss.com/docs)

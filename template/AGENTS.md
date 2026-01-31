# Copilot Instructions for This Project

## Overview

This project is a modern Python application
Code quality is enforced using [Ruff](https://docs.astral.sh/ruff/) for linting and formating and [Ty](https://github.com/astral-sh/ruff/tree/main/crates/ty) for type checking.

**Editor Setup**: VS Code is configured to use Ty's language server for real-time type checking (not Pylance). Type errors will appear as you type, matching exactly what `task lint` checks in CI.

## General Tone

- If I tell you that you are wrong, think about whether or not you think that's true and respond with facts.
- Avoid apologizing or making conciliatory statements.
- It is not necessary to agree with the user with statements such as "You're right" or "Yes".
- Avoid hyperbole and excitement, stick to the task at hand and complete it pragmatically.
- Avoid words like seamless, captivating

## Best Practices

### 1. Code Style & Linting

- **Always run Ruff and Ty before committing code.**
- Follow [PEP8](https://peps.python.org/pep-0008/) style guidelines.
- Use type hints everywhere.
- Keep imports organized and sorted (stdlib, third-party, local) unused imports are removed (Ruff will check this).
- Prefer f-strings for string formatting.
- `open()` should be replaced by pathlib `Path.open()`
- use logguru.logger instead of print or logging.
- use dotenv for environment variables in a .env file
- First line of docstring should be in imperative mood
- Avoid having more than 5 params to functions, use a dataclass or pydantic model if it makes sense
- If in need of a http client prefer httpx over requests
- Always ask first before adding 3rd party libraries and provide choices if there are multiple candidates
- Prefer small, composable functions over large monolithic scripts. But do not create too many functions


### 2. Project Structure

**Directory Layout:**
- **`tmp/`** - Output files from scripts should be placed here by default. This directory is gitignored for temporary/generated content.
- **`fixtures/`** - Test fixtures and sample data files should be kept here for consistency.
- **`tests/`** - All test files using pytest should be organized in this directory.
- **`.env`** - Environment variables are stored here (gitignored). Never hardcode secrets in Python files.
- **`.vscode/`** - VS Code workspace settings configure the Ty language server for type checking (replaces Pylance).

**Important Notes:**
- Keep env variables in local `.env` file (ignored by git). Secrets should NEVER be hardcoded in Python files.
- Do not log credentials or full payloads with sensitive data.

**Dependency Management Enforcement:**

This project enforces the use of `uv` for package management. Standard `pip` and `pip3` commands are blocked through:
1. Wrapper scripts at `.venv/bin/pip` and `.venv/bin/pip3` that display error messages
2. A `.venv/pip.conf` file that breaks pip installs by pointing to a non-existent index

**Why Block pip?**
- **Consistency**: Ensures all developers use the same package manager (uv)
- **Lock file integrity**: Prevents accidental modifications outside of uv's lock file management
- **Speed**: uv is significantly faster than pip
- **Reliability**: Avoids dependency resolution conflicts between pip and uv

**If you accidentally try to use pip:**
You'll see: `Error: Standard 'pip' usage is prohibited in this project.`

**Instead, use these uv commands:**
- Add a package: `uv add <package-name>`
- Remove a package: `uv remove <package-name>`
- Sync dependencies: `uv sync` or `uv sync --extra dev`
- Add dev dependency: `uv add --dev <package-name>`

The pip blocking is set up automatically when running `task setup` or `task init`.


### 3. Testing

**General Testing Philosophy:**
- Write tests for all business logic and models if asked to do so
- Use [pytest](https://docs.pytest.org/) as the test runner
- Place tests in `tests/` directory
- Use fixtures from `tests/conftest.py` for common test setup
- Keep tests focused and readable - prefer readability over DRY in test code

**Running Tests:**
- `task test` - Run all tests
- `uv run pytest -k "pattern"` - Run tests matching pattern
- `uv run pytest -m "not slow"` - Skip slow tests during development
- `uv run pytest tests/test_specific.py::test_function` - Run specific test

**Using Fixtures:**
The project includes pre-configured fixtures in `tests/conftest.py`:
- `tmp_output_dir` - Use for file operations without affecting actual tmp/ directory
- `sample_json_data` - Use for testing JSON/API data processing
- `sample_csv_file` - Use for testing CSV/data file processing
- `fixtures_dir` - Access static test data from fixtures/ directory
- `mock_api_response` - Use for testing error handling scenarios
- `env_vars` - Pre-configured test environment variables (API keys, URLs, etc.)

**For API Integration POCs:**
- Use `env_vars` fixture to set test API credentials without modifying .env
- Create mock responses in `fixtures/` directory for repeatable testing
- Use `mock_api_response` fixture for testing error handling paths
- When testing httpx clients, consider using respx or pytest-httpx for mocking
- Example: Load `fixtures/sample_api_response.json` to test parsing logic

**For Data Processing POCs:**
- Use `sample_csv_file` fixture for testing data transformations
- Use `tmp_output_dir` for writing processed results
- Store reference datasets in `fixtures/` directory
- Use parametrized tests (`@pytest.mark.parametrize`) for multiple input scenarios
- Example: Test CSV parsing, filtering, aggregation with known sample data

**Test Markers:**
Use markers to categorize tests:
- `@pytest.mark.slow` - For tests that take >1 second
- `@pytest.mark.integration` - For tests that call external APIs
- `@pytest.mark.unit` - For isolated unit tests
- Configure additional markers in `[tool.pytest.ini_options]` in pyproject.toml

**Best Practices:**
- Test one thing per test function
- Use descriptive test names: `test_<what>_<condition>_<expected>`
- Use parametrize for testing multiple similar cases
- Don't test implementation details, test behavior
- For POCs, focus on critical paths and edge cases
- Mock external dependencies (APIs, databases) to keep tests fast and reliable

### 4. Dependency Management

- Use UV for managing dependencies via `uv sync`
- All dependencies are defined in `pyproject.toml`:
  - Production dependencies in `[project.dependencies]`
  - Development dependencies in `[project.optional-dependencies] dev`
- The `uv.lock` file is committed to git for reproducible environments
- Use `task install` to sync dependencies or `uv sync --extra dev` directly

### 5. Documentation

- Document all public functions and classes with docstrings. Keep them short on to the point
- Write comments as full sentences ending with a period. 
- Only add comments when it adds value for understanding
- Maintain a `README.md` with setup and usage instructions.

## Linting Commands

Run these commands via Task:
- `task lint` - Run all linting and formatting
- `task dev-watch` - Run ruff in watch mode for continuous linting
- Or run individually:
  - `uv run ruff check --fix .`
  - `uv run ruff format .`
  - `uv run ty check .`


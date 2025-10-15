# Copilot Instructions for This Project

## Overview

This project is a modern Python application built with

Code quality is enforced using [Ruff](https://docs.astral.sh/ruff/) for linting and formating and [Ty](https://ty-cli.github.io/) for type checking.

## General Tone

- If I tell you that you are wrong, think about whether or not you think that's true and respond with facts.
- Avoid apologizing or making conciliatory statements.
- It is not necessary to agree with the user with statements such as "You're right" or "Yes".
- Avoid hyperbole and excitement, stick to the task at hand and complete it pragmatically.
- Avoid words like seamless,captivating

## Best Practices

### 1. Code Style & Linting

- **Always run Ruff and Ty before committing code.**
- Follow [PEP8](https://peps.python.org/pep-0008/) style guidelines.
- Use type hints everywhere.
- Keep imports organized and unused imports removed (Ruff will check this).
- Prefer f-strings for string formatting.
- `open()` should be replaced by pathlib `Path.open()`
- use logguru.logger instead of print or logging.
- use dotenv for environment variables in a .env file
- First line of docstring should be in imperative mood
- avoid having more than 5 params to functions, use a dataclass or pydantic model if it makes sense

### 2. Project Structure

- Keep env variables in local .env file

### 3. Testing

- Write tests for all business logic and models if asked to do so
- Use [pytest](https://docs.pytest.org/) as the test runner.
- Place tests in a `tests/` directory.

### 4. Dependency Management

- Use uv for managing packages via uv pip
- Use a requirements.txt file for production dependencies.
- Use a requirements_dev.txt file for development dependencies.
- Use `pyproject.toml` for project metadata and linter configuration.

### 5. Documentation

- Document all public functions and classes with docstrings.
- Maintain a `README.md` with setup and usage instructions.

## Linting Commands

```sh
uv run ruff check --fix .
uv run ruff format .
uv run ty check .
```

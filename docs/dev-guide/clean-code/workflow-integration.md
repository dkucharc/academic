# Workflow Integration

Integrating code quality tools into your development workflow ensures consistent standards without manual effort. This section covers automation strategies for maintaining clean code.

## Pre-commit Hooks

[Pre-commit](https://pre-commit.com/) runs checks automatically before each commit, catching issues early.

### Installation and Setup

**Install pre-commit:**

=== "pip"
    ```bash
    pip install pre-commit
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge pre-commit
    # or
    mamba install -c conda-forge pre-commit
    ```

=== "uv"
    ```bash
    uv add pre-commit
    ```

=== "poetry"
    ```bash
    poetry add pre-commit --group dev
    ```

**Setup:**
```bash
# Create configuration file
touch .pre-commit-config.yaml

# Install git hooks
pre-commit install
```

### Configuration with Ruff

Create a `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
```

### Traditional Tools Configuration

If using traditional tools instead of Ruff:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy
```

### Running Pre-commit

```bash
# Run on all files
pre-commit run --all-files

# Run on specific files
pre-commit run --files src/main.py

# Skip hooks for emergency commits
git commit --no-verify -m "Emergency fix"

# Update hook versions
pre-commit autoupdate
```

## Continuous Integration (CI/CD)

Automate code quality checks in your CI/CD pipeline to ensure all code meets standards.

### GitHub Actions

Create `.github/workflows/code-quality.yml`:

```yaml
name: Code Quality

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  code-quality:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install ruff mypy pytest
        pip install -r requirements.txt

    - name: Lint with Ruff
      run: |
        ruff check .
        ruff format --check .

    - name: Type check with MyPy
      run: mypy src/

    - name: Run tests
      run: pytest tests/

    - name: Upload coverage reports
      uses: codecov/codecov-action@v3
      if: success()
```

### GitLab CI

Create `.gitlab-ci.yml`:

```yaml
stages:
  - quality
  - test

code-quality:
  stage: quality
  image: python:3.11
  before_script:
    - pip install ruff mypy
  script:
    - ruff check .
    - ruff format --check .
    - mypy src/
  only:
    - merge_requests
    - main

test:
  stage: test
  image: python:3.11
  before_script:
    - pip install -r requirements.txt
    - pip install pytest pytest-cov
  script:
    - pytest --cov=src tests/
  coverage: '/TOTAL.*\s+(\d+%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
```

### Azure DevOps

Create `azure-pipelines.yml`:

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

variables:
  pythonVersion: '3.11'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(pythonVersion)'
  displayName: 'Use Python $(pythonVersion)'

- script: |
    python -m pip install --upgrade pip
    pip install ruff mypy pytest
    pip install -r requirements.txt
  displayName: 'Install dependencies'

- script: |
    ruff check .
    ruff format --check .
  displayName: 'Lint code'

- script: mypy src/
  displayName: 'Type check'

- script: pytest tests/ --junitxml=junit/test-results.xml
  displayName: 'Run tests'

- task: PublishTestResults@2
  condition: succeededOrFailed()
  inputs:
    testResultsFiles: '**/test-*.xml'
    testRunTitle: 'Publish test results'
```

## IDE Integration

Configure your IDE for automatic code quality checks and formatting.

### VS Code

Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "ruff",
    "python.linting.mypyEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true,
        "source.fixAll": true
    },
    "files.associations": {
        "*.py": "python"
    },
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestArgs": [
        "tests"
    ]
}
```

Install recommended extensions in `.vscode/extensions.json`:

```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.mypy-type-checker",
        "charliermarsh.ruff",
        "ms-python.pytest"
    ]
}
```

### PyCharm

Configure PyCharm settings:

1. **File → Settings → Tools → External Tools**
   - Add Ruff as external tool
   - Command: `ruff`
   - Arguments: `check $FilePath$`

2. **File → Settings → Editor → Code Style → Python**
   - Set line length to 88
   - Configure import organization

3. **File → Settings → Editor → Inspections**
   - Enable Python type checker
   - Configure MyPy integration

### Vim/Neovim

Example configuration for Neovim with LSP:

```lua
-- init.lua
require('lspconfig').ruff_lsp.setup {}
require('lspconfig').pyright.setup {}

-- Auto-format on save
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = "*.py",
  callback = function()
    vim.lsp.buf.format()
  end,
})
```

## Project Configuration

### pyproject.toml

Centralize all tool configurations:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-research-project"
version = "0.1.0"
description = "Research project with clean code practices"
authors = [{name = "Your Name", email = "your.email@example.com"}]
dependencies = [
    "numpy>=1.21.0",
    "pandas>=1.3.0",
    "requests>=2.25.0",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.0",
    "mypy>=1.5.0",
    "pytest>=7.0.0",
    "pre-commit>=3.0.0",
]

[tool.ruff]
line-length = 88
target-version = "py38"
exclude = [
    ".git",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
]

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
    "N",   # pep8-naming
]
ignore = ["E501"]  # Line too long (handled by formatter)

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--verbose",
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html",
]

[tool.coverage.run]
source = ["src"]
omit = ["tests/*", "*/migrations/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
]
```

## Makefile for Common Tasks

Create a `Makefile` for easy command execution:

```makefile
.PHONY: help install dev-install lint format type-check test clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -e .

dev-install:  ## Install development dependencies
	pip install -e ".[dev]"
	pre-commit install

lint:  ## Run linting
	ruff check .

format:  ## Format code
	ruff format .

type-check:  ## Run type checking
	mypy src/

test:  ## Run tests
	pytest

test-cov:  ## Run tests with coverage
	pytest --cov=src --cov-report=html

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

all: lint type-check test  ## Run all checks
```

## Docker Integration

Include code quality checks in your Docker workflow:

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install dev dependencies for quality checks
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# Copy source code
COPY src/ src/
COPY tests/ tests/
COPY pyproject.toml .

# Run quality checks
RUN ruff check .
RUN ruff format --check .
RUN mypy src/
RUN pytest

# Final image without dev dependencies
FROM python:3.11-slim as production
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ src/
CMD ["python", "-m", "src.main"]
```

## Monitoring and Metrics

### Code Quality Badges

Add badges to your README to show code quality status:

```markdown
# My Research Project

[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/mypy-checked-blue)](https://mypy-lang.org/)
[![Tests](https://github.com/username/repo/workflows/tests/badge.svg)](https://github.com/username/repo/actions)
[![Coverage](https://codecov.io/gh/username/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/username/repo)
```

### Quality Gates

Set up quality gates in your CI/CD pipeline:

```yaml
# GitHub Actions example
- name: Quality Gate
  run: |
    # Fail if coverage is below 80%
    coverage report --fail-under=80

    # Fail if there are any linting errors
    ruff check . --exit-non-zero-on-fix

    # Fail if there are type errors
    mypy src/ --strict
```

## Best Practices for Workflow Integration

1. **Start Simple**: Begin with basic linting and formatting
2. **Gradual Adoption**: Add tools incrementally to avoid overwhelming the team
3. **Team Agreement**: Ensure all team members agree on the standards
4. **Documentation**: Document your workflow and tool configurations
5. **Regular Updates**: Keep tools and configurations up to date
6. **Flexibility**: Allow exceptions for special cases with proper justification

By integrating these tools into your workflow, you ensure that code quality is maintained automatically, reducing manual effort and improving consistency across your research projects.

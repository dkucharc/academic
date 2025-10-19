# Linting and Formatting

Linting helps identify programming errors, bugs, stylistic errors, and suspicious constructs. Formatting ensures consistent code style across your project.

## Ruff: The Modern Python Linter and Formatter

[Ruff](https://github.com/astral-sh/ruff) is an extremely fast Python linter and code formatter, written in Rust. It's designed to replace multiple tools (Flake8, isort, Black, and more) with a single, unified tool that's 10-100x faster than existing alternatives.

### Key Features

- **Speed**: 10-100x faster than existing Python linters
- **Comprehensive**: Implements over 800 lint rules from popular tools
- **All-in-one**: Combines linting, formatting, and import sorting
- **Compatible**: Drop-in replacement for Flake8, isort, and other tools
- **Configurable**: Highly customizable via `pyproject.toml`

### Installation

=== "pip"
    ```bash
    pip install ruff
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge ruff
    # or
    mamba install -c conda-forge ruff
    ```

=== "uv"
    ```bash
    uv add ruff
    ```

=== "poetry"
    ```bash
    poetry add ruff --group dev
    ```

### Basic Usage

```bash
# Linting - check for issues
ruff check .

# Formatting - format code
ruff format .

# Auto-fix issues where possible
ruff check --fix .

# Check specific files
ruff check src/main.py tests/

# Format specific files
ruff format src/main.py
```

### Configuration

Configure Ruff in your `pyproject.toml`:

```toml
[tool.ruff]
# Set the maximum line length to 88.
line-length = 88

# Assume Python 3.8+
target-version = "py38"

# Exclude specific directories
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

[tool.ruff.lint]
# Enable specific rule sets
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
    "N",   # pep8-naming
    "D",   # pydocstyle
]

# Ignore specific rules
ignore = [
    "E501",  # line too long (handled by formatter)
    "D100",  # missing docstring in public module
    "D104",  # missing docstring in public package
]

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.ruff.format]
# Use double quotes for strings.
quote-style = "double"

# Indent with spaces, rather than tabs.
indent-style = "space"

# Respect magic trailing commas.
skip-magic-trailing-comma = false

# Automatically detect the appropriate line ending.
line-ending = "auto"
```

### Rule Categories

Ruff supports rules from many popular linters:

| Code | Tool | Description |
|------|------|-------------|
| E, W | pycodestyle | Style violations |
| F | pyflakes | Logical errors |
| I | isort | Import sorting |
| B | flake8-bugbear | Bug-prone patterns |
| C4 | flake8-comprehensions | Comprehension improvements |
| UP | pyupgrade | Python version upgrades |
| N | pep8-naming | Naming conventions |
| D | pydocstyle | Docstring style |

## Traditional Linting Tools

While Ruff is becoming the modern standard, you may still encounter these traditional tools:

### Pylint

A comprehensive linter that checks for errors, enforces coding standards, and looks for code smells.

**Installation:**

=== "pip"
    ```bash
    pip install pylint
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge pylint
    # or
    mamba install -c conda-forge pylint
    ```

=== "uv"
    ```bash
    uv add pylint
    ```

=== "poetry"
    ```bash
    poetry add pylint --group dev
    ```

**Usage:**
```bash
pylint your_script.py
pylint src/

# Generate config file
pylint --generate-rcfile > .pylintrc
```

### Flake8

Combines PyFlakes, pycodestyle, and McCabe complexity checker.

**Installation:**

=== "pip"
    ```bash
    pip install flake8
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge flake8
    # or
    mamba install -c conda-forge flake8
    ```

=== "uv"
    ```bash
    uv add flake8
    ```

=== "poetry"
    ```bash
    poetry add flake8 --group dev
    ```

**Usage:**
```bash
flake8 your_script.py
flake8 src/

# Configuration in setup.cfg
[flake8]
max-line-length = 88
exclude = .git,__pycache__,build,dist
```

### Mypy

A static type checker for Python.

**Installation:**

=== "pip"
    ```bash
    pip install mypy
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge mypy
    # or
    mamba install -c conda-forge mypy
    ```

=== "uv"
    ```bash
    uv add mypy
    ```

=== "poetry"
    ```bash
    poetry add mypy --group dev
    ```

**Usage:**
```bash
mypy your_script.py
mypy src/

# Configuration in mypy.ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

## Traditional Formatting Tools

### Black

An opinionated formatter that adheres to PEP 8 guidelines.

**Installation:**

=== "pip"
    ```bash
    pip install black
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge black
    # or
    mamba install -c conda-forge black
    ```

=== "uv"
    ```bash
    uv add black
    ```

=== "poetry"
    ```bash
    poetry add black --group dev
    ```

**Usage:**
```bash
black your_script.py
black src/

# Configuration in pyproject.toml
[tool.black]
line-length = 88
target-version = ['py38']
```

### isort

A utility to sort imports alphabetically and automatically separate them into sections.

**Installation:**

=== "pip"
    ```bash
    pip install isort
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge isort
    # or
    mamba install -c conda-forge isort
    ```

=== "uv"
    ```bash
    uv add isort
    ```

=== "poetry"
    ```bash
    poetry add isort --group dev
    ```

**Usage:**
```bash
isort your_script.py
isort src/

# Configuration in pyproject.toml
[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
```

## Choosing Your Tools

### Modern Approach (Recommended)
Use Ruff for most projects:
- **Ruff** for linting and formatting
- **Mypy** for type checking
- **Pytest** for testing

### Traditional Approach
If you need specific features not in Ruff:
- **Black** for formatting
- **isort** for import sorting
- **Flake8** for linting
- **Mypy** for type checking

## Integration Examples

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

### GitHub Actions

```yaml
# .github/workflows/lint.yml
name: Lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install ruff
      - run: ruff check .
      - run: ruff format --check .
```

### VS Code Settings

```json
{
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

## Best Practices

1. **Start Early**: Set up linting and formatting from the beginning of your project
2. **Automate**: Use pre-commit hooks and CI/CD to enforce standards
3. **Be Consistent**: Choose one set of tools and stick with them
4. **Configure Appropriately**: Adjust rules for your project's needs
5. **Fix Gradually**: Don't try to fix all issues at once in existing projects

Remember: The goal is to improve code quality and consistency, not to achieve perfect scores on all metrics.

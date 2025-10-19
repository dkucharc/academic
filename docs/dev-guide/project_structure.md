# Project Structure

This document describes the standard project structure for research projects hosted on GitHub Classroom. This structure promotes clean code practices, reproducibility, and maintainability across all student assignments and research work.

## Overview

Our standardized project structure follows Python best practices and includes modern tooling for code quality, testing, and documentation. Each project should be self-contained, reproducible, and ready for collaborative development.

## Standard Directory Structure

```
my-research-project/
├── src/                     # Source code directory
│   ├── __init__.py         # Makes src a Python package
│   ├── problem_1.py        # Main problem solution
│   ├── utils.py            # Utility functions
│   └── data_processing.py  # Data processing modules
├── notebooks/              # Jupyter notebooks for exploration
│   ├── exploration.ipynb   # Data exploration
│   ├── analysis.ipynb      # Analysis and visualization
│   └── results.ipynb       # Final results presentation
├── tests/                  # Test files using pytest
│   ├── __init__.py         # Makes tests a Python package
│   ├── test_problem_1.py   # Tests for problem_1.py
│   ├── test_utils.py       # Tests for utility functions
│   └── conftest.py         # Pytest configuration and fixtures
├── data/                   # Data files (if small and non-sensitive)
│   ├── raw/                # Raw, unprocessed data
│   ├── processed/          # Cleaned and processed data
│   └── external/           # External datasets
├── docs/                   # Documentation
│   ├── README.md           # Project documentation
│   └── api.md              # API documentation
├── .github/                # GitHub-specific files
│   └── workflows/          # GitHub Actions workflows
│       └── tests.yml       # Automated testing workflow
├── Justfile                # Task runner for common commands
├── pyproject.toml          # Python project configuration
├── env.yaml                # Conda environment specification
├── .gitignore              # Git ignore patterns
├── .pre-commit-config.yaml # Pre-commit hooks configuration
└── README.md               # Main project documentation
```

## Core Files and Directories

### Source Code (`src/`)

The [`src/`](src/) directory contains all your Python source code. This structure follows the "src layout" pattern, which provides better isolation and testing practices.

**Key files:**
- [`src/problem_1.py`](src/problem_1.py) - Main implementation for your assignment
- [`src/utils.py`](src/utils.py) - Reusable utility functions
- [`src/__init__.py`](src/__init__.py) - Package initialization

**Benefits of src layout:**
- Prevents accidental imports of development code
- Clearer separation between source and test code
- Better support for packaging and distribution

### Notebooks (`notebooks/`)

The [`notebooks/`](notebooks/) directory contains Jupyter notebooks for data exploration, analysis, and result presentation. Notebooks are excellent for:

- Exploratory data analysis
- Prototyping algorithms
- Creating visualizations
- Documenting analysis workflows

**Organization tips:**
- Use descriptive names with numbers for ordering: `01_data_exploration.ipynb`
- Keep notebooks focused on specific tasks
- Export important functions to [`src/`](src/) modules
- Clear outputs before committing to version control

### Tests (`tests/`)

The [`tests/`](tests/) directory contains all test files using [pytest](https://pytest.org/). Testing is crucial for:

- Verifying code correctness
- Preventing regressions
- Documenting expected behavior
- Building confidence in your implementation

**Test file naming:**
- `test_*.py` or `*_test.py` patterns
- Mirror the structure of your [`src/`](src/) directory
- One test file per source module

See the [Testing with Pytest](#testing-with-pytest) section for detailed information.

### Configuration Files

#### [`pyproject.toml`](pyproject.toml)
Central configuration file for Python projects. Contains:

- Project metadata and dependencies
- Tool configurations (Ruff, pytest, mypy)
- Build system specifications

For detailed configuration options, see our [Linting & Formatting](clean-code/linting-formatting.md) and [Workflow Integration](clean-code/workflow-integration.md) guides.

#### [`env.yaml`](env.yaml)
Conda environment specification for reproducible environments:

```yaml
name: my-research-project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy
  - pandas
  - matplotlib
  - scipy
  - jupyter
  - pytest
  - pip
  - pip:
    - ruff
    - mypy
```

For more details, see our [Python Environment Management](getting-started/python_management.md) guide.

#### [`.gitignore`](.gitignore)
Specifies files and directories that Git should ignore:

- Python bytecode (`__pycache__/`, `*.pyc`)
- Virtual environments (`.venv/`, `env/`)
- IDE files (`.vscode/`, `.idea/`)
- Data files (if large or sensitive)
- Build artifacts (`build/`, `dist/`)

#### [`.pre-commit-config.yaml`](.pre-commit-config.yaml)
Configuration for pre-commit hooks that run automatically before each commit. See [Workflow Integration](clean-code/workflow-integration.md) for setup details.

## Justfile - Task Automation

The [`Justfile`](Justfile) provides a simple way to run common development tasks. [Just](https://github.com/casey/just) is a modern alternative to Make with a cleaner syntax.

### Current Justfile Commands

Our current [`Justfile`](Justfile) includes:

```just
# Run pre-commit hooks on all files
pc:
    pre-commit run --all-files

# Serve the MkDocs documentation
serve:
    poetry run mkdocs serve
```

### Recommended Justfile for Student Projects

For student research projects, we recommend expanding the [`Justfile`](Justfile) with these common tasks:

```just
# Show available commands
default:
    @just --list

# Install dependencies and setup development environment
setup:
    conda env create -f env.yaml
    conda activate my-research-project
    pre-commit install

# Run all tests
test:
    pytest tests/ -v

# Run tests with coverage report
test-cov:
    pytest tests/ --cov=src --cov-report=html --cov-report=term

# Run linting and formatting
lint:
    ruff check src/ tests/
    ruff format src/ tests/

# Run type checking
typecheck:
    mypy src/

# Run all quality checks
check: lint typecheck test

# Clean up generated files
clean:
    rm -rf .pytest_cache/
    rm -rf htmlcov/
    rm -rf .coverage
    find . -type d -name __pycache__ -delete
    find . -type f -name "*.pyc" -delete

# Start Jupyter notebook server
notebook:
    jupyter notebook notebooks/

# Run the main problem solution
run:
    python -m src.problem_1
```

### Installing Just

Install Just using one of these methods:

```bash
# Using cargo (Rust package manager)
cargo install just

# Using conda
conda install -c conda-forge just

# Using homebrew (macOS)
brew install just

# Using pip (unofficial)
pip install just-install
```

## Testing with Pytest

[Pytest](https://pytest.org/) is the recommended testing framework for Python projects. It provides powerful features with minimal boilerplate.

### Basic Test Structure

```python
# tests/test_problem_1.py
import pytest
from src.problem_1 import solve_problem, validate_input

def test_solve_problem_basic():
    """Test basic functionality of solve_problem."""
    result = solve_problem([1, 2, 3])
    assert result == 6

def test_solve_problem_empty_input():
    """Test solve_problem with empty input."""
    result = solve_problem([])
    assert result == 0

def test_validate_input_valid():
    """Test validate_input with valid data."""
    assert validate_input([1, 2, 3]) is True

def test_validate_input_invalid():
    """Test validate_input with invalid data."""
    with pytest.raises(ValueError):
        validate_input("not a list")

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    """Test using a fixture."""
    result = solve_problem(sample_data)
    assert result == 15
```

### Pytest Configuration

Configure pytest in [`pyproject.toml`](pyproject.toml):

```toml
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
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
]
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_problem_1.py

# Run tests matching a pattern
pytest -k "test_solve"

# Run tests with verbose output
pytest -v

# Run tests and stop on first failure
pytest -x
```

### Test Organization Best Practices

1. **Mirror source structure**: Test files should mirror your [`src/`](src/) directory structure
2. **Descriptive names**: Use clear, descriptive test function names
3. **One concept per test**: Each test should verify one specific behavior
4. **Use fixtures**: Share common test data and setup using pytest fixtures
5. **Test edge cases**: Include tests for boundary conditions and error cases

## Development Workflow

### Initial Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd my-research-project
   ```

2. **Set up environment:**
   ```bash
   # Using conda (recommended)
   conda env create -f env.yaml
   conda activate my-research-project

   # Or using pip + venv
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install development tools:**
   ```bash
   pre-commit install
   ```

4. **Verify setup:**
   ```bash
   just test  # or pytest
   just lint  # or ruff check .
   ```

### Daily Development

1. **Start working:**
   ```bash
   conda activate my-research-project  # or source .venv/bin/activate
   ```

2. **Run tests frequently:**
   ```bash
   just test  # or pytest
   ```

3. **Check code quality:**
   ```bash
   just check  # or just lint && just typecheck
   ```

4. **Before committing:**
   ```bash
   just check  # Ensure all checks pass
   git add .
   git commit -m "Descriptive commit message"
   ```

### Code Quality Tools

Our projects use modern Python tooling for maintaining code quality:

- **[Ruff](https://github.com/astral-sh/ruff)**: Fast linting and formatting (replaces Black, isort, Flake8)
- **[MyPy](https://mypy.readthedocs.io/)**: Static type checking
- **[Pytest](https://pytest.org/)**: Testing framework
- **[Pre-commit](https://pre-commit.com/)**: Git hooks for automated checks

For detailed information about these tools, see:
- [Linting & Formatting](clean-code/linting-formatting.md)
- [Type Hints](clean-code/type-hints.md)
- [Workflow Integration](clean-code/workflow-integration.md)

## GitHub Classroom Integration

### Repository Setup

When you accept a GitHub Classroom assignment:

1. **Repository is automatically created** with the standard structure
2. **GitHub Actions workflows** are pre-configured for automated testing
3. **Branch protection rules** may be enabled to require passing tests

### Automated Testing

GitHub Actions automatically run tests on every push and pull request:

```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov ruff mypy
      - name: Run linting
        run: ruff check .
      - name: Run type checking
        run: mypy src/
      - name: Run tests
        run: pytest --cov=src
```

### Submission Guidelines

1. **Complete all required functions** in [`src/problem_1.py`](src/problem_1.py)
2. **Write comprehensive tests** in [`tests/`](tests/)
3. **Ensure all tests pass** locally and in GitHub Actions
4. **Follow code quality standards** (linting, formatting, type hints)
5. **Update documentation** as needed
6. **Commit frequently** with descriptive messages

## Best Practices

### Code Organization

1. **Keep functions small and focused** - Each function should do one thing well
2. **Use meaningful names** - Variables, functions, and classes should have descriptive names
3. **Add type hints** - Help with code clarity and catch errors early
4. **Write docstrings** - Document your functions and classes
5. **Separate concerns** - Keep data processing, analysis, and visualization separate

### Version Control

1. **Commit frequently** - Small, focused commits are easier to review and debug
2. **Write good commit messages** - Explain what and why, not just what
3. **Use branches** - Create feature branches for significant changes
4. **Don't commit generated files** - Keep your repository clean

### Testing

1. **Write tests first** - Test-driven development helps design better code
2. **Test edge cases** - Don't just test the happy path
3. **Keep tests simple** - Tests should be easy to understand and maintain
4. **Use descriptive test names** - Test names should explain what is being tested

### Documentation

1. **Keep README up to date** - Explain how to set up and run your project
2. **Document your analysis** - Use notebooks to explain your thought process
3. **Comment complex code** - Help future you understand what you were thinking
4. **Include examples** - Show how to use your functions

## Troubleshooting

### Common Issues

**Environment activation fails:**
```bash
# Make sure conda is initialized
conda init
# Restart your terminal
# Try activating again
conda activate my-research-project
```

**Tests fail with import errors:**
```bash
# Make sure you're in the project root directory
# Install the project in development mode
pip install -e .
```

**Pre-commit hooks fail:**
```bash
# Run hooks manually to see detailed errors
pre-commit run --all-files
# Fix the issues and try again
```

**Ruff formatting conflicts:**
```bash
# Let Ruff fix what it can automatically
ruff check --fix .
ruff format .
```

### Getting Help

1. **Check the error message** - Most errors have helpful information
2. **Read the documentation** - Links to tool documentation are provided throughout
3. **Ask for help** - Use GitHub Issues or class discussion forums
4. **Search online** - Stack Overflow and GitHub Issues are great resources

## Related Documentation

- [Getting Started Guide](getting-started/intro.md) - Initial setup and installation
- [Python Environment Management](getting-started/python_management.md) - Detailed environment setup
- [Clean Code Practices](clean-code/index.md) - Code quality guidelines
- [Linting & Formatting](clean-code/linting-formatting.md) - Tool configuration and usage
- [Type Hints](clean-code/type-hints.md) - Static typing in Python
- [Workflow Integration](clean-code/workflow-integration.md) - Automation and CI/CD
- [Git & GitHub Cheat Sheet](../cheat-sheets/git-github.md) - Version control reference
- [Conda Cheat Sheet](../cheat-sheets/conda.md) - Environment management reference

This structure ensures that your research projects are reproducible, maintainable, and follow modern Python development best practices. By following these guidelines, you'll develop good habits that will serve you well in both academic and professional software development.

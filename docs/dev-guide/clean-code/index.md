# Clean Code

Writing clean, readable, and maintainable code is crucial for reproducible research.

This section covers Python coding standards, linting, and formatting tools to help you write high-quality, consistent code.

## Overview

Clean code practices ensure that your research code is:

- **Readable**: Easy to understand by you and your collaborators
- **Maintainable**: Simple to modify and extend
- **Reproducible**: Consistent results across different environments
- **Professional**: Follows industry standards and best practices

## What You'll Learn

This guide covers:

1. **[Python Standards](python-standards.md)**: Understanding PEPs and core Python conventions
2. **[Style Guidelines](style-guidelines.md)**: PEP 8 and formatting best practices
3. **[Linting and Formatting](linting-formatting.md)**: Modern tools like Ruff for code quality
4. **[Type Hints](type-hints.md)**: Using Python's type system for better code
5. **[Documentation](documentation.md)**: Writing effective comments and docstrings
6. **[Best Practices](best-practices.md)**: Additional principles for clean code
7. **[Workflow Integration](workflow-integration.md)**: Automating code quality in your development process

## Quick Start

For immediate improvement to your code quality:

1. **Install Ruff:**

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

2. Run linting: `ruff check .`
3. Auto-format: `ruff format .`
4. Add type hints to your functions
5. Write docstrings for your modules and functions

By following these guidelines and using modern tools, you'll produce cleaner, more maintainable, and more reproducible code.

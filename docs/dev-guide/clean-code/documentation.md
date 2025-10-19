# Documentation

Good documentation is essential for maintainable code. This includes comments, docstrings, and following established documentation standards.

## Google Python Style Guide for Documentation

Following [Google's Python Style Guide for Comments and Docstrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) ensures consistent and comprehensive documentation.

### Docstring Format

Use the Google docstring format for consistency:

```python
def fetch_smalltable_rows(table_handle: bigtable.Table,
                         keys: Sequence[bytes],
                         require_all_keys: bool = False,
                         ) -> Mapping[bytes, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle. String keys will be UTF-8 encoded.

    Args:
        table_handle: An open bigtable.Table instance.
        keys: A sequence of strings representing the key of each table
            row to fetch. String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be
            returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes. If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
```

## Docstring Conventions (PEP 257)

[PEP 257](https://peps.python.org/pep-0257/) defines docstring conventions:

### Basic Rules

1. Use triple double quotes for docstrings
2. Start with a one-line summary
3. Use imperative mood ("Return" not "Returns")
4. End the summary line with a period
5. Leave a blank line after the summary if there's more content

### Module Docstrings

```python
"""A one-line summary of the module or program.

This module provides utilities for data processing and analysis.
It includes functions for cleaning, transforming, and validating
research data from various sources.

Example:
    Basic usage of this module:

        from data_utils import clean_data, validate_input

        cleaned = clean_data(raw_data)
        if validate_input(cleaned):
            process_data(cleaned)

Attributes:
    DEFAULT_ENCODING (str): The default character encoding.
    MAX_RETRIES (int): Maximum number of retry attempts.
"""

DEFAULT_ENCODING = "utf-8"
MAX_RETRIES = 3
```

### Class Docstrings

```python
class DataProcessor:
    """A class for processing research data.

    This class provides methods for cleaning, transforming, and validating
    data from various research sources. It maintains state about the
    processing pipeline and can handle multiple data formats.

    Attributes:
        config: A dictionary containing processing configuration.
        processed_count: The number of records processed.

    Example:
        processor = DataProcessor(config={'format': 'csv'})
        result = processor.process_file('data.csv')
    """

    def __init__(self, config: dict[str, str]) -> None:
        """Initialize the DataProcessor.

        Args:
            config: Configuration dictionary with processing options.
        """
        self.config = config
        self.processed_count = 0
```

### Function Docstrings

```python
def calculate_statistics(data: list[float],
                        include_median: bool = True) -> dict[str, float]:
    """Calculate basic statistics for a dataset.

    Computes mean, standard deviation, and optionally median
    for the provided numerical data.

    Args:
        data: A list of numerical values to analyze.
        include_median: Whether to include median in the results.

    Returns:
        A dictionary containing statistical measures:
        - 'mean': The arithmetic mean
        - 'std': The standard deviation
        - 'median': The median (if include_median is True)

    Raises:
        ValueError: If the data list is empty.
        TypeError: If data contains non-numerical values.

    Example:
        >>> data = [1, 2, 3, 4, 5]
        >>> stats = calculate_statistics(data)
        >>> print(stats['mean'])
        3.0
    """
    if not data:
        raise ValueError("Data list cannot be empty")

    # Implementation here
    pass
```

## Comment Guidelines

### When to Comment

**Good reasons to comment:**
- Explain complex algorithms or business logic
- Clarify non-obvious code behavior
- Provide context for decisions
- Explain workarounds or temporary solutions
- Document external dependencies or assumptions

```python
# Use binary search for O(log n) performance on sorted data
def find_insertion_point(sorted_list: list[int], value: int) -> int:
    """Find the index where value should be inserted to maintain sort order."""
    left, right = 0, len(sorted_list)

    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid

    return left

# Workaround for API rate limiting - retry with exponential backoff
def api_request_with_retry(url: str, max_retries: int = 3) -> dict:
    """Make API request with retry logic for rate limiting."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Rate limited
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
            else:
                raise
    raise Exception(f"Failed after {max_retries} attempts")
```

### When NOT to Comment

**Avoid these types of comments:**
- Stating the obvious
- Repeating what the code clearly shows
- Outdated or incorrect information

```python
# Bad - states the obvious
x = x + 1  # Increment x by 1
user_count = len(users)  # Get the length of users list

# Good - explains why
x = x + 1  # Compensate for zero-based indexing
user_count = len(users)  # Cache count to avoid repeated calculations
```

## Documentation Tools

### Sphinx

Generate documentation from docstrings:

=== "pip"
    ```bash
    pip install sphinx
    sphinx-quickstart
    sphinx-build -b html source build
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge sphinx
    # or
    mamba install -c conda-forge sphinx
    sphinx-quickstart
    sphinx-build -b html source build
    ```

=== "uv"
    ```bash
    uv add sphinx
    sphinx-quickstart
    sphinx-build -b html source build
    ```

=== "poetry"
    ```bash
    poetry add sphinx --group dev
    sphinx-quickstart
    sphinx-build -b html source build
    ```

### MkDocs

Create documentation websites:

=== "pip"
    ```bash
    pip install mkdocs
    mkdocs new my-project
    mkdocs serve
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge mkdocs
    # or
    mamba install -c conda-forge mkdocs
    mkdocs new my-project
    mkdocs serve
    ```

=== "uv"
    ```bash
    uv add mkdocs
    mkdocs new my-project
    mkdocs serve
    ```

=== "poetry"
    ```bash
    poetry add mkdocs --group dev
    mkdocs new my-project
    mkdocs serve
    ```

### Pydoc

Built-in Python documentation generator:

```bash
python -m pydoc -w mymodule
python -m pydoc -p 8080  # Start web server
```

## Type Hints as Documentation

Type hints serve as inline documentation:

```python
from typing import Optional, Union
from pathlib import Path

def load_config(
    config_path: Path,
    default_values: Optional[dict[str, str]] = None,
    format_type: Union[str, None] = None
) -> dict[str, str]:
    """Load configuration from file.

    The type hints clearly show:
    - config_path must be a Path object
    - default_values is optional and should be a string dict
    - format_type can be a string or None
    - Returns a string dictionary
    """
    pass
```

## Documentation Best Practices

### 1. Keep Documentation Current

```python
def process_data(data: list[dict]) -> list[dict]:
    """Process research data records.

    Note: Update this docstring when changing the algorithm!

    Args:
        data: List of data records as dictionaries.

    Returns:
        Processed data records.
    """
    # When you modify this function, update the docstring too
    pass
```

### 2. Use Examples

```python
def format_citation(authors: list[str], title: str, year: int) -> str:
    """Format a research paper citation.

    Args:
        authors: List of author names.
        title: Paper title.
        year: Publication year.

    Returns:
        Formatted citation string.

    Example:
        >>> authors = ["Smith, J.", "Doe, A."]
        >>> citation = format_citation(authors, "Research Methods", 2023)
        >>> print(citation)
        Smith, J., & Doe, A. (2023). Research Methods.
    """
    pass
```

### 3. Document Edge Cases

```python
def calculate_percentage(part: float, whole: float) -> float:
    """Calculate percentage.

    Args:
        part: The part value.
        whole: The whole value.

    Returns:
        Percentage as a float (0-100).

    Raises:
        ZeroDivisionError: If whole is zero.
        ValueError: If part or whole is negative.

    Note:
        Returns 0.0 if both part and whole are zero.
    """
    if whole == 0 and part == 0:
        return 0.0
    if whole == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if part < 0 or whole < 0:
        raise ValueError("Values must be non-negative")

    return (part / whole) * 100
```

### 4. Use Consistent Style

Choose one docstring style and stick to it throughout your project:

- **Google Style**: Clear sections (Args, Returns, Raises)
- **NumPy Style**: Similar to Google but different formatting
- **Sphinx Style**: Uses reStructuredText markup

### 5. Document Public APIs

Focus documentation efforts on public interfaces:

```python
class DataAnalyzer:
    """Public class for data analysis."""

    def analyze(self, data: list) -> dict:
        """Public method - needs full documentation."""
        return self._internal_process(data)

    def _internal_process(self, data: list) -> dict:
        """Private method - minimal documentation is fine."""
        # Implementation details
        pass
```

## README Files

Every project should have a comprehensive README:

```markdown
# Project Name

Brief description of what this project does.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from myproject import MyClass

analyzer = MyClass()
result = analyzer.process(data)
```

## API Reference

Link to detailed API documentation.

## Contributing

Guidelines for contributors.

## License

License information.
```

Good documentation makes your code accessible to others (including your future self). Invest time in writing clear, helpful documentation that explains not just what your code does, but why it does it.

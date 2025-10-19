# Style Guidelines

## PEP 8: Style Guide for Python Code

[PEP 8](https://peps.python.org/pep-0008/) is the official style guide for Python code. Following PEP 8 ensures consistency across Python projects. Key points include:

### Indentation
- Use 4 spaces per indentation level
- Never mix tabs and spaces
- Continuation lines should align wrapped elements

```python
# Correct
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Incorrect
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

### Maximum Line Length
- Limit lines to 79 characters for code
- Limit lines to 72 characters for comments and docstrings
- Some teams use 88 characters (Black formatter default)

```python
# Correct - break long lines
result = some_function_that_takes_arguments(
    'a', 'b', 'c', 'd', 'e', 'f'
)

# Incorrect - too long
result = some_function_that_takes_arguments('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
```

### Imports
Place imports at the top of the file, grouped in the following order:

1. Standard library imports
2. Related third-party imports
3. Local application/library specific imports

```python
# Standard library
import os
import sys
from pathlib import Path

# Third-party
import numpy as np
import pandas as pd
import requests

# Local
from myproject import mymodule
from . import sibling_module
```

### Whitespace
- Use blank lines to separate functions and classes
- Use blank lines sparingly inside functions to separate logical sections
- Avoid extraneous whitespace

```python
# Correct
spam(ham[1], {eggs: 2})

# Incorrect
spam( ham[ 1 ], { eggs: 2 } )
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Functions, variables, attributes | `lowercase_with_underscores` | `my_function`, `user_name` |
| Classes | `CapitalizedWords` | `MyClass`, `HTTPServer` |
| Constants | `ALL_CAPS` | `MAX_SIZE`, `DEFAULT_TIMEOUT` |
| Private attributes | `_leading_underscore` | `_internal_var` |
| Protected attributes | `__double_leading_underscore` | `__private_var` |

```python
# Correct naming
class DataProcessor:
    MAX_ITEMS = 1000

    def __init__(self):
        self.item_count = 0
        self._internal_state = {}

    def process_data(self, input_data):
        return self._clean_data(input_data)

    def _clean_data(self, data):
        # Private method
        return data.strip()
```

### Comments
- Use inline comments sparingly
- Comments should be complete sentences
- Update comments when code changes

```python
# Correct - explains why, not what
x = x + 1  # Compensate for border

# Incorrect - states the obvious
x = x + 1  # Increment x
```

## Beyond PEP 8

While PEP 8 is fundamental, consider these additional style principles:

### Consistency
- Be consistent within a project
- Follow existing code style in a codebase
- Use automated formatters to maintain consistency

### Readability
- Choose descriptive names over short ones
- Avoid abbreviations unless they're widely understood
- Use meaningful variable names

```python
# Good
user_count = len(active_users)
for user in active_users:
    send_notification(user)

# Poor
n = len(u)
for x in u:
    send_notification(x)
```

### Simplicity
- Prefer simple, straightforward solutions
- Avoid clever code that's hard to understand
- Use built-in functions when appropriate

```python
# Good - clear and simple
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]

# Overly complex
squares = list(map(lambda x: x ** 2, numbers))
```

## Modern Style Considerations

### F-strings (PEP 498)
Prefer f-strings for string formatting:

```python
# Modern (Python 3.6+)
name = "Alice"
age = 30
message = f"Hello, {name}! You are {age} years old."

# Older style
message = "Hello, {}! You are {} years old.".format(name, age)
message = "Hello, %s! You are %d years old." % (name, age)
```

### Pathlib
Use `pathlib` for file system operations:

```python
# Modern
from pathlib import Path

config_file = Path("config") / "settings.json"
if config_file.exists():
    content = config_file.read_text()

# Older style
import os

config_file = os.path.join("config", "settings.json")
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        content = f.read()
```

## Automated Style Checking

Use tools to automatically check and enforce style:

- **Ruff**: Modern, fast linter and formatter
- **Black**: Opinionated code formatter
- **isort**: Import statement organizer
- **Flake8**: Style guide enforcement

These tools help maintain consistent style across your codebase without manual effort.

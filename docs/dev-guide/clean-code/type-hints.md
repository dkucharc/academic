# Type Hints

Type hints, introduced in [PEP 484](https://peps.python.org/pep-0484/), enable static type checking and improve code clarity. They help catch type-related errors early and make code more self-documenting.

## Why Use Type Hints?

1. **Early Error Detection**: Catch type-related bugs before runtime
2. **Better IDE Support**: Enhanced autocomplete and refactoring
3. **Self-Documenting Code**: Types serve as inline documentation
4. **Improved Maintainability**: Easier to understand and modify code
5. **Tool Integration**: Better support from linters and static analyzers

## Basic Type Hints

### Function Annotations

```python
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)
```

### Variable Annotations

```python
# Python 3.6+ variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

# For variables without initial values
user_id: int
config: dict[str, str]
```

## Built-in Types

### Basic Types

```python
def process_data(
    text: str,
    count: int,
    ratio: float,
    is_valid: bool
) -> None:
    print(f"Processing {text} with {count} items")
```

### Collection Types (Python 3.9+)

```python
# Lists
def process_names(names: list[str]) -> list[str]:
    return [name.title() for name in names]

# Dictionaries
def get_user_info() -> dict[str, str]:
    return {"name": "Alice", "email": "alice@example.com"}

# Sets
def get_unique_ids(data: list[int]) -> set[int]:
    return set(data)

# Tuples
def get_coordinates() -> tuple[float, float]:
    return (10.5, 20.3)

# Tuple with variable length
def get_scores() -> tuple[int, ...]:
    return (85, 92, 78, 96)
```

### Optional and Union Types

```python
from typing import Optional, Union

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    """Find a user by ID, return None if not found."""
    # Implementation here
    return None

# Union types (Python 3.10+)
def handle_input(value: str | int) -> str:
    """Handle data that can be either string or integer."""
    return str(value)

# Older syntax (before Python 3.10)
def handle_data(data: Union[str, int]) -> str:
    return str(data)
```

## Advanced Type Hints

### Generic Types

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

# Usage
string_stack: Stack[str] = Stack()
string_stack.push("hello")

int_stack: Stack[int] = Stack()
int_stack.push(42)
```

### Callable Types

```python
from typing import Callable

def apply_operation(
    numbers: list[int],
    operation: Callable[[int], int]
) -> list[int]:
    """Apply an operation to each number in the list."""
    return [operation(num) for num in numbers]

# Usage
def square(x: int) -> int:
    return x ** 2

result = apply_operation([1, 2, 3, 4], square)
```

### Protocol (Structural Typing)

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def render_shape(shape: Drawable) -> None:
    """Render any drawable shape."""
    shape.draw()

# Both Circle and Square can be used
render_shape(Circle())
render_shape(Square())
```

### Literal Types

```python
from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    """Set file operation mode."""
    print(f"Mode set to: {mode}")

# Valid calls
set_mode("read")
set_mode("write")

# This would cause a type error
# set_mode("invalid")  # Type error
```

## Type Aliases

Create aliases for complex types:

```python
# Type aliases
UserId = int
UserData = dict[str, str | int]
Coordinates = tuple[float, float]

def create_user(user_id: UserId, data: UserData) -> None:
    print(f"Creating user {user_id} with data {data}")

def calculate_distance(point1: Coordinates, point2: Coordinates) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
```

## Modern Type Hints (Python 3.9+)

### Built-in Collections

```python
# Python 3.9+ - use built-in types directly
def process_data(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

def merge_configs(
    config1: dict[str, str],
    config2: dict[str, str]
) -> dict[str, str]:
    return {**config1, **config2}

# Before Python 3.9 - needed typing module
from typing import List, Dict

def process_data_old(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}
```

### Union Operator (Python 3.10+)

```python
# Python 3.10+ - use | for unions
def process_value(value: str | int | float) -> str:
    return str(value)

def find_item(items: list[str], query: str) -> str | None:
    for item in items:
        if query in item:
            return item
    return None

# Before Python 3.10
from typing import Union

def process_value_old(value: Union[str, int, float]) -> str:
    return str(value)
```

## Type Checking with Mypy

Install and use Mypy for static type checking:

=== "pip"
    ```bash
    pip install mypy
    mypy your_script.py
    ```

=== "conda/mamba"
    ```bash
    conda install -c conda-forge mypy
    # or
    mamba install -c conda-forge mypy
    mypy your_script.py
    ```

=== "uv"
    ```bash
    uv add mypy
    mypy your_script.py
    ```

=== "poetry"
    ```bash
    poetry add mypy --group dev
    mypy your_script.py
    ```

### Mypy Configuration

Create a `mypy.ini` file:

```ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
```

Or configure in `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true

# Per-module options
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

## Best Practices

### 1. Start Gradually
```python
# Start with function signatures
def calculate_total(prices: list[float]) -> float:
    return sum(prices)

# Add variable annotations where helpful
total_price: float = calculate_total([10.99, 5.50, 3.25])
```

### 2. Use Specific Types
```python
# Good - specific
def get_user_ages() -> dict[str, int]:
    return {"alice": 30, "bob": 25}

# Less helpful - too generic
def get_user_ages() -> dict:
    return {"alice": 30, "bob": 25}
```

### 3. Handle Optional Values
```python
def find_user(user_id: int) -> Optional[dict[str, str]]:
    # Always handle the None case
    user = database.get_user(user_id)
    if user is None:
        return None
    return {"name": user.name, "email": user.email}
```

### 4. Use Type Aliases for Complex Types
```python
# Define complex types once
JSONData = dict[str, str | int | float | bool | None]
APIResponse = dict[str, JSONData | list[JSONData]]

def process_api_response(response: APIResponse) -> None:
    # Implementation here
    pass
```

## Common Patterns

### Factory Functions
```python
from typing import TypeVar

T = TypeVar('T')

def create_list(item_type: type[T], *items: T) -> list[T]:
    return list(items)

# Usage
numbers = create_list(int, 1, 2, 3)  # list[int]
names = create_list(str, "a", "b", "c")  # list[str]
```

### Context Managers
```python
from typing import Iterator
from contextlib import contextmanager

@contextmanager
def database_transaction() -> Iterator[None]:
    # Setup
    begin_transaction()
    try:
        yield
    except Exception:
        rollback_transaction()
        raise
    else:
        commit_transaction()
```

## Integration with IDEs

Most modern IDEs support type hints:

- **VS Code**: Install Python extension for full type checking support
- **PyCharm**: Built-in type checking and inference
- **Vim/Neovim**: Use language servers like Pylsp or Pyright

Type hints make your code more professional, maintainable, and less prone to bugs. Start using them in new code and gradually add them to existing projects.

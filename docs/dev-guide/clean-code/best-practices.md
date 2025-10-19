# Best Practices

Beyond style guides and tools, these principles will help you write cleaner, more maintainable code.

## Core Principles

### 1. DRY (Don't Repeat Yourself)

Avoid duplicating code. Extract repeated logic into functions or classes.

```python
# Bad - repetitive code
def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

def calculate_sphere_volume(radius):
    return (4/3) * 3.14159 * radius * radius * radius

# Good - extract constants and common patterns
import math

PI = math.pi

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    return PI * radius ** 2

def calculate_circle_circumference(radius: float) -> float:
    """Calculate the circumference of a circle."""
    return 2 * PI * radius

def calculate_sphere_volume(radius: float) -> float:
    """Calculate the volume of a sphere."""
    return (4/3) * PI * radius ** 3
```

### 2. KISS (Keep It Simple, Stupid)

Write simple, straightforward code. Avoid over-engineering.

```python
# Bad - overly complex
def is_even_complex(number):
    return True if number % 2 == 0 else False

def get_user_status_complex(user):
    if user.is_active == True:
        if user.subscription_expired == False:
            return "active"
        else:
            return "expired"
    else:
        return "inactive"

# Good - simple and clear
def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0

def get_user_status(user) -> str:
    """Get user status based on activity and subscription."""
    if not user.is_active:
        return "inactive"
    if user.subscription_expired:
        return "expired"
    return "active"
```

### 3. YAGNI (You Aren't Gonna Need It)

Don't add functionality until it's necessary.

```python
# Bad - premature optimization and unused features
class DataProcessor:
    def __init__(self):
        self.cache = {}  # Might need caching later
        self.parallel_processing = False  # Future feature
        self.compression_enabled = False  # Maybe useful

    def process(self, data):
        # Only actually need this simple processing
        return [item.strip().lower() for item in data]

# Good - implement only what's needed now
class DataProcessor:
    def process(self, data: list[str]) -> list[str]:
        """Process data by stripping whitespace and converting to lowercase."""
        return [item.strip().lower() for item in data]
```

## Code Organization

### 4. Single Responsibility Principle

Each function or class should have one reason to change.

```python
# Bad - multiple responsibilities
class UserManager:
    def create_user(self, user_data):
        # Validate data
        if not user_data.get('email'):
            raise ValueError("Email required")

        # Save to database
        db.save_user(user_data)

        # Send welcome email
        email_service.send_welcome(user_data['email'])

        # Log the action
        logger.info(f"User created: {user_data['email']}")

# Good - separated responsibilities
class UserValidator:
    def validate(self, user_data: dict) -> None:
        """Validate user data."""
        if not user_data.get('email'):
            raise ValueError("Email required")

class UserRepository:
    def save(self, user_data: dict) -> None:
        """Save user to database."""
        db.save_user(user_data)

class UserNotificationService:
    def send_welcome_email(self, email: str) -> None:
        """Send welcome email to new user."""
        email_service.send_welcome(email)

class UserManager:
    def __init__(self):
        self.validator = UserValidator()
        self.repository = UserRepository()
        self.notification_service = UserNotificationService()

    def create_user(self, user_data: dict) -> None:
        """Create a new user."""
        self.validator.validate(user_data)
        self.repository.save(user_data)
        self.notification_service.send_welcome_email(user_data['email'])
        logger.info(f"User created: {user_data['email']}")
```

### 5. Write Self-Documenting Code

Choose descriptive names that explain their purpose.

```python
# Bad - unclear names
def calc(d, r):
    return d * r * 0.1

def proc_usr(u):
    if u[0] > 18:
        return True
    return False

# Good - self-documenting
def calculate_discount(price: float, discount_rate: float) -> float:
    """Calculate discount amount."""
    return price * discount_rate * 0.1

def is_adult(user_age: int) -> bool:
    """Check if user is an adult (18 or older)."""
    return user_age >= 18
```

## Error Handling

### 6. Fail Fast and Explicitly

Catch errors early and provide clear error messages.

```python
# Bad - silent failures and unclear errors
def divide_numbers(a, b):
    try:
        return a / b
    except:
        return None

def process_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        return ""

# Good - explicit error handling
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def process_file(filename: str) -> str:
    """Read and return file contents."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {filename}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"Cannot decode file: {filename}")
```

### 7. Use Context Managers

Ensure proper resource cleanup.

```python
# Bad - manual resource management
def read_config():
    file = open('config.txt')
    data = file.read()
    file.close()  # Might not execute if error occurs
    return data

# Good - automatic resource management
def read_config() -> str:
    """Read configuration from file."""
    with open('config.txt', 'r', encoding='utf-8') as file:
        return file.read()

# Custom context manager for database connections
from contextlib import contextmanager

@contextmanager
def database_connection():
    """Context manager for database connections."""
    conn = create_connection()
    try:
        yield conn
    finally:
        conn.close()

# Usage
def get_user_data(user_id: int) -> dict:
    """Get user data from database."""
    with database_connection() as conn:
        return conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

## Function Design

### 8. Keep Functions Small

Functions should do one thing well.

```python
# Bad - large function doing multiple things
def process_user_registration(user_data):
    # Validate email
    if '@' not in user_data['email']:
        raise ValueError("Invalid email")

    # Check if user exists
    existing = db.query("SELECT * FROM users WHERE email = ?", user_data['email'])
    if existing:
        raise ValueError("User already exists")

    # Hash password
    import hashlib
    hashed_password = hashlib.sha256(user_data['password'].encode()).hexdigest()

    # Save user
    db.execute("INSERT INTO users (email, password) VALUES (?, ?)",
               user_data['email'], hashed_password)

    # Send email
    send_email(user_data['email'], "Welcome!")

    # Log action
    logger.info(f"User registered: {user_data['email']}")

# Good - small, focused functions
def validate_email(email: str) -> None:
    """Validate email format."""
    if '@' not in email:
        raise ValueError("Invalid email format")

def check_user_exists(email: str) -> bool:
    """Check if user already exists."""
    existing = db.query("SELECT * FROM users WHERE email = ?", email)
    return bool(existing)

def hash_password(password: str) -> str:
    """Hash password using SHA256."""
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(email: str, hashed_password: str) -> None:
    """Save user to database."""
    db.execute("INSERT INTO users (email, password) VALUES (?, ?)",
               email, hashed_password)

def process_user_registration(user_data: dict) -> None:
    """Process user registration."""
    validate_email(user_data['email'])

    if check_user_exists(user_data['email']):
        raise ValueError("User already exists")

    hashed_password = hash_password(user_data['password'])
    save_user(user_data['email'], hashed_password)

    send_email(user_data['email'], "Welcome!")
    logger.info(f"User registered: {user_data['email']}")
```

### 9. Use Pure Functions When Possible

Functions that don't have side effects are easier to test and reason about.

```python
# Bad - function with side effects
total_processed = 0

def process_item(item):
    global total_processed
    result = item.upper()
    total_processed += 1  # Side effect
    print(f"Processed: {result}")  # Side effect
    return result

# Good - pure function
def process_item(item: str) -> str:
    """Process item by converting to uppercase."""
    return item.upper()

def process_items_with_logging(items: list[str]) -> list[str]:
    """Process items and log progress."""
    results = []
    for i, item in enumerate(items):
        result = process_item(item)
        results.append(result)
        print(f"Processed {i+1}/{len(items)}: {result}")
    return results
```

## Data Structures

### 10. Use Appropriate Data Structures

Choose the right data structure for the job.

```python
# Bad - using list for lookups
def find_user_by_id(users_list, user_id):
    for user in users_list:  # O(n) lookup
        if user['id'] == user_id:
            return user
    return None

# Good - using dictionary for O(1) lookups
def create_user_index(users: list[dict]) -> dict[int, dict]:
    """Create an index of users by ID for fast lookups."""
    return {user['id']: user for user in users}

def find_user_by_id(user_index: dict[int, dict], user_id: int) -> dict | None:
    """Find user by ID using index."""
    return user_index.get(user_id)

# Use sets for membership testing
def filter_allowed_users(users: list[str], allowed_users: set[str]) -> list[str]:
    """Filter users to only include allowed ones."""
    return [user for user in users if user in allowed_users]  # O(1) lookup
```

### 11. Prefer Immutable Data

Immutable data is safer and easier to reason about.

```python
# Bad - mutable default arguments
def add_item(item, items=[]):  # Dangerous!
    items.append(item)
    return items

# Good - immutable approach
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    """Add item to list, returning new list."""
    if items is None:
        items = []
    return items + [item]  # Return new list

# Use dataclasses with frozen=True for immutable objects
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def move(self, dx: float, dy: float) -> 'Point':
        """Return new Point moved by dx, dy."""
        return Point(self.x + dx, self.y + dy)
```

## Testing Considerations

### 12. Write Testable Code

Design code to be easy to test.

```python
# Bad - hard to test due to dependencies
def process_user_data():
    data = requests.get("https://api.example.com/users").json()
    processed = [user['name'].upper() for user in data]
    with open('output.txt', 'w') as f:
        f.write('\n'.join(processed))

# Good - testable with dependency injection
def fetch_user_data(api_client) -> list[dict]:
    """Fetch user data from API."""
    return api_client.get_users()

def process_names(users: list[dict]) -> list[str]:
    """Process user names."""
    return [user['name'].upper() for user in users]

def save_results(data: list[str], file_writer) -> None:
    """Save results using provided writer."""
    file_writer.write('\n'.join(data))

def process_user_data(api_client, file_writer) -> None:
    """Main processing function."""
    users = fetch_user_data(api_client)
    processed_names = process_names(users)
    save_results(processed_names, file_writer)
```

## Performance Considerations

### 13. Optimize When Necessary

Don't optimize prematurely, but be aware of performance implications.

```python
# Bad - premature optimization
def find_max_optimized(numbers):
    # Unnecessary complexity for most use cases
    if not numbers:
        return None
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val

# Good - use built-in functions first
def find_max(numbers: list[float]) -> float | None:
    """Find maximum value in list."""
    return max(numbers) if numbers else None

# Optimize only when profiling shows it's needed
def find_max_large_dataset(numbers: list[float]) -> float | None:
    """Optimized max finding for very large datasets."""
    if not numbers:
        return None

    # Use numpy for large datasets if available
    try:
        import numpy as np
        return float(np.max(numbers))
    except ImportError:
        return max(numbers)
```

These best practices will help you write code that is not only functional but also maintainable, readable, and robust. Remember: good code is written for humans to read, not just for computers to execute.

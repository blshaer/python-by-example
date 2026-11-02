"""
================================================================================
File: 02_type_hinting.py
Topic: Type Hints in Python
================================================================================

This file demonstrates type hints (type annotations) in Python. Type hints make
code more readable, enable better IDE support, and can catch bugs early using
static type checkers like mypy.

Key Concepts:
- Basic type hints
- typing module (List, Dict, Optional, etc.)
- Function annotations
- Class type hints
- Generics
- Type checking tools

Note: Type hints are OPTIONAL and don't affect runtime behavior!

================================================================================
"""

# =============================================================================
# 1. BASIC TYPE HINTS
# =============================================================================
# Syntax: variable: Type = value

print("--- Basic Type Hints ---")

# Simple types
name: str = "Alice"
age: int = 25
height: float = 1.75
is_active: bool = True

print(f"name: str = '{name}'")
print(f"age: int = {age}")
print(f"height: float = {height}")
print(f"is_active: bool = {is_active}")

# Type hints are just hints - they don't enforce types at runtime!
# This works but is wrong (would be caught by type checker):
# age: int = "not an int"

# =============================================================================
# 2. FUNCTION TYPE HINTS
# =============================================================================
# Parameters and return types

print("\n--- Function Type Hints ---")

def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def is_even(n: int) -> bool:
    """Check if number is even."""
    return n % 2 == 0

# Function with no return value
def print_message(message: str) -> None:
    """Print a message (returns None)."""
    print(message)

print(f"greet('World'): {greet('World')}")
print(f"add_numbers(3, 5): {add_numbers(3, 5)}")
print(f"is_even(4): {is_even(4)}")

# =============================================================================
# 3. TYPING MODULE - COLLECTION TYPES
# =============================================================================

print("\n--- Collection Types ---")

from typing import List, Dict, Set, Tuple

# Python 3.10+ prefers built-in generics: list[int], dict[str, int], set[str]
# The typing aliases below still work and appear in older examples.

# List of specific type
def process_numbers(numbers: list[int]) -> int:
    """Sum a list of integers."""
    return sum(numbers)

# Dictionary with key and value types
def get_user_ages(users: dict[str, int]) -> list[str]:
    """Get names of users older than 18."""
    return [name for name, age in users.items() if age > 18]

# Set of specific type
def get_unique_words(text: str) -> set[str]:
    """Get unique words from text."""
    return set(text.lower().split())

# Tuple with specific types (fixed length)
def get_point() -> tuple[float, float]:
    """Return an (x, y) coordinate."""
    return (1.5, 2.5)

# Tuple with variable length of same type
def get_scores() -> tuple[int, ...]:
    """Return any number of scores."""
    return (85, 90, 78, 92)

# Examples
print(f"process_numbers([1,2,3]): {process_numbers([1, 2, 3])}")
print(f"get_unique_words('hello hello world'): {get_unique_words('hello hello world')}")
print(f"get_point(): {get_point()}")

# =============================================================================
# 4. OPTIONAL AND UNION TYPES
# =============================================================================

print("\n--- Optional and Union ---")

from typing import Optional, Union

# Optional = can be None
def find_user(user_id: int) -> Optional[str]:
    """Find user by ID, return None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns None if not found

# Union = can be one of several types (3.10+ also allows int | str)
def process_input(value: int | str) -> str:
    """Process either int or string input."""
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

# Python 3.10+ syntax: X | Y instead of Union[X, Y]
# def process_input(value: int | str) -> str:

print(f"find_user(1): {find_user(1)}")
print(f"find_user(99): {find_user(99)}")
print(f"process_input(42): {process_input(42)}")
print(f"process_input('hello'): {process_input('hello')}")

# =============================================================================
# 5. SPECIAL TYPES
# =============================================================================

print("\n--- Special Types ---")

from typing import Any, Callable, Sequence, Iterable

# Any - accepts any type (avoid when possible)
def log_value(value: Any) -> None:
    """Log any value."""
    print(f"  Logged: {value}")

log_value(42)
log_value("hello")
log_value([1, 2, 3])

# Callable - function type
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    """Apply a function to two numbers."""
    return func(a, b)

print(f"\napply_function(lambda x,y: x+y, 3, 4): {apply_function(lambda x, y: x + y, 3, 4)}")

# Sequence - any ordered collection (list, tuple, str)
def get_first(items: Sequence[int]) -> int:
    """Get first item from sequence."""
    return items[0]

# Iterable - anything you can iterate over
def count_items(items: Iterable[str]) -> int:
    """Count items in iterable."""
    return sum(1 for _ in items)

# =============================================================================
# 6. TYPE ALIASES
# =============================================================================

print("\n--- Type Aliases ---")

from typing import List, Tuple

# Create readable aliases for complex types
UserId = int
Username = str
Coordinate = Tuple[float, float]
UserList = List[Dict[str, Union[str, int]]]

def get_user(user_id: UserId) -> Username:
    """Get username by ID."""
    return f"user_{user_id}"

def calculate_distance(point1: Coordinate, point2: Coordinate) -> float:
    """Calculate distance between two points."""
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

print(f"get_user(123): {get_user(123)}")
print(f"distance((0,0), (3,4)): {calculate_distance((0, 0), (3, 4))}")

# =============================================================================
# 7. CLASS TYPE HINTS
# =============================================================================

print("\n--- Class Type Hints ---")

from typing import Optional, List, ClassVar

class Person:
    """A person with type-hinted attributes."""
    
    # Class variables
    species: ClassVar[str] = "Homo sapiens"
    
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.email: Optional[str] = None
    
    def set_email(self, email: str) -> None:
        """Set the person's email."""
        self.email = email
    
    def get_info(self) -> str:
        """Get person's info."""
        return f"{self.name}, {self.age} years old"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Person":
        """Create Person from dictionary."""
        return cls(data["name"], data["age"])

person = Person("Alice", 25)
person.set_email("alice@example.com")
print(f"Person: {person.get_info()}")
print(f"Email: {person.email}")

# =============================================================================
# 8. GENERICS
# =============================================================================

print("\n--- Generics ---")

from typing import TypeVar, Generic, List

# Define a type variable
T = TypeVar('T')

# Generic function
def first_item(items: List[T]) -> T:
    """Get first item of any list type."""
    return items[0]

# Generic class
class Stack(Generic[T]):
    """A generic stack."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push item onto stack."""
        self._items.append(item)
    
    def pop(self) -> T:
        """Pop item from stack."""
        return self._items.pop()
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0

# Using generics
print(f"first_item([1, 2, 3]): {first_item([1, 2, 3])}")
print(f"first_item(['a', 'b']): {first_item(['a', 'b'])}")

stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack pop: {stack.pop()}")

# =============================================================================
# 9. LITERAL AND FINAL
# =============================================================================

print("\n--- Literal and Final ---")

from typing import Literal, Final

# Literal - exact values only
Mode = Literal["r", "w", "a"]

def open_file(path: str, mode: Mode) -> str:
    """Open file with specific mode."""
    return f"Opening {path} in mode '{mode}'"

print(open_file("data.txt", "r"))
# open_file("data.txt", "x")  # Type error! "x" is not allowed

# Final - cannot be reassigned
MAX_SIZE: Final[int] = 100
# MAX_SIZE = 200  # Type checker would flag this

print(f"MAX_SIZE (Final): {MAX_SIZE}")

# =============================================================================
# 10. TYPE CHECKING TOOLS
# =============================================================================

print("\n--- Type Checking ---")

print("""
Type hints are NOT enforced at runtime!
Use these tools to check types statically:

1. mypy - The most popular type checker
   pip install mypy
   mypy your_script.py

2. pyright - Microsoft's type checker (fast)
   pip install pyright
   pyright your_script.py

3. IDE Support
   - VS Code with Pylance
   - PyCharm (built-in)

Example mypy output:
  error: Argument 1 to "greet" has incompatible type "int"; expected "str"
  
Benefits of type hints:
  ✓ Catch bugs early (before runtime)
  ✓ Better IDE autocomplete
  ✓ Self-documenting code
  ✓ Easier refactoring
  ✓ Better code reviews
""")

# =============================================================================
# 11. BEST PRACTICES
# =============================================================================

print("--- Best Practices ---")

print("""
1. Start with function signatures
   - Hint parameters and return types first

2. Use Optional[X] for nullable values
   - Not: x: str = None (wrong type!)
   - Yes: x: Optional[str] = None

3. Prefer specific types over Any
   - Any defeats the purpose of type hints

4. Use type aliases for complex types
   - Makes code more readable

5. Enable strict mode in mypy
   - mypy --strict your_script.py

6. Type hint public APIs first
   - Internal code can be less strict

7. Use TypedDict for dictionaries with known structure
   
8. Consider using dataclasses for structured data
""")

# Example: TypedDict and dataclass
from typing import TypedDict
from dataclasses import dataclass

class UserDict(TypedDict):
    """User data as dictionary."""
    name: str
    age: int
    email: Optional[str]

@dataclass
class UserDataClass:
    """User data as dataclass."""
    name: str
    age: int
    email: Optional[str] = None

# Both provide type safety for structured data
user_dict: UserDict = {"name": "Alice", "age": 25, "email": None}
user_obj = UserDataClass(name="Bob", age=30)

print(f"\nTypedDict: {user_dict}")
print(f"Dataclass: {user_obj}")

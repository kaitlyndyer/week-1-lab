"""
WEEK 1 LECTURE 2: TYPING, TESTING & DEBUGGING

SUMMARY:
Functions:
- Parameters: defaults, *args (arbitrary arguements)
- Keyword arguments
- Docstrings
- if __name__ = "__main__"

Built-in Functions & Methods:
- range() - generate squences
- sum() - sum values
- len() - get length
- input() - get user input
- print() - output
- .isdigit() - check if character is digit
- .isupper() - check if character is uppercase

Testing:
- pytest framework
- assert statements
- Test function naming (test_*)

Type Annotations:
- Basic: int, float, bool, str
- collections: list[T], dic[K, V], tuple, set
- Union types: int | str
- Generics: def func[T](items: list[T]) -> T

Development Tools:
- ruff: linting and formatting
- ty: type checking
- VS Code debugger

Control Flow:
- if/elif/else statements
- while loops (unknown iterations)
- for loops (known iterations)
- break and continue
- Gaurd clause pattern
"""
# FUNCTIONS
# Default parameters (must be rightmost)
def area(width: int, height: int = 3) -> int:
    """calculate rectangle area"""
    return width * height

print(area(2))                 # 6
print(area(4, 4))              # 16
print(area(height=1, width=9)) # 9

def average(*numbers: int) -> float:
    """calculate average of any number of values"""
    return sum(numbers) / len(numbers)

print(average(12, 45, 15, 22)) # 23.5
# IF __NAME__ == "__MAIN__"
# Run code only when executed directly (not when imported)
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

# TESTING WITH PYTEST
# Run: uv run pytest filename.py
# Test functions must start with "test_"
def inc(x: int) -> int:
    return x + 1

def test_inc():
    assert inc(3) == 4
    assert inc(0) == 1

# TYPE ANNOTATIONS
# Basic types
x: int = 1
y: float = 1.0
z: bool = True
name: str = "test"

# Collections
numbers: list[int] = [1, 2, 3]
grades: dict[str, float] = {"math": 95.5}
point: tuple[int, str, float] = (3, "yes", 7.5)

# Union types (use | operator)
mixed: list[int | str] = [3, 5, "hello", "world"]
optional: str | None = "something"

# Any type (must import)
from typing import Any
unknown: Any = "anything"

# Function annotations
def add(a: int, b: int) -> int:
    return a + b

def say_hello() -> None: # Returns nothing
    print("Hello!")

# Generics (T = type variable)
def first[T](items: list[T]) -> T:
    return items[0]

# TOOLS

# CONTROL FLOW: IF STATEMENTS

# CONTROL FLOW: LOOPS

# DEBUGGER (VS CODE)

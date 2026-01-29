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
# Ruff linter: uv run ruff check filename.py --fix
# Ruff formatter: uv run ruff formate filename.py
# Type checker: uv run ty check

# CONTROL FLOW: IF STATEMENTS
# single selction
if x > 10:
    print("Greater than 10")

# chained comparisons
if 1 <= x <= 5:
    print("Between 1 and 5")

# double selection
grade = 50
if grade >= 50:
    print("pass")
else: 
    print("Fail")

# multiple selection
mark = 61
if mark >= 72:
    print("Distinction")
elif mark >= 62:
    print("Merit")
else:
    print("Pass or Fail")

# guard clause pattern (avoid nested ifs)
def grade(mark: int) -> str:
    if mark >= 72:
        return "Distinction"
    if mark >= 62:
        return "Merit"
    if mark >= 52:
        return "Pass"
    return "Fail"

# CONTROL FLOW: LOOPS
# While loop (unknown iterations)
i = 10
while i > 0:
    print(i)
    i -= 1

# Infinite loop with break
while True:
    choice = input("Exit? (y/n): ")
    if choice == "y":
        break

# For loop (known iterations)
for char in "Python":
    print(char)

for x in range(5):
    print(x)

# continue: skip current iteration
# break: exit loop entirely

# DEBUGGER (VS CODE)
"""
SETUP: Click line number for breakpoint (red dot)
START: "Python Debugger: Debug Python File" or ⇧⌘D

Controls:
- Continue: Run until next breakpoint
- Step Over: Execute line (don't enter functions)
- Step into: Execute and enter functions
- Step Out: retur to outer function
- Restart/Stop: Restart or exit debugger
"""

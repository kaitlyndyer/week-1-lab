# ===================================================
# SEQUENCES IN PYTHON
# ===================================================

# a sequence groups multiple values in a specific order
# examples:
# - letters in a string
# - items in a shopping list

# common Python squence types:
# - lists
# - tuples
# - strings

# ===================================================
# LISTS:
# ===================================================

# Mutable -> contents can change
# Writen using square brackets []

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Length of a List:
print(len(rainbow))  # 7

# INDEXING (indexes start at 0):
print(rainbow[0])  # 'red'
print(rainbow[1 + 2])  # 'green'

# NEGATIVE INDEXING:
print(rainbow[-1])  # 'violet'
print(rainbow[-2])  # 'indigo'

# ===================================================
# Lists can contain mixed types and nested lists:
# ===================================================

matrix = [[1, 2, 3], [4, 5, 6]]

print(matrix[0])  # [1, 2, 3]
print(matrix[0][1])  # 2

# ===================================================
# TUPLES:
# ===================================================

# immutable -> cannot be changed after creation
# written using parenthese ()

user = (5566, "hello@email.com")

# Immutability Example
# user[0] = 5567  -> TypeError: 'tuple' object does not support item assignment

# Memory comparison
[1, 2, 3].__sizeof__()  # 72
(1, 2, 3).__sizeof__()  # 48

# Typical use case: list of tuples (records)
users = [
    (5566, "hello@email.com"),
    (5567, "example@gmail.com"),
    (5568, "hello@nulondon.ac.uk"),
]

# ===================================================
# INDEXING WORKS ON LISTS, TUPLES, AND STRINGS
# ===================================================

# Access tems using square brackets
# strings support indexing and slicing too
print(rainbow[0])  # 'red'
print("Hello"[1])  # 'e'

# ===================================================
# SLICING
# ===================================================

# Format: start:end:step
# End index is exclusive

print(rainbow[1:4])  # ['orange', 'yellow', 'green']
print(rainbow[5:])  # ['indigo', 'violet']
print(rainbow[:3])  # ['red', 'orange', 'yellow']

# Step arguement
print(rainbow[::2])  # ['red', 'yellow', 'blue', 'violet']

# Reverse a sequence
print(rainbow[::-1])  # reversed list

# ===================================================
# CONCATENATION
# ===================================================

more_colors = ["plum", "maroon"]
big_rainbow = rainbow + more_colors

# ===================================================
# INSERTING, MODIFYING, AND DELETING LIST ITEMS
# ===================================================

breakfast = []

# append
breakfast.append("tea")
breakfast.append("cereal")

# modify
breakfast[0] = "coffee"

# insert at index
breakfast.insert(1, "banana")
print(breakfast)

# delete
del breakfast[-1]
print(breakfast)

# ===================================================
# SEARCHING AND MEMBERSHIP
# ===================================================

alphabet = ["bee", "apple", "dog", "car"]

print(alphabet.index("car"))  # 3

# membership operators
print("apple" in alphabet)  # True
print("elephant" not in alphabet)  # True

# ===================================================
# SORTING
# ===================================================

# list.sort() modifies the original list
alphabet.sort()
print(alphabet)  # ['apple', 'bee', 'car', 'dog']

alphabet.sort(reverse=True)
print(alphabet)  # ['dog', 'car', 'bee', 'apple']

# sorted() returns a NEW list
original = ["bee", "apple", "dog", "car"]
new_list = sorted(original)

print(original)  # unchanged
print(new_list)  # sorted list

# sorting tuples using a key
sorted(users, key=lambda x: x[1])

# ===================================================
# BUTLT-IN SEQUENCE FUNCTIONS
# ===================================================

print(all([False, True, False]))  # False
print(any([False, True, False]))  # True

print(sum([1, 2, 3, 4]))  # 10

print(min([3, 4, 6, 12, 5]))  # 3
print(max([3, 4, 6, 12, 5]))  # 12

print(min(["bee", "apple", "dog", "car"]))  # 'apple'
print(max(["bee", "apple", "dog", "car"]))  # 'dog'

# example calculations
marks = [82, 75, 82, 85, 62]
average_mark = sum(marks) / len(marks)
print(average_mark)
marks_range = max(marks) - min(marks)
print(marks_range)

# ===================================================
# ITERATION
# ===================================================

# for loop over a list
for n in [1, 2, 3]:
    print(n**2)

# for loop over a string
for c in "Hello World":
    print(c)

# ===================================================
# RANGE
# ===================================================

# range(start, stop)
for n in range(1, 4):
    print(n**2)

# range(start, stop, step)
for n in range(10, 20, 2):
    print(n)

# ===================================================
# LIST COMPREHENSIONS
# ===================================================

# transforming a list
y = [1, 2, 3, 4]
y_doubled = [x * 2 for x in y]
print(y_doubled)

# equivalent for-loop
y_doubled = []
for x in y:
    y_doubled.append(x * 2)
print(y_doubled)

# with condition
y = [9, 10, 6, 12, 15]
print([x for x in y if x > 10])  # [12, 15]

# ===================================================
# UNPACKING
# ===================================================

user = (5566, "hello@email.com")
profile_id, email = user
print(email)

# ===================================================
# ENUMERATE
# ===================================================

seasons = ["Spring", "Summer", "Autumn", "Winter"]
list(enumerate(seasons))

for idx, x in enumerate(["a", "b", "c"]):
    print(f"index {idx}")
    print(f"item {x}\n")

# ===================================================
# ZIP
# ===================================================

for item in zip(["A", "B", "C"], ["sugar", "spice", "everything nice"]):
    print(item)

# zip stops at the shortest sequence
for item in zip(range(3), ["fee", "fi", "fo", "fum"]):
    print(item)

# strict=True raises an error if lengths differ
# zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True)

# ===================================================
# FILTER AND MAP
# ===================================================

numbers = [1, 2, 3, 4, 5, 6]

# filter()
print(list(filter(lambda x: x % 2 == 0, numbers)))  # [2, 4, 6]

# map()
print(list(map(lambda x: x**2, numbers)))
strings = ["hello", "world"]
print(list(map(str.upper, strings)))

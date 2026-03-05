# CLASS EXERCISES

# sets
# given this list of student ids convert it to a set to remove duplicates and find the unique students. print how many unique students there are
student_ids = [101, 102, 103, 101, 104, 102, 105, 103]

unique_ids = set(student_ids)
print(len(unique_ids))

# two classes have the following students:
class_a = {"Angus", "Bubbles", "Chester", "Daisy"}
class_b = {"Chester", "Daisy", "Eve", "Frita"}

# Find:
# 1. students in both classes
print(class_a & class_b)

# 2. students in either class (union)
print(class_a | class_b)

# 3. students only in class_a (difference)
print(class_a - class_b)

# 4. students in only one class (symmetric difference)
print(class_a ^ class_b)


# dictionaries
# create a new dictionary with only students who scored above 75 using a dictionary comprehension
scores = {"Angus": 85, "Bubbles": 92, "Chester": 78, "Daisy": 95, "Eve": 88}
high_scores = {k: v for k, v in scores.items() if v > 75}
print(high_scores)


# create a dictionary that counts how may times each letter appears in the word "hello"
def count_char(word: str) -> dict[str, int]:
    count = {}
    for char in word:
        count[char] = count.get(char, 0) + 1
    return count


print(count_char("hello"))

# create a program that tracks inventory for a small shop. start with this dictionary:
inventory = {"apples": 50, "bananas": 30, "oranges": 45, "pears": 20}

# complete the following tasks:
# 1. add a new item 'grapes' with quantity 35
inventory["grapes"] = 35
print(inventory.get("grapes"))

# 2. a customer buys 10 apples - update the inventory
inventory["apples"] -= 10
print(inventory["apples"])

# 3. check if 'mangoes' are in stock using the in operator
print("mangoes" in inventory)

# 4. print all items with quantity less than 25
for item, cost in inventory.items():
    if cost < 25:
        print(f"{item}: ${cost}")

# create a new dictionary using comprehension that applies a 10% restock to all items (multiply by 1.1)
restock = {item: cost * 1.1 for item, cost in inventory.items()}
print(restock)
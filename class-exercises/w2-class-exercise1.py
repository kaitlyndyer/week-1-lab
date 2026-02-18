# CLASS EXERCISES

# lists
# given a list of student grades, calculate statistics:
grades = [78, 85, 92, 68, 95, 88, 73, 90, 82, 87]

# 1. find the highest and lowest grades
print(max(grades)) # 95
print(min(grades)) # 68

# 2. calculate the average grade
print(sum(grades) / len(grades)) # 83.8

# 3. count how many students scored above 80
len_grades = list(filter(lambda x: x > 80, grades))

print(len(len_grades)) # 7

# 4. create a new list with only grades aove 85
high_grades = []
for x in grades:
    if x > 85:
        high_grades.append(x)

print(high_grades)

# 5. sort the grades in descending order
print(sorted(grades, reverse=True))


# list comprehensions
#use list comprehensions to solve these problems:

# 1. create a list of squares for numbers 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2. from the following list, create a list of words with more than 5 letters
words = ["apple", "banana", "kiwi", "strawberry", "grape"]
long = []
for w in words:
    if len(w) > 5:
        long.append(w)

print(long)

# 3. given the temperatures in the following list, create a list with temperatures in Fahrenheit
temperatures = [23, 18, 32, 15, 28, 20]
fahrenheit = [c * 9/5 + 32 for c in temperatures]
print(fahrenheit)

# tuples
# work with user information stored as tuples:
users = [
    (101, "barold@email.com", "Barold"),
    (102, "cleo@email.com", "Cleo"),
    (103, "kabuki@email.com", "Kabuki")
]

# 1. print each user's name and email using a for loop
for id, email, name in users:
    print(f'{name}: {email}')

# 2. find the user with ID 102
for user in users:
    if user[0] == 102:
        print(user)
    
# 3. add a new user (104, "maddie@email.com", "Maddie")
users.append((104, "maddie@email.com", "Maddie"))
print(users[3])

# 4. create a list of just email addresses by unpacking each tuple in a loop or list comprehension
emails = []
for id, email, name in users:
    emails.append(email)
print(emails)


# zip and enumerate
# you have two lists representing products and their prices:
products = ["laptop", "mouse", "keyboard", "monitor"]
prices = [899, 25, 75, 350]

# 1. use zip() to create a list of tuples pairing each product with its price
items = list(zip(products, prices))
print(items)

# 2. use enumerate() to print each product with its position number (starting from 1)
for index, product in enumerate(items, start=1):
    print(f'{index}. {product}')

# 3. find the most expensive product using max() with a lambda function
most_expensive = max(items, key=lambda x: x[1])
print(f'The most expensive product is: {most_expensive}')

# 4. Create a new list with a 10% discount applied to all prices using map()
discount = list(map(lambda x: x[1] * 0.9, items))
print(discount)

# 5. filter and show only products that cost more than 50
high_prices = list(filter(lambda x: x[1] > 50, items))
print(high_prices)


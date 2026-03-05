from collections.abc import Iterable

# CLASS EXERCISES
# low to high
# write a recursive function a start_to_end that accepts a start and end parameter and prints out the number in that range:
def start_to_end(s, e):
    if s > e:
        return
    print(s)
    start_to_end(s + 1, e)

start_to_end(1, 3)
# 1
# 2
# 3


# list flattening
# flatten a nested list [[1, 2], [3, [4, 5]], 6] -> [1, 2, 3, 4, 5, 6]
# - check if first element is a list
# - if yes, flatten it and concatenate with rest
# - if no, add it to flattened rest
def flatten(l):
    if not l:
        return []
    
    f = l[0]
    r = flatten(l[1:])

    if isinstance(f, Iterable):
        return flatten(list(f)) + r
    else:
        return [f] + r

example = flatten([[1, 2], [3, [4, 5]], 6])
print(example)  

# coin combinations
# write a recursive function ways(amount) that returns how many different combinations of 1p, 2p, and 5p coins make up a given amount
# for example, there are 9 ways to make 5p: 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1, 5
def ways(amount):
    global call_count
    call_count += 1
    
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    return ways(amount - 1) + ways(amount - 2) + ways(amount - 5)

print(ways(5))


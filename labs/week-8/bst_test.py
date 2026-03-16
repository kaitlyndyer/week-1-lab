from bst import BinarySearchTree

bst = BinarySearchTree()
for word in ["piano", "crane", "stove", "apple", "zebra", "mango", "flute"]:
    bst.insert(word)

# TESTING: _to_list
print(bst.to_list())


# TESTING: _range_query
print(bst.range_query("crane", "stove"))
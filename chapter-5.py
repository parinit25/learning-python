# ----------------------------
# Python Dictionaries (Hash Maps)
# ----------------------------

# Dictionaries are mutable mappings of unique keys to values.
person = {"name": "Parinit", "age": 25, "city": "Bangalore"}
print("Original dict:", person)  
# → {'name': 'Parinit', 'age': 25, 'city': 'Bangalore'}

# 1. Length
print("1. Length of dict:", len(person))  
# → 3

# 2. Accessing values
print("2. Accessing values")
print("Name:", person["name"])               # direct access (KeyError if missing)
print("Age:", person.get("age"))             # safe access (returns None if missing)
print("Country:", person.get("country", "India"))  # default if key not found
print()

# 3. Checking for keys
print("3. Key membership")
print("'city' in person?", "city" in person)       # True
print("'email' in person?", "email" in person)     # False 
print()

# 4. Adding or updating entries
print("4. Adding/updating entries")
person["email"] = "parinit@example.com"     # add new key
person["age"] = 26                          # update existing key
print(person)
# → {'name': 'Parinit', 'age': 26, 'city': 'Bangalore', 'email': 'parinit@example.com'}
print()

# 5. Removing entries
print("5. Removing entries")
removed_email = person.pop("email")         # removes and returns the value
print("Removed email:", removed_email)
last_item = person.popitem()                # removes and returns (key, value) of last insert
print("popitem():", last_item)
print("After removals:", person)
# To clear everything: person.clear()
print()

# 6. Iterating over a dict
person = {"name": "Parinit", "age": 26, "city": "Bangalore"}
print("6. Iteration")
print("Keys only:")
for key in person:
    print(key, "->", person[key])
print("\nKey–value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
print()

# 7. Common dict methods
print("7. Dict views & methods")
print("Keys view:", list(person.keys()))      # ['name', 'age', 'city']
print("Values view:", list(person.values()))  # ['Parinit', 26, 'Bangalore']
print("Items view:", list(person.items()))    # [('name','Parinit'),('age',26),('city','Bangalore')]

# update() merges another dict (overwrites existing keys)
person.update({"age": 27, "country": "India"})
print("After update():", person)
# shallow copy
copy_person = person.copy()
print("Shallow copy:", copy_person)
print()

# 8. fromkeys() — create new dict from a sequence of keys
print("8. fromkeys()")
keys_list = ["a", "b", "c"]
zeros = dict.fromkeys(keys_list, 0)
print("fromkeys:", zeros)
# → {'a': 0, 'b': 0, 'c': 0}
print()

# 9. Nested dictionaries
print("9. Nested dicts")
students = {
    "Alice": {"math": 85, "english": 78},
    "Bob":   {"math": 90, "english": 82},
}
print("Alice's math score:", students["Alice"]["math"])
# → 85
print()

# 10. Dictionary comprehensions
print("10. Dict comprehensions")
squares = {x: x*x for x in range(1, 6)}
print("Squares:", squares)
# → {1:1, 2:4, 3:9, 4:16, 5:25}
print()

# 11. Merging dicts (Python 3.5+)
print("11. Merging dicts")
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}   # d2’s 'b' overwrites d1’s
print("Merged:", merged)
# → {'a': 1, 'b': 3, 'c': 4}
print()





# ----------------------------
# Python Sets (Unordered, Unique Collections)
# ----------------------------







# 1. Creating sets
empty_set = set()            # correct way to make an empty set
empty_dict = {}              # this makes an empty dict, NOT a set!

numbers = {1, 2, 3, 4, 5}    # literal syntax for a non-empty set
print("numbers:", numbers, type(numbers))
# → numbers: {1, 2, 3, 4, 5} <class 'set'>
print()

# 2. Adding and removing elements
numbers.add(6)               # add a single element
print("After add(6):", numbers)

numbers.update([7, 8, 9])    # add multiple elements at once
print("After update([7,8,9]):", numbers)

numbers.discard(3)           # remove 3 if present (no error if missing)
print("After discard(3):", numbers)

removed = numbers.pop()      # remove and return an arbitrary element
print("Popped element:", removed)
print("Remaining:", numbers)

# numbers.remove(10)         # would raise KeyError if 10 not in set
print()

# 3. Membership test
print("Is 5 in numbers?", 5 in numbers)
print("Is 100 in numbers?", 100 in numbers)
print()

# 4. Common set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("a:", a)
print("b:", b)

print("Union (a ∪ b):", a | b)              # {1,2,3,4,5,6}
print("Intersection (a ∩ b):", a & b)       # {3,4}
print("Difference (a – b):", a - b)         # {1,2}
print("Difference (b – a):", b - a)         # {5,6}
print("Symmetric Difference:", a ^ b)       # {1,2,5,6}
print()

# 5. Iterating over a set
print("Iterating through 'a':")
for elem in a:
    print(elem, end=" ")
print("\n")

# 6. Set comprehensions
squares = {x * x for x in range(1, 6)}
print("Set comprehension (squares 1–5):", squares)
# → {1, 4, 9, 16, 25}
print()

# 7. Other useful methods
print("Size of a:", len(a))                   # 4
print("Minimum:", min(a), "Maximum:", max(a))
print("Sum:", sum(a))

copy_of_a = a.copy()                          # shallow copy
print("Copy of a:", copy_of_a)

a.clear()                                     # remove all elements
print("After clear(), a:", a)
print()

# 8. Immutable sets: frozenset
fs = frozenset([1, 2, 3, 2])
print("frozenset:", fs, type(fs))
# fs.add(4)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'

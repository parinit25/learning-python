# ----------------------------
# Python Lists (Dynamic Arrays)
# ----------------------------

# Lists are mutable sequences—you can change, add, or remove elements.
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)            # [10, 20, 30, 40, 50]

# 1. Length
print("Length:", len(numbers))              # 5

# 2. Indexing & assignment
print("First item:", numbers[0])            # 10
numbers[2] = 99                             # change element at index 2
print("After assignment:", numbers)         # [10, 20, 99, 40, 50]

# 3. Slicing
print("Slice [1:4]:", numbers[1:4])         # [20, 99, 40]
print("Slice [:3]:", numbers[:3])           # [10, 20, 99]
print("Slice [2:]:", numbers[2:])           # [99, 40, 50]
print("Skip [::2]:", numbers[::2])          # [10, 99, 50]

# 4. Adding elements
numbers.append(60)                          # add to end
print("Append 60:", numbers)                # [10, 20, 99, 40, 50, 60]
numbers.insert(1, 15)                       # insert 15 at index 1
print("Insert 15 at idx1:", numbers)        # [10, 15, 20, 99, 40, 50, 60]
numbers.extend([70, 80])                    # extend by another list
print("Extend [70,80]:", numbers)           # [10, 15, 20, 99, 40, 50, 60, 70, 80]

# 5. Removing elements
numbers.remove(99)                          # remove first occurrence of 99
print("Remove 99:", numbers)                # [10, 15, 20, 40, 50, 60, 70, 80]
popped = numbers.pop()                      # pop last element
print("Popped:", popped, "Remaining:", numbers)
numbers.pop(2)                              # pop item at index 2
print("Pop idx2:", numbers)

# 6. Other useful methods
print("Index of 50:", numbers.index(50))    # index of 50
print("Count of 10:", numbers.count(10))    # how many times 10 appears
numbers.reverse()                           # reverse in place
print("Reversed:", numbers)
numbers.sort()                              # sort in place
print("Sorted:", numbers)
copy_of_numbers = numbers.copy()            # shallow copy
print("Copy:", copy_of_numbers)

print("\n" + "-"*50 + "\n")

# ----------------------------
# Python Tuples (Immutable Sequences)
# ----------------------------

# Tuples cannot be changed after creation.
coords = (3, 5, 7, 9)
print("Original tuple:", coords)            # (3, 5, 7, 9)

# 1. Length
print("Length:", len(coords))               # 4

# 2. Indexing & slicing
print("First item:", coords[0])             # 3
# coords[1] = 10  # ❌ TypeError: 'tuple' object does not support item assignment
print("Slice [1:3]:", coords[1:3])          # (5, 7)
print("Skip [::2]:", coords[::2])           # (3, 7)

# 3. Tuple-specific methods
print("Index of 9:", coords.index(9))       # 3
print("Count of 5:", coords.count(5))       # 1

# 4. Packing & Unpacking
# Packing:
point =  (1, 2, 3)
# Unpacking:
x, y, z = point
print("Unpacked:", x, y, z)                 # 1 2 3

# 5. Singleton tuples
single = (42,)                              # note the trailing comma
print("Single-element tuple:", single, type(single))

# 6. Converting between list and tuple
as_list = list(coords)
print("As list:", as_list)                  # [3, 5, 7, 9]
back_to_tuple = tuple(as_list)
print("Back to tuple:", back_to_tuple)      # (3, 5, 7, 9)

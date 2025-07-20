# ----------------------------
# Python Strings Overview
# ----------------------------

# Strings are immutable: you cannot change individual characters in place.
name = "Parinit"
# name[0] = "p"  # ❌ TypeError: 'str' object does not support item assignment

# 1. Length of a string
print("1. Length")
print(len(name))  # 7
print()

# 2. Indexing
print("2. Indexing")
print(name[0], name[3], name[-1])  # 'P' 'i' 't'
print()

# 3. Slicing
#    name[start:stop] — extracts from start up to (but not including) stop
print("3. Basic slicing")
print(name[0:4])   # 'Pari'
print(name[:4])    # same as name[0:4]
print(name[3:])    # from index 3 to end: 'init'
print(name[:])     # the whole string: 'Parinit'
print()

# 4. Negative slicing
print("4. Negative slicing")
print(name[-4:-1]) # indices -4,-3,-2 → 'ini'
print(name[-3:])   # last three chars: 'nit'
print()

# 5. Skipping with slice steps
alphabets = "abcdefghijklmnopqrstuvwxyz"
skip = alphabets[0:26:2]  # every 2nd letter
print("5. Skipping in slices")
print(skip)            # 'acegikmoqsuwy'
print(len(skip))       # 13
print()

# ----------------------------
# Common String Methods
# ----------------------------
s = "  hello, World! Welcome to Python.  "

print("6. Case conversions")
print(s.upper())       # '  HELLO, WORLD! WELCOME TO PYTHON.  '
print(s.lower())       # '  hello, world! welcome to python.  '
print(s.capitalize())  # '  hello, world! welcome to python.  '
print(s.title())       # '  Hello, World! Welcome To Python.  '
print(s.swapcase())    # '  HELLO, wORLD! wELCOME TO pYTHON.  '
print()

print("7. Searching & counting")
print(s.count("o"))    # count occurrences of 'o': 5
print(s.find("World")) # index of first 'World': 8
print(s.find("x"))     # -1 if not found
# .index works like find but raises ValueError if not found
# print(s.index("x"))  # ValueError
print()

print("8. Checking start/end")
print(s.startswith("  hello"))   # True
print(s.endswith("Python.  "))   # True
print()

print("9. Stripping whitespace")
print(f"'{s.strip()}'")           # removes leading/trailing spaces
print(f"'{s.lstrip()}'")          # left only
print(f"'{s.rstrip()}'")          # right only
print()

print("10. Splitting & joining")
words = s.strip().split()         # split on whitespace
print(words)                      # ['hello,', 'World!', 'Welcome', 'to', 'Python.']
rejoined = "_".join(words)
print(rejoined)                   # 'hello,_World!_Welcome_to_Python.'
print()

print("11. Replacing substrings")
print(s.replace("Python", "JS"))  # '  hello, World! Welcome to JS.  '
print()

print("12. Formatting")
# old‑style %
print("Hello, %s! You have %d messages." % ("Alice", 5))
# str.format()
print("Hello, {}! Today is {}.".format("Bob", "Sunday"))
# f‑strings (Python 3.6+)
name2 = "Carol"
count = 3
print(f"Hi, {name2}! You have {count*2} tasks.")

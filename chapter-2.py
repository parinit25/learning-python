# Variables and data-types

# a = 1                # a is an integer
# b = 5.22             # b is a floating point number
# c ="Parinit"         # c is a string
# d= True              # d is a boolean variable
# e = None             # e is a none type variable

#----------------------------------
# Rules for defining variable names
#----------------------------------

# 1. A variable name can contain alphabets, digits and underscores.
# 2. Variable name can only start with alphabets and underscore.
# 3. A variable name can't start with a digit.
# 4. No white space is allowed in a variable name.

# Examples of some variable names are :

# parinit, one8 , _parinit , etc.

#---------------------------------
# Operators in Python
#---------------------------------

# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison oprators: ==, >, >=, <, != etc. 
# 4. Logical operators: and, or, not.

#---------------------------------
# Type() function and TYPECASTING
#---------------------------------

a = 31 # type = <class 'int'>
print(type(a))

b = 'Parinit'
print(type(b)) # <class 'str'>

c = 31.2
print(type(c)) # <class 'float'>

d = False
print(type(d)) # <class 'bool'>

e = None
print(type(e)) # <class 'NoneType'>


# There are also functions like int() float() and str()
# that are used to convert the types required that the
# conversion is legal

a = "31.2"
b = float(a)
print(type(b)) # <class 'float'>


# ----------------
# Input function
# ----------------


# By default input function takes string as input so to perform mathematical operations
# we need to convert them to int by using the conversion functions like int(), float(0)

a = int(input("Enter number 1"))
b = int(input("Enter number 2")) 
c = a + b
print("Sum is",c," Number 1 is:",a," Number 2 is:",b)
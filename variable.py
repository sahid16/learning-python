# Python Fundamentals: Comprehensive Notes and Code Explanation

# 1. Variable Declaration
# Variables are containers for data. They can store various data types.
name = "sahid"          # String: A sequence of characters.
age = 21                # Integer: Whole numbers without decimals.
book_price = 10.00      # Float: Numbers with decimal points.
price = False           # Boolean: Represents True or False values.
true_price = None       # NoneType: Represents the absence of value (null).

# Assigning the value of one variable to another
age2 = age  # The value of 'age' is copied to 'age2'.

# 2. Printing Values
# The `print()` function is used to display output in the console.
print("my name is:", name)                      # Output: my name is: sahid
print("my age is:", age2)                       # Output: my age is: 21
print("note book price is:", book_price)        # Output: note book price is: 10.0
print("notebook is 1rs true or false:", price)  # Output: notebook is 1rs true or false: False
print(true_price)                               # Output: None

# 3. Arithmetic Operations
# Python supports common mathematical operations like addition, subtraction, multiplication, etc.
a = 10
b = 5
print(a + b)  # Adds 'a' and 'b'. Output: 15

# Another way to perform addition
a = 20
b = 20
sum = b + a
print(sum)  # Output: 40

# 4. String Manipulation with Arithmetic
# Python allows creative operations with strings using arithmetic operators like *.

# Strings and numeric values can interact with '*'
a, b = 2, 3
c = a + b  # Addition of numbers.
text = "@"
print(a * text * b)  # Repeats '@' in sequence. Output: @@@@@@

# Strings can be concatenated and repeated
a, b = "2", 3
txt = "@"
print((a + txt) * b)  # Combines and repeats. Output: 2@2@2@

# 5. Arithmetic with Numbers
# Numbers can be used with all arithmetic operators like +, -, *, /, etc.
a, b, c = 5, 5, 5
print(a + b + c)  # Adds three values. Output: 15

# Arithmetic involving integers and floats results in a float.
a, b = 10, 5.0
c = a * b  # Multiplies an integer and a float.
print(c)  # Output: 50.0

# 6. Division Operations
# Regular division '/' always results in a float.
a, b = 1, 2
c = a / b
print(c)  # Output: 0.5

# Floor division '//' truncates the decimal part and returns an integer-like float.
a, b = 1.5, 3
c = a // b
print(c, a / b)  # Output: 0.0 (floor division) and 0.5 (regular division).

# 7. Floor Division Examples
# Floor division provides the closest integer that is less than or equal to the result.
A, B = 12, 5
C = A // B
print(C)  # Output: 2

# Floor division with negative values
a, b = -12, 5
c = a // b
print(c)  # Output: -3

a, b = 12, -5
c = a // b
print(c)  # Output: -3

# 8. Modulo (Remainder) Operation
# Modulo '%' returns the remainder of a division operation.
a, b = -5, 2
c = a % b
print(c)  # Output: 1 (remainder is positive).

a, b = 5, 2
c = a % b
print(c)  # Output: 1.

a, b = 5, -2
c = a % b
print(c)  # Output: -1 (remainder matches the sign of the divisor).

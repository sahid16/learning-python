# Python Operators: Comprehensive Notes

# Introduction:
# An operator is a symbol that performs a specific operation between operands (e.g., addition, comparison).
# Let's explore the main types of operators in Python with examples.

# ---------------------------------------------
# 1. Arithmetic Operators
# Perform mathematical calculations between operands.

a = 12
b = 5

print("Addition:", a + b)          # Adds a and b
print("Subtraction:", a - b)       # Subtracts b from a
print("Multiplication:", a * b)    # Multiplies a and b
print("Division:", a / b)          # Divides a by b (float result)
print("Floor Division:", a // b)   # Divides a by b (integer result)
print("Modulus:", a % b)           # Finds the remainder of a divided by b
print("Exponentiation:", a ** b)   # Raises a to the power of b

# ---------------------------------------------
# 2. Relational / Comparison Operators
# Compare values and return a boolean result (True or False).

x = 15
y = 20

print("Equal to:", x == y)         # Checks if x is equal to y
print("Not equal to:", x != y)     # Checks if x is not equal to y
print("Greater than:", x > y)      # Checks if x is greater than y
print("Less than:", x < y)         # Checks if x is less than y
print("Greater than or equal to:", x >= y)  # Checks if x is greater or equal to y
print("Less than or equal to:", x <= y)     # Checks if x is less or equal to y

# ---------------------------------------------
# 3. Assignment Operators
# Assign values to variables with or without modifying them.

z = 10  # Assigns the value 10 to z
z += 5  # Adds 5 to z (z = z + 5)
print("After += operation:", z)

z -= 3  # Subtracts 3 from z (z = z - 3)
print("After -= operation:", z)

z *= 2  # Multiplies z by 2 (z = z * 2)
print("After *= operation:", z)

z /= 4  # Divides z by 4 (z = z / 4)
print("After /= operation:", z)

z %= 3  # Modulus operation (z = z % 3)
print("After %= operation:", z)

z **= 2  # Exponentiation (z = z ** 2)
print("After **= operation:", z)

# ---------------------------------------------
# 4. Logical Operators
# Combine conditional statements to evaluate logic.

a = True
b = False

print("Logical AND (a and b):", a and b)  # Returns True if both a and b are True
print("Logical OR (a or b):", a or b)    # Returns True if either a or b is True
print("Logical NOT (not a):", not a)     # Reverses the logical state of a

# Example: Combining conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

# ---------------------------------------------
# Best Practices
"""
1. Use clear and meaningful variable names (e.g., 'age', 'salary', 'marks').
2. Comment complex operations for better understanding.
3. Test edge cases, like division by zero or unexpected inputs.
4. Use parentheses to clarify operator precedence (e.g., a + (b * c)).
5. Avoid overly nested or complex logic; split into smaller operations.
"""

# Python Type Conversion: A Comprehensive Guide

# Introduction:
# Type conversion refers to converting one data type into another.
# Python supports two types of type conversion:
# 1. Implicit Type Conversion (done automatically by Python)
# 2. Explicit Type Conversion (done manually by the programmer)

# ---------------------------------------------
# 1. Implicit Type Conversion
# Python automatically converts one data type to another where no data loss occurs.

print("Implicit Type Conversion Example:")

# Adding an integer and a float
num_int = 10
num_float = 5.5

result = num_int + num_float  # Python converts the integer to a float automatically
print("Result (num_int + num_float):", result)
print("Type of result:", type(result))  # Output type will be 'float'

# ---------------------------------------------
# 2. Explicit Type Conversion
# The programmer manually converts one data type into another using functions.

print("\nExplicit Type Conversion Example:")

# Converting float to integer
num_float = 9.8
num_int = int(num_float)  # Use int() to convert
print("Converted float to int:", num_int)

# Converting string to integer
str_num = "123"
num_int = int(str_num)  # Use int() to convert
print("Converted string to int:", num_int)

# Converting integer to string
num = 50
str_num = str(num)  # Use str() to convert
print("Converted int to string:", str_num)

# Converting integer to float
num_float = float(num)
print("Converted int to float:", num_float)

# Converting list to tuple
list_data = [1, 2, 3, 4]
tuple_data = tuple(list_data)  # Use tuple() to convert
print("Converted list to tuple:", tuple_data)

# Converting tuple to list
tuple_data = (5, 6, 7)
list_data = list(tuple_data)  # Use list() to convert
print("Converted tuple to list:", list_data)

# ---------------------------------------------
# Common Type Conversion Functions
"""
int(x)    -> Converts x to an integer
float(x)  -> Converts x to a float
str(x)    -> Converts x to a string
tuple(x)  -> Converts x to a tuple
list(x)   -> Converts x to a list
set(x)    -> Converts x to a set
dict(x)   -> Converts x to a dictionary (if x is in key-value pair format)
"""

# ---------------------------------------------
# Real-World Example: Adding User Input
# Note: User input is always stored as a string by default.

print("\nReal-World Example: Adding User Input")
num1 = input("Enter the first number: ")  # Input is a string
num2 = input("Enter the second number: ") # Input is a string

# Convert inputs to integers before performing addition
num1 = int(num1)
num2 = int(num2)

result = num1 + num2
print("Sum of the two numbers:", result)

# ---------------------------------------------
# Best Practices
"""
1. Always validate user input before converting it (e.g., ensure it's numeric before using int() or float()).
2. Be aware of potential data loss (e.g., converting float to int truncates decimal values).
3. Use explicit conversion only when necessary to avoid runtime errors.
4. Take advantage of type-checking functions like type() to debug issues.
"""

# Experiment with type conversion in Python to understand it better!

# Python Type Casting: A Comprehensive Guide

# Introduction:
# Type casting refers to the process of converting one data type into another.
# Python provides built-in functions for type casting, allowing programmers to control conversions explicitly.
# This is commonly used when handling user inputs or performing operations between different data types.

# ---------------------------------------------
# 1. What is Type Casting?
"""
Type casting is categorized into two forms:
1. Implicit Type Casting: Automatically performed by Python.
2. Explicit Type Casting: Manually performed by the programmer using casting functions like int(), float(), str(), etc.
"""

# ---------------------------------------------
# 2. Implicit Type Casting
# Python automatically converts smaller data types to larger data types to avoid data loss.

print("Implicit Type Casting Example:")

# Integer to Float Conversion
int_value = 10
float_value = 5.5

result = int_value + float_value  # Python automatically converts 'int_value' to float
print("Result:", result)  # Result will be float (15.5)
print("Type of result:", type(result))

# ---------------------------------------------
# 3. Explicit Type Casting
# You must manually convert data types using casting functions.

print("\nExplicit Type Casting Examples:")

# Example 1: Converting float to integer
float_value = 9.8
int_value = int(float_value)  # Use int() to truncate decimal part
print("Converted float to int:", int_value)

# Example 2: Converting string to integer
str_number = "123"
int_value = int(str_number)
print("Converted string to int:", int_value)

# Example 3: Converting integer to string
num = 50
str_value = str(num)
print("Converted int to string:", str_value)

# Example 4: Converting string to float
str_float = "45.67"
float_value = float(str_float)
print("Converted string to float:", float_value)

# Example 5: Converting list to tuple
list_data = [1, 2, 3]
tuple_data = tuple(list_data)  # Use tuple() to convert
print("Converted list to tuple:", tuple_data)

# Example 6: Converting tuple to list
tuple_data = (4, 5, 6)
list_data = list(tuple_data)  # Use list() to convert
print("Converted tuple to list:", list_data)

# ---------------------------------------------
# 4. Real-World Example of Type Casting
# Input Handling and Type Conversion

print("\nReal-World Example: User Input and Type Casting")

# User input is always stored as a string
age = input("Enter your age: ")  # Input will be string by default
age = int(age)  # Convert to integer for calculations
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ---------------------------------------------
# 5. Common Type Casting Functions
"""
1. int(x): Converts x to an integer (e.g., int("5") → 5)
2. float(x): Converts x to a floating-point number (e.g., float("5.6") → 5.6)
3. str(x): Converts x to a string (e.g., str(5) → "5")
4. list(x): Converts x to a list (e.g., list((1, 2, 3)) → [1, 2, 3])
5. tuple(x): Converts x to a tuple (e.g., tuple([1, 2, 3]) → (1, 2, 3))
6. set(x): Converts x to a set (e.g., set([1, 1, 2]) → {1, 2})
"""

# ---------------------------------------------
# 6. Best Practices for Type Casting
"""
1. Always validate user input before casting to avoid runtime errors.
   Example: Use str.isdigit() to ensure a string contains only digits before converting to int.
   
2. Be cautious of data loss:
   - Converting float to int will remove the decimal part.
   - Ensure this behavior is acceptable for your use case.

3. Use try-except blocks to handle conversion errors gracefully:
"""
try:
    value = int("abc")  # Trying to convert an invalid string to int
except ValueError as e:
    print(f"Error: {e} - Invalid input for type casting.")

# ---------------------------------------------
# Explore and Practice!
"""
1. Modify the provided examples and test various inputs.
2. Experiment with edge cases, like converting empty strings or extremely large numbers.
3. Combine type casting with other Python concepts (e.g., loops, functions) for real-world applications.
"""

# End of Notes

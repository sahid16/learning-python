# Taking input from the user and printing it

# Input different types of data from the user
name = input("Write your name: ")
age = int(input("Write your age: "))
price = float(input("Write the price of your book: "))

# Display the inputs back to the user
print("Your name is:", name)
print("Your age is:", age)
print("The price of your book is:", price)

# ---------------------------------------------

# Conditional statements: if-elif-else

# Example 1: Traffic Light Simulation
light = input("What color is the traffic light showing? ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down and look")
elif light == "green":
    print("Go")
else:
    print("The traffic light is not functioning properly.")

# ---------------------------------------------

# Example 2: Driving Eligibility
age = int(input("Enter your age: "))
print("Your age is:", age)

if age >= 18:
    print("You can drive.")
else:
    print("You can't drive.")

# ---------------------------------------------

# Example 3: Voting Eligibility
if age >= 18:
    print("You can vote.")
else:
    print("You can't vote.")

# ---------------------------------------------

# Example 4: Grading System
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("GRADE A")
elif 80 <= marks < 90:
    print("GRADE B")
elif 60 <= marks < 80:
    print("GRADE C")
else:
    print("GRADE D")

# ---------------------------------------------

# Ternary operators: Shortened conditional logic

# Example 1: Food Preference
food = input("Enter what you eat: ").lower()
response = "Yes" if food == "cake" else "No"
print("Do you like cake? ", response)

# Example 2: Sweet Checking
food = input("Enter food: ").lower()
print("Sweet") if food in ["jalebi", "cake"] else print("No sweet")

# Example 3: Clever ternary operator for voting eligibility
age = int(input("Enter your age: "))
vote = "Yes" if age >= 18 else "No"
print("Can you vote?", vote)

# ---------------------------------------------

# Example 4: Calculating TAX based on salary
salary = float(input("Enter your salary: "))
TAX = salary * (0.1 if salary < 50000 else 0.2)  # 10% if salary < 50000, else 20%
print(f"The tax you need to pay is: {TAX}")

# ---------------------------------------------

# Best practices in writing Python code (Summary)
"""
1. Use simple instructions for readability.
2. One instruction per task to avoid confusion.
3. Use short and meaningful variable names (e.g., 'age' instead of 'a').
4. Apply appropriate logic for solving problems.
5. Avoid complex expressions; break them into smaller parts.
6. Comment your code for clarity and better understanding.
7. Test edge cases when dealing with user inputs (e.g., empty input or invalid values).
"""

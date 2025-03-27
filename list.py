# ---------------------------------------------
# Lists in Python
# A list is a mutable (changeable) data structure that can store multiple items in a single variable.

# Example: Creating a List
marks = [9, 10, 3, 4, 6]
print("Original List:", marks)

# ---------------------------------------------
# List Methods: Performing common operations on lists

# Adding elements to a list
marks.append(8)  # Adds 8 to the end of the list
print("After append(8):", marks)

marks.insert(2, 7)  # Inserts 7 at index 2
print("After insert(2, 7):", marks)

# Removing elements from a list
marks.remove(3)  # Removes the first occurrence of 3 from the list
print("After remove(3):", marks)

popped_value = marks.pop()  # Removes the last element and returns it
print("After pop():", marks)
print("Popped Value:", popped_value)

# Modifying elements in a list
marks[0] = 99  # Replacing the value at index 0 with 99
print("After modifying index 0:", marks)

# Sorting the list
marks.sort()  # Sorts the list in ascending order
print("After sort():", marks)

# Reversing the list
marks.reverse()  # Reverses the list order
print("After reverse():", marks)

# Other useful operations
length = len(marks)  # Returns the number of elements in the list
print("Length of the list:", length)

# ---------------------------------------------
# Tuples in Python
# A tuple is an immutable (unchangeable) data structure used to store multiple items in a single variable.

# Example: Creating a Tuple
student_marks = (9, 10, 3, 4, 6)
print("\nOriginal Tuple:", student_marks)

# Accessing elements in a tuple
print("First Element (index 0):", student_marks[0])
print("Last Element (index -1):", student_marks[-1])

# Slicing a tuple
print("Sliced Tuple (index 1 to 3):", student_marks[1:4])

# Tuple Methods: Available operations on tuples
count = student_marks.count(10)  # Returns the number of occurrences of 10
print("Count of 10 in tuple:", count)

index = student_marks.index(4)  # Returns the index of the first occurrence of 4
print("Index of 4 in tuple:", index)

# ---------------------------------------------
# Key Differences Between Lists and Tuples
"""
1. Lists are mutable: You can modify, add, or remove elements.
   Example: marks[0] = 99 modifies the first element in a list.
   
2. Tuples are immutable: Once defined, you cannot change their contents.
   Example: student_marks[0] = 99 would raise a TypeError.

3. Lists use more memory and are slower compared to tuples.
   Use tuples when you need a fixed, unchangeable collection.
"""

# ---------------------------------------------
# Best Practices
"""
1. Use lists for collections that may change during the program.
2. Use tuples for fixed collections (e.g., coordinates, configuration values).
3. Use descriptive variable names (e.g., 'marks', 'student_scores') for readability.
4. Use list comprehensions for efficient list creation and processing.
   Example: squares = [x**2 for x in range(5)]
"""

# Experiment with the provided examples and modify them to deepen your understanding!

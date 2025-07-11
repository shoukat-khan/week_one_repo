#!/usr/bin/env python3
"""
Python Fundamentals: Variables, Functions, Conditionals, and Loops
This script demonstrates core Python concepts with practical examples.
"""

# ============================================================================
# VARIABLES AND DATA TYPES
# ============================================================================

print("=" * 60)
print("VARIABLES AND DATA TYPES")
print("=" * 60)

# Numeric variables
age = 25
height = 5.9
complex_num = 3 + 4j

# String variables
name = "Alice Johnson"
email = "alice.johnson@email.com"

# Boolean variables
is_student = True
is_employed = False

# List variables
hobbies = ["reading", "swimming", "coding"]
grades = [85, 92, 78, 96, 88]

# Dictionary variables
person = {
    "name": "Bob Smith",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}

# Tuple variables (immutable)
coordinates = (40.7128, -74.0060)
rgb_color = (255, 128, 0)

# Set variables (unique elements)
unique_numbers = {1, 2, 3, 4, 5, 5, 6}  # Duplicate 5 will be removed

print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print(f"Name: {name} (type: {type(name)})")
print(f"Is student: {is_student} (type: {type(is_student)})")
print(f"Hobbies: {hobbies} (type: {type(hobbies)})")
print(f"Person: {person} (type: {type(person)})")
print(f"Coordinates: {coordinates} (type: {type(coordinates)})")
print(f"Unique numbers: {unique_numbers} (type: {type(unique_numbers)})")

# ============================================================================
# FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTIONS")
print("=" * 60)

def greet(name, greeting="Hello"):
    """Simple function with default parameter"""
    return f"{greeting}, {name}!"

def calculate_area(length, width):
    """Calculate area of a rectangle"""
    return length * width

def calculate_circle_area(radius):
    """Calculate area of a circle"""
    import math
    return math.pi * radius ** 2

def get_grade(score):
    """Return letter grade based on numeric score"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def fibonacci(n):
    """Calculate Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    """Calculate factorial using iteration"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function with multiple return values
def get_name_parts(full_name):
    """Split full name into first and last name"""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]
    return full_name, ""

# Lambda function (anonymous function)
square = lambda x: x ** 2
add = lambda x, y: x + y

# Testing functions
print(greet("World"))
print(greet("Alice", "Good morning"))
print(f"Rectangle area: {calculate_area(5, 3)}")
print(f"Circle area: {calculate_circle_area(3):.2f}")
print(f"Grade for 85: {get_grade(85)}")
print(f"Fibonacci(8): {fibonacci(8)}")
print(f"Factorial(5): {factorial(5)}")

first, last = get_name_parts("John Doe Smith")
print(f"First: {first}, Last: {last}")

print(f"Square of 7: {square(7)}")
print(f"Sum of 10 and 20: {add(10, 20)}")

# ============================================================================
# CONDITIONALS
# ============================================================================

print("\n" + "=" * 60)
print("CONDITIONALS")
print("=" * 60)

def check_number(num):
    """Demonstrate if-elif-else statements"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def check_age_category(age):
    """Demonstrate nested conditionals"""
    if age >= 0:
        if age < 13:
            return "Child"
        elif age < 20:
            return "Teenager"
        elif age < 65:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"

def check_password_strength(password):
    """Check password strength using multiple conditions"""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    length_ok = len(password) >= 8
    
    if score >= 3 and length_ok:
        return "Strong"
    elif score >= 2 and length_ok:
        return "Medium"
    else:
        return "Weak"

# Testing conditionals
test_numbers = [-5, 0, 10]
for num in test_numbers:
    print(f"{num} is {check_number(num)}")

test_ages = [5, 15, 25, 70]
for age in test_ages:
    print(f"Age {age}: {check_age_category(age)}")

passwords = ["abc", "password123", "MyP@ssw0rd", "STRONG123!"]
for pwd in passwords:
    print(f"Password '{pwd}': {check_password_strength(pwd)}")

# ============================================================================
# LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("LOOPS")
print("=" * 60)

# For loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# For loop with list
print("\nIterating through a list:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"  I like {fruit}")

# For loop with enumerate
print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index + 1}. {fruit}")

# For loop with dictionary
print("\nIterating through dictionary:")
for key, value in person.items():
    print(f"  {key}: {value}")

# While loop
print("\nWhile loop example:")
count = 0
while count < 3:
    print(f"  Count is {count}")
    count += 1

# Loop with break
print("\nLoop with break:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}")

# Loop with continue
print("\nLoop with continue:")
for i in range(5):
    if i == 2:
        continue
    print(f"  {i}")

# List comprehension
print("\nList comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"  Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"  Even squares: {even_squares}")

# Dictionary comprehension
print("\nDictionary comprehension:")
word_lengths = {word: len(word) for word in fruits}
print(f"  Word lengths: {word_lengths}")

# Nested loops
print("\nNested loops (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")

# ============================================================================
# PRACTICAL EXAMPLE: STUDENT GRADE CALCULATOR
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: STUDENT GRADE CALCULATOR")
print("=" * 60)

def calculate_average(scores):
    """Calculate average of scores"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def analyze_student_performance(student_name, scores):
    """Analyze student performance and provide feedback"""
    if not scores:
        return "No scores provided"
    
    average = calculate_average(scores)
    highest = max(scores)
    lowest = min(scores)
    grade = get_grade(average)
    
    print(f"\nPerformance Analysis for {student_name}:")
    print(f"  Scores: {scores}")
    print(f"  Average: {average:.2f}")
    print(f"  Highest: {highest}")
    print(f"  Lowest: {lowest}")
    print(f"  Grade: {grade}")
    
    # Provide feedback based on performance
    if average >= 90:
        print("  Feedback: Excellent work! Keep it up!")
    elif average >= 80:
        print("  Feedback: Good job! You're doing well.")
    elif average >= 70:
        print("  Feedback: You're passing, but there's room for improvement.")
    else:
        print("  Feedback: You need to work harder to improve your grades.")
    
    return grade

# Test the student grade calculator
students = {
    "Alice": [95, 88, 92, 96, 90],
    "Bob": [75, 82, 78, 85, 80],
    "Charlie": [65, 70, 68, 72, 69]
}

for student, scores in students.items():
    analyze_student_performance(student, scores)

print("\n" + "=" * 60)
print("END OF VARIABLES, FUNCTIONS, CONDITIONALS, AND LOOPS")
print("=" * 60) 